# Javascript의 변수 선언 방식

: var, let, const



1. var은 변수 재선언이 가능하다.

```javascript
var name = 'bathingape'
console.log(name) // bathingape

var name = 'javascript'
console.log(name) // javascript
```

위와 같은 결과가 나오는데, 이는 var이 변수를 재선언하는것이 가능하기 때문이다.



2. let : 변수에 재할당이 가능하다.

```javascript
let name = 'bathingape'
    console.log(name) // bathingape

    let name = 'javascript'
    console.log(name) 
    // Uncaught SyntaxError: Identifier 'name' has already been declared

    name = 'react'
    console.log(name) //react
```



3. const : 변수 재선언, 변수 재할당이 모두 불가능하다.

```javascript
const name = 'bathingape'
console.log(name) // bathingape

const name = 'javascript'
console.log(name) 
// Uncaught SyntaxError: Identifier 'name' has already been declared

name = 'react'
console.log(name) 
//Uncaught TypeError: Assignment to constant variable.


```







