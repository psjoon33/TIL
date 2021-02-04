# v-directive

### 조건문과 반복문 : v-if / v-for



**1. v-if**

```html
<div id="app-3">
    <p v-if="seen">
        이제 나를 볼 수 있어요!
    </p>
</div>
```

```javascript
var app3 = new Vue({
    el: #app-3,
    data: {
    	senn: true
	}
 })
```

--> ``` 이제 나를 볼 수 있어요```

v-if : 요소를 화면에 렌더링 할 것인지, 안 할 것인지를 결정할 수 있다. 

​		== 존재 여부를 토글하는 것 (토글 = 데이터를 껐다 켰다하는 것)

​	  : ture이면 보여주고, false이면 보여주지 않음.



**2. v-for**

```html
<div id="app-4">
    <ol>
        <li v-for="todo in todos">
        	{{ todo.text }}
        </li>
    </ol>
</div>
```

```javascript
var app4 = new Vue({
    el: #app-4,
    data: {
    	todos: [
    		{text: 'JavaScript 마스터하기'},
            {text: 'Vue 마스터하기'},
            {text: 'React도 마스터해버리기!'}
			]
		}
	})
```

```python
# 결과
1. JavaScript 마스터하기
2. Vue 마스터하기
3. React도 마스터해버리기!
```



**v-for를 쓸 때의 주의사항!!**

초기에는 많이 사용 안해서 괜찮지만,

나중되면 v-for에 많은 것들을 반복해서 돌릴 때 중복된다는 것과 같은, 문제가 생길수도 있다.

그래서 , html 부분에 v-for="" 부분의 옆에 항상 ```v-bind:key=""``` 를 추가해서 입력해준다.

ex) 위의 javascript 부분에서 {text: 'Javascript 마스터하기'} 에 id: '1'과 같은 것들을 고유하게 보여하면, v-bind:key="todo.id" 가 될 것이다.



-----

### 사용자 입력 핸들링

**1. v-on **: 사용자가 앱과 상호 작용할 수 있게 하기 위해, v-on을 이용하면 vue 인스턴스에서 메소드를 호출하는 이벤트 리스너를 추가할 수 있다.

```html
<div id="app-5">
  <p>{{ message }}</p>
  <button v-on:click="reverseMessage">메시지 뒤집기</button>
</div>
```

```javascript
var app5 = new Vue({
  el: '#app-5',
  data: {
    message: '안녕하세요!'
  },
  methods: {
    reverseMessage: function () {
      this.message = this.message.split('').reverse().join('')
    }
  }
})
```



: 의미를 해석해보면, 일단 기본적으로 {{ message }} 에 해당하는 부분이 띄워짐

그리고 메시지 뒤집기라는 버튼이 있다. 

그리고 이 버튼을 클릭하게 되면 v-on:click에서 이 클릭을 감지하고, reverseMessage라는 메서드를 실행시킨다.

```python
#결과
안녕하세요
<button>메시지 뒤집기</button>

#에서 버튼을 클릭하면
요세하녕안
<button>메시지 뒤집기</button>

#으로 바뀐다.
```



**2. v-model**  : 양식에 대한 입력과 앱 상태를 양방향으로 바인딩하는 디렉티브

```html
<div id="app-6">
  <p>{{ message }}</p>
  <input v-model="message">
</div>
```

```javascript
var app6 = new Vue({
  el: '#app-6',
  data: {
    message: '안녕하세요 Vue!'
  }
})
```

```python
#결과
#일단 기본적으로 안녕하세요 Vue! 라고 떠있고,
#밑에는 input 에 마찬가지로 안녕하세요 Vue!라고 입력이 되어 있다.

안녕하세요 Vue!
<input>안녕하세요 Vue!
```

```python
# 그런데 여기서, input안에 있는거를 지우고 다른 것을 입력하면, 인풋위에 있는 텍스트도 변한다.

너는 내가 마스터한다 Vue!
<input>너는 내가 마스터한다 Vue!

```













