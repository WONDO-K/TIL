# 얕은 복사와 깊은 복사
자바에서 객체를 복사할 때 얕은 복사와 깊은 복사라는 두 가지 방식이 있다.
## 먼저 Book과 Author라는 두 클래스를 사용한 예제
> Book은 책의 이름(name)과 저자(author) 정보를 가직 있고, Author는 저자의 이름을 가지고 있다.
```java
class Book {

    private String name; // 책 이름
    private Author author; // 저자

    public Book(String name, Author author) {
        this.name = name;
        this.author = author;
    }

    public Book shallowCopy() { // 얕은 복사
        return new Book(this.name, this.author);
    }

    public Book deepCopy() { // 깊은 복사
        Author copiedAuthor = new Author(this.author.getName());
        return new Book(this.name, copiedAuthor);
    }

    public void changeAuthor(String name) { // 저자 이름 변경
        author.setName(name);
    }

    @Override
    public String toString() {
        return "Book name : " + name + ", " + author;
    }

    static class Author {

        private String name; // 저자 이름

        public Author(String name) {
            this.name = name;
        }

        public String getName() { // 저자 이름 반환
            return name;
        }

        public void setName(String name) { // 저자 이름 변경
            this.name = name;
        }

        @Override
        public String toString() {
            return "Author : " + name;
        }
    }

    public static void main(String[] args) {
        Author author1 = new Author("동운오");
        Book book1 = new Book("농사직설", author1);

        // 얕은 복사 후 변경
        Book shallowCopyBook = book1.shallowCopy();
        shallowCopyBook.changeAuthor("Dong Woonoh");

        // 얕은 복사 결과 출력
        System.out.println("After shallow copy and change:");
        System.out.println("Original book1: " + book1);
        System.out.println("Shallow copied book: " + shallowCopyBook);

        Author author2 = new Author("동까");
        Book book2 = new Book("통풍을 이기는 비결", author2);

        // 깊은 복사 후 변경
        Book deepCopyBook = book2.deepCopy();
        deepCopyBook.changeAuthor("Dong Kka");

        // 깊은 복사 결과 출력
        System.out.println("
After deep copy and change:");
        System.out.println("Original book2: " + book2);
        System.out.println("Deep copied book: " + deepCopyBook);
    }
}
```
- shallowCopy()
    - Book 객체는 새로 만들되, 내부의 Author 객체는 기존 Book이 참조하던 것을 그대로 사용한다.
    - 즉, 두 Book 인스턴스가 같은 Author 인스턴스를 참조하게 된다.
    - 예를 들어, shallowCopyBook의 저자 이름을 바꾸면, book1의 저자 이름도 함께 바뀐다.
- deepCopy()
    - Book과 Author 모두 새롭게 복제된 객체로 생성된다.
    - 즉, 원본 Book의 Author와 복사된 Book의 Author는 서로 다른 인스턴스이다.
    - 따라서 deepCopyBook의 저자 이름을 변경해도, 원본 book2의 Author는 영향을 받지 않는다.
## 출력 결과
### book1
```java
After shallow copy and change:
Original book1: Book name : 이펙티브 자바, Author : Dong Woonoh
Shallow copied book: Book name : 이펙티브 자바, Author : Dong Woonoh
```
> 얕은 복사에서 shallowCopyBook과 book1이 같은 Author를 공유하니까, shallowCopyBook의 저자 이름을 바꾸면 book1의 저자 이름도 바뀐 것.

### book2
```java
After deep copy and change:
Original book2: Book name : 리팩터링, Author : 동까
Deep copied book: Book name : 리팩터링, Author : Dong Kka
```
> 깊은 복사한 deepCopyBook과 book2는 서로 다른 Author 객체를 참조하니까, deepCopyBook의 저자 이름을 바꿔도 book2는 영향을 받지 않는다.

