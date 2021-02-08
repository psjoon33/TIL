# Router-link 연결하기

1. html 부분에서 event 설정해놓고, 그 event가 발생하면, 밑에 javascript 부분에 설정해 놓은 대로 이동하기.

```html
@click="toHome"
```

```javascript
methods: {
    toHome () {
        this.$router.push('/home')
    },
}
```



2. 바로 html 에서 연결해버리기

```html
<h2 @click="$router.push('/home')">
    HOME
</h2>
```



3. router-link 이용하기

```html
<router-link to="/home">
	HOME
</router-link>

#이 때, router-link랑 2번의 h2 태그랑 같게 하기 위해서 뒤에 tag="h2" 를 붙힌다.
```

