# Class & Method

- Class : 객체들의 분류를 정의할 때 쓰이는 키워드
- 클래스 내부에는 함수를 정의할 수 있고, 이 때 정의된 함수를 바로 Method(메서드)라고 부른다.

```python
class Person:
    <method>
```



- 정의된 클래스에 속하는 개체를 해당 클래스의 인스턴스(instance)라고 한다.
- Person 이라는 클래스의 인스턴스는 Person() 을 호출함으로써 생성할 수 있다.

```python
person1 = Person()
```



- 메서드의 정의

```python
class Person:
    def talk(self):
        return '안녕!'
    
# Person이라는 클래스를 정의
# talk이라는 메서드를 정의
# 이 때 중요한 것은, 함수의 형태와 비슷한 형태로 정의한다는 것.
# self 인자를 넣는다는 것.
```

- 메서드 활용

```python
person1 = Person()
#인스턴스의 선언
person1.talk()

#--> '안녕!'
```



- 또한, 메서드도 함수이기 때문에 추가적인 인자를 받을 수 있다.

```python
class Person:
    def talk(self):
        return '안녕'
    def eat(self, food='먹을거줘'):
        return f'{food} 냠냠'
    
# f-string을 이용하였다.
# food에다가 기본값으로 '먹을거줘' 를 설정하였다.
```



- 생성자 메서드와 소멸자 메서드

- 생성자 : ```__init__(self):```

- 소멸자 : ```__del__(self):```

  : 약간 어떤 느낌이냐면 생성되면 뭔가가 작동하고, 사라지면서도 뭔가가 작동하는 느낌.

```python
class Person:
    def __init__(self):
        print('응애!')
    def __del__(self):
        print('깨꼬닥!')
# 생성되면 '응애!', 소멸되면 '깨꼬닥!'을 출력하는 클래스 설정
```

```python
p1 = person()

#-=-> '응애'
```

```python
del p1

#--> '깨꼬닥!'
```

```python
p1 = Person()
p1 = 'hello'

#--> 응애 
#--> 깨꼬닥!

#이는 일단, 생성되면서 '응애' 하고 / 'hello'라고 설정함으로써 더이상 instance가 아닌 것!
#그래서 클래스에서 삭제되었으므로, '깨꼬닥!'
```



### 속성(Attribute)

- 활용법

```python
class Person:
    def __init__(self, name):
        self.name = name
        
    def talk(self):
        return f'안녕! 나는 {self.name}'
```



- 실습

```python
class handsome:
    def __init__(self, name, score):
        self.name = name
        self.score = score
    def appeal(self):
        return f'안녕! 잘생긴 내 이름은 {self.name}이야. 내 아만다 점수는 {self.score}이다!'
        
```

```python
me = handsome('성준', '4.5')
me.appeal()

#--> '안녕! 잘생긴 내 이름은 성준이야. 내 아만다 점수는 4.5이다!'
```

