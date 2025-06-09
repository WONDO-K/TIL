# RequestBody VS ModelAttribute의 차이점
이들은 클라이언트 측에서 보낸 데이터를 Java 객체로 만들어주는데 ReqeustBody는 요청의 본문(Body)에 있는 값을 바인딩할 때 사용하고, ModelAttribute는 요청 파라미터나 multipart/form-data 형식을 바인딩할 때 사용한다.

## RequestBody
- 클라이언트가 보내는 요청의 본문을 자바 객체로 변환한다.
- 내부적으로 HttpMessageConverter를 거치는데, 이떄 ObjectMapper를 통해 JSON 값을 Java객체로 역직렬화 한다.
- 따라서 변환될 Java 객체에 기본 생성자를 정의해야 하고, getter나 setter를 선언해야 한다.
- cf.record에 기본 생성자를 따로 정의하지 않았는데 역직렬화가 되는 이유
    - record는 기본생성자를 자동으로 제공하지 않는 대신, '모든 필드를 초기화하는 생성자'를 제공한다.
    - jackson은 일반 객체와 달리, record를 역직렬화할 때는 '모든 필드를 초기화하는 생성자'를 사용해 역직렬화하기 때문이다.

## ModelAttribute
- 두가지 사용법
- 첫번째 사용법인 메서드 단에서의 사용법은 jsp의 Model에 하나 이상의 속성을 추가하고 싶을 때 사용한다.
    - e.g. model.addAttribute(“속성 이름”, “속성 값”)
- 두번째 사용법인 인자 단에서의 사용으로 클라이언트가 보내는 요청의 파라미터나 multipart/form-data 형식의 데이터를 자바 객체로 변환한다.
- 내부적으로 ModelAttributeMethodProcessor를 거치는데, 이때 지정된 클래스의 생성자를 찾아 객체롤 변환한다.