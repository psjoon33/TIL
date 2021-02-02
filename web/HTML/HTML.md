# HTML

**a 태그**

: 링크를 걸어줄 수 있는 태그

```html
<a href="https://www.naver.com">네이버로 고고!</a>

#라고 입력을 하면 네이버로 고고! naver로 가는 링크가 걸린다.
```



**시맨틱 태그**

HTML에서 의미론적 요소를 담은 태그의 등장

대표적인 태그들..

- header : 문서 전체나 섹션의 헤더(머릿말 부분)
- nav : 내비게이션
- aside, section, article, footer 등등



**그룹 컨텐츠에 이용하는 태그**

- p 태그
- hr 태그 : 문서의 중간에 선을 긋는 태그
- ol 태그 : orderd list :  1, 2, 3, 4, ,,, 처럼 번호를 붙힌 리스트
- ul 태그 : unorderd list : 번호를 안 붙히는 리스트
- div



**텍스트 관련 요소**

- span 태그 : 인라인 태그 : 

  : div  태그와 마찬가지로 특별한 기능을 가지고 있는 것은 아니다. 하지만, inline이라는 속성이 있다.

  즉, div태그는 줄바꿈이 되지만, span 태그는 줄바꿈이 일어나지 않는다.

- br :  줄바꿈

- img :  이미지 태그



**form 태그**

: 서버에서 처리될 데이터를 제공하는 역할

- form 의 기본 속성
  - action : 입력받은 값을 어디로 보낼지
  - method : GET / POST



**input 태그**

: 다양한 타입을 가지는 입력 데이터 필드

공통 속성

- name , placeholder
- required
- autofocus















# FLEXBOX

: container / box

**container에 부여할 수 있는 속성**

- display
  - flex (ex. display : flex;)
- flex-direction : 방향을 설정
  - row
  - row-reverse
  - column
  - column-reverse
- flex-wrap
  - wrap 
  - wrap-reverse
  - nowrap
- flex-flow
  - flex-direction 과 flex-wrap 을 합침
  - ex) flex-flow : column, wrap 



**container의 속성 중 아이템들의 배치에 이용**

- justify-content
- align-items
- align-content

**item에 부여할 수 있는 속성**

- order
- flex-grow
- flex-shrink
- flex
- align-self















