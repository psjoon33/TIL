# 반응형 웹사이트를 만들기 위한 CSS Units

유닛에는 크게 2가지가 있다.

바로 절대적인 값과 상대적인 값.

절대적인 값에는 주로 px를 사용한다.

하지만 이 px를 사용하게 된다면 화면의 크기가 변화해도 글자의 크기가 변하지 않는다.

그래서 주로 %를 이용해서 부모에 대한 비율을 이용하는 경우가 많다.



### 상대적인 유닛이 중요!!

: em, rem, vw, vh, %



1. em : 부모에 대한 비율...

   ex) 일단 브라우저의 기본 1em = 16px

   그래서 .parent { font-size: 8em; }

    이고, child { font-size: 0.5em} 이라고 설정되어 있으면

   parent는 1em이 기본값인 16px이므로 , 128px이며

   child는 부모, 즉, parent에서의 기본값인 128px의 0.5배인 64em 이다.

   **사실, 0.5em이라는 것은 50%라는 것과 같은 의미이다.**



2. rem : 부모가 아니라 root에 지정된 폰트 사이즈에 대한 비율

   위의 em에서의 예를 그대로 가져와서 child가 0.5rem이면 8px이된다.

   

3. vw : viewport의 width...

   : 브라우저의 너비에 대한 백분율을 의미한다.

   그래서 50vw라는 것은 브라우저의 너비에 대한 50%

4. vh : viewport의 height

   : 브라우저의 높이에 대한 백분율을 의미한다.

   그래서 50vh라는 것은 브라우저의 높이에 대한 50%

