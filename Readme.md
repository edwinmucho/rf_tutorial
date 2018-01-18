# REST FRAMEWORK
* Serializer : 모델 객체를 json으로 변환.
   - 사용법은 Django의 Form과 유사함.
* Request/Response/API view/ suffix URL
   - 요청된 type으로 자동으로 렌더링됨.
   - URL을 유연하게 처리
* Class Based View
   - mixins 이용 (간결하게 표현가능)
   - generics 이용 (매우 간결해짐)
* Authentication & Permissions
  - User 추가후 Serializer 부분과 View 부분에 User 연결 및 권한 설정(로그인 유무/ 글쓴이인지/ 읽기전용인지)
  - urls.py(project folder에서) api-auth 추가시 우측 상단에 log-in 버튼이 생김
* Relationships & Hyperlinked APIs
  - 각각의 관계를 설정 가능(어디에 속하고 그런것들..)
* Viewsets & Routers
  - View와 Url 패턴쪽을 간결하게 나타낼수 있음. (명백하게 표현되기 보다는 추상적이라 가독성이 떨어질수도 있음.)
 
 