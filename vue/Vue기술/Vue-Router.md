# Vue-Router

vue가 설치된 상황에서,,,,

```bash
# vue-router 를 설치하기 위해서 터미널에 입력

npm i vue-router
```



이렇게 vue-router가 설치가 완료되면, 라우터의 구성 파일을 만들어서 그 구성 파일을, 프로젝트의 최상위 부분에 있는 vue instance 부분에 연결을 해줘야한다.

그리고 이 파일이 바로 **main.js**

이제 라우터의 구성 파일을 만들어야 한다.

1. 최상위 위치에 새로운 디렉토리를 하나 만든다. 이름은 **'router'**
2.  그리고 이 router 폴더 안에 파일을 하나 생성 . == > **'index.js'**
3. index.js 안에 코드 작성

```javascript
import Vue from 'vue'
import VueRouter from 'vue-router'

# 2개의 모듈을 불러온다.
# 그리고 Vue안에서 VueRouter가 사용이 되게 해야 하므로,,,
Vue.use(VueRouter)

# 그 다음 routes라는 배열을 만들어서 사용한다.
const routes = [
    
]

# 이 구성된 routes를 가지고 main.js로 가서 세팅을 해야 한다.
export default new VueRouter(){
    routes
    # 위에서 만든 routes라는 배열을 export 
}
```

이제는 routes 배열 부분 안에 계속 추가해주면 된다.



4. main.js

```javascript
#기존의 
import Vue from 'vue'
import App from './App'
#의 아래에
# import router from './router/index.js' 를 입력하면 되는데,, index는 원래 생략이 가능하므로, 다음과 같이 입력한다.
import router from './router' 

new Vue({
    el: '#app',
    render: h => h(App),
})
# 기존의 입력에서 vue instance는 router라는 데이터를 설정함으로써 받아낼 수 있다.
# 그래서 router를 추가해준다.

new Vue({
    el: '#app',
    router,
    render: h => h(App),
})

# 여기서 원래는 router:router를 추가해줘야 하는데, 같아서 그냥 router를 추가하면 된다.
```



여기까지가 되면 일단 연결은 되었다 라고 생각하면 된다.

여기서 추가할 것은 index.js 를 수정함으로써 해나가면 된다.



**Home.vue라는 파일을 생성하고, 이 파일을 url 로 연결하기**

5. index.js에 입력한다.

```javascript
import Vue from 'vue'
import VueRouter from 'vue-router'

#3. Home이라는 컴포넌트를 불러온다. 
import Home from '../views/Home.vue'

Vue.use(VueRouter)

const routes = [
    {
        path: '/',   #1. path 설정 (기본뒤에 붙는 거를 입력하면 된다.)
        component: Home,    #2. Home이라는 component를 연결한다.
    }
]

export default new VueRouter({
    routes
})
```



6. 그리고 이제 위치에 맡게 views 라는 디렉토리 내에 Home.vue 를 생성하면 연결이 된다.

























