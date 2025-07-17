# Spring Data JPA에서 새로운 Entity인지 판단하는 방법

```java
@Override
public boolean isNew(T entity) {

    // @Version 필드가 존재하지 않거나,
    // 혹은 해당 필드의 타입이 primitive 타입이라면
    if(versionAttribute.isEmpty()
          || versionAttribute.map(Attribute::getJavaType)
                             .map(Class::isPrimitive) // primitive 타입인지 여부 확인
                             .orElse(false)) {
        // primitive는 null이 될 수 없어 버전 기반 신규 판단이 어려움 → 상위 로직(super)으로 위임
        return super.isNew(entity);
    }

    // version 필드가 존재하고, 타입이 wrapper 클래스(Long, Integer 등)이라면
    // BeanWrapper를 통해 해당 필드 값을 직접 꺼내 null 여부로 신규 판단
    BeanWrapper wrapper = new DirectFieldAccessFallbackBeanWrapper(entity);

    // version 값이 null이면 아직 DB에 저장되지 않은 새 엔티티로 간주
    return versionAttribute.map(it -> wrapper.getPropertyValue(it.getName()) == null)
                           .orElse(true);
}
```
- 새로운 Entity인지 여부는 JpaEntityInformation의 isNew(T entity)에 의해 판단한다. 
- 다른 설정이 없으면 JpaEntityInformation의 구현체 중 JpaMetamodelEntityInformation 클래스가 동작한다. 
- @Version이 사용된 필드가 없거나 @Version이 사용된 필드가 primitive 타입이면 AbstractEntityInformation의 isNew()를 호출한다.
- @Version이 사용된 필드가 wrapper class이면 null여부를 확인한다.

```java
public boolean isNew(T entity) {

    // ID 값 추출
    Id id = getId(entity);
    Class<ID> idType = getIdType();

    // ID 타입이 primitive가 아니라면 (e.g., Long, Integer)
    // null 여부로 신규 여부 판단
    if (!idType.isPrimitive()) {
        return id == null;
    }

    // ID가 Number 계열이라면 값이 0인지 체크하여 신규 판단
    if (id instanceof Number) {
        return ((Number) id).longValue() == 0L;
    }

    // 그 외 primitive 타입은 지원하지 않음
    throw new IllegalArgumentException(String.format("Unsupported primitive id type %s", idType));
}
```
- @Version이 사용된 필드가 없어서 AbstractEntityInformation 클래스가 동작하면 @Id 어노테이션을 사용한 필드를 확인해서 primitive 타입이 아니라면 null 여부, Number의 하위 타입이면 0인지 여부를 확인한다.
- @GeneratedValue 어노테이션으로 키 생성 전략을 사용하면 데이터베이스에 저장될 때 id가 할당됩니다. 따라서 데이터베이스에 저장되기 전에 메모리에서 생성된 객체는 id가 비어있기 때문에 isNew()는 true가 되어 새로운 entity로 판단한다.

## 💡 추가 설명: @Version 필드의 타입에 따른 신규 엔티티 판단 차이

| 타입 | 설명 | 신규 판단 방식 |
|------|------|----------------|
| `primitive` (`int`, `long` 등) | null 불가능 → 버전 필드로는 신규 판단 불가 | ID 기반으로 판단 (e.g., null, 0) |
| `wrapper` (`Integer`, `Long` 등) | null 가능 → 버전 값이 null이면 신규로 판단 가능 | version == null 여부 확인 |

- 따라서 `@Version` 필드가 wrapper 타입인 경우, 직접 해당 값이 null인지 확인하여 `persist()` 또는 `merge()`를 선택하게 됩니다.
- 반면 primitive 타입이면 무조건 값이 존재하므로 version 기반으로는 신규 여부를 판단할 수 없어 `super.isNew()`에서 ID 기반으로 판단합니다.

## 직접 ID를 할당하는 경우에는 어떻게 동작하는가?
키 생성 전략을 사용하지 않고 직접 ID를 할당하는 경우 새로운 entity로 간주되지 않는다.
이 때는 엔티티에서 Persistable<T> 인터페이스를 구현해서 JpaMetamodelEntityInformation 클래스가 아닌 JpaPersistableEntityInformation의 isNew()가 동작하도록 해야한다.

```java
public class JpaPersistableEntityInformation<T extends Persistable<ID, ID> 
        extends JpaMetamodelEntityInformation<T, ID> {

    public JpaPersistableEntityInformation(Class<T> domainClass, Metamodel metamodel, 
            PersistenceUnitUtil persistenceUnitUtil) {
        super(domainClass, metamodel, persistenceUnitUtil);
    }

    @Override
    public boolean isNew(T entity) {
        return entity.isNew();
    }

    @Nullable
    @Override
    public ID getId(T entity) {
        return entity.getId();
    }
}
```

## 새로운 Entity인지 판단하는게 왜 중요할까?
```java
@Override
@Transactional
public <S extends T> S save(S entity) {

    Assert.notNull(entity, "Entity must not be null");

	if (entityInformation.isNew(entity)) {
		entityManager.persist(entity);
		return entity;
	} else {
		return entityManager.merge(entity);
	}
}
```

- SimpleJpaRepository의 save() 메서드에서 isNew()를 사용하여 persist를 수행할지 merge를 수행할지 결정한다.
- 만약 ID를 직접 지정해주는 경우에는 신규 entity라고 판단하지 않기 때문에 merge를 수행한다. 
- 이때 해당 entity는 신규임에도 불구하고 DB를 조회하기 때문에 비효율적이다.
- 따라서, 새로운 entity인지 판단하는 것은 중요한 부분이다.

---

면접에서는 이렇게 나올 수 있어요:

> **Q. JPA에서 엔티티가 새로운 객체인지 어떻게 판단하나요?**

✅ 답변 예시:

> `JpaEntityInformation`의 `isNew()` 메서드를 통해 판단하며, `@Version` 필드가 존재한다면 wrapper 타입일 경우 `null` 여부로 신규 여부를 결정합니다.  
> 만약 primitive 타입이면 `null`이 될 수 없어 `ID` 값의 존재 여부나 값(예: 0)을 기준으로 판단하게 됩니다.