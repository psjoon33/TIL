# pjt08

**저번주에 했던거랑 똑같다! vue를 이용해서!**



목표 

- 영화 정보를 제공하는 SPA 제작



컴포넌트 구조를 봤을 때, 우선 vue-cli를 이용해서 project를 생성한다.

(vue-create <프로젝트이름>)

거기에다가 vue router를 등록해준다. 그러면 router-view가 자동으로 생성된다.

(vue add router)

그래서 여기서 3가지 vue를 만든다.

home.vue (전체 영화 목록 페이지)

random.vue (랜덤 영화 추천 페이지)

mymovielist.vue (개인 영화 리스트 페이지)

이렇게 3가지를 만든다.



Home.vue의 내부에 MovieCard.vue 를 v-for를 이용해서 반복문으로 100개를 출력하면 된다.

home.vue에서 영화정보 100개를 가져온 다음에,, 그걸 NovieCard.vue라는 컴포넌트로 반복적으로 출력하기 위해서는 써야하는 라이브러리가 있다.



1. Home

100개의 영화정보가 담긴 제이슨파일은 제공을 받을 것이다. axios라는 라이브러리를 통해 AJAX 요청을 보낸다.

이렇게 데이터를 가져온 데이터 안에서 필요한 정보들을 쏙쏙 뽑아내는 것

(영화 포스터, 제목, 줄거리 데이터, (title, overview, poster_path)이렇게 3가지의 정보들을 카드 컴포넌트에 넣고 반복 출력 해주면 된다. )



2.  Random

랜덤으로 보여주는 것

이거는 그냥 지난주에 했던 점심메뉴 추천 이거랑 똑같은 거라고 생각을 하면 된다.

미리 영화를 한 5개를 고르고,,, random.vue안에 데이터 속성에다가 리스트 하나를 만든다.

그리고 그 리스트 안에다가 미리 정한 5개 영화를 넣는다.

 그리고 그거를 랜덤 추출하면 된다.

이 때 사용해야 하는 라이브러는 바로 lodash('__') 



3. MyMovieList

 지난 금요일에 했던 todolist랑 거의 비슷한 것으로,,

보고싶은 영화를 검색하면 목록이 저장된다.

vuex를 이용하여 데이터를 저장한다.

(ㅈ됐다)

MyListForm.vue는 데이터를 입력하고 저장하는 기능을 가진 컴포넌트이다.

MyList.vue는 저장된 데이터를 출력하는 기능을 가진 컴포넌트이다.



4. 추가적인 스타일링

vue에서 bootstrap을 적용하는 방법

```html
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.5.3/dist/css/bootstrap.min.css" integrity="sha384-TX8t27EcRE3e/ihU7zmQxVncDAy5uIKz4rEkgIXeMed4M0jlfIDPvg6uqKI2xXr2" crossorigin="anonymous">
```

위의 것을 복사해서 index.html에서 head에 title태그 밑에다가 붙혀넣기 하면 bootstrap이 적용된다.