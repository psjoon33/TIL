# SET & Dictionary

### SET

: 변경 가능하고, 순서가 없고, 순회는 가능한

: mutable, unordered, iterable

: SET는 일종의 집합이라고 생각하면 된다. 즉 내부에 중복되는 요소가 존재하지 않는다.



- 비어있는 SET의 선언

```python 
a = set()
a.add(5)
print(a)
#-->{5}
```



- .add(element)

  : set에 element를 추가한다. 이 때 성분은 한 번에 하나만 추가가능.

  

- .update(*others)

  : 여러가지의 값을 한 번에 추가하고 싶을 때 이용한다.

```python
a = {'사과', '바나나', '수박'}

a.update({'토마토', '토마토', '딸기'})

print(a)

#--> {'딸기', '바나나', '수박', '토마토', '사과'}
```

​	: 이 때 주의할 점은 update() 안에 하나의 set만 들어가지 않아도 된다. ->  여러가지의 set 한 번에 추가 가능!!

```python
a = {'사과', '바나나', '수박'}

a.update({'토마토', '토마토', '딸기'}, {'포도', '레몬'})
print(a)

#--> {'딸기', '바나나', '수박', '토마토', '사과', '레몬', '포도'}
# 이렇게 중복된 값은 당연히 사라지고, 또한, 여러개의 set를 한 번에 추가할 수 있다.
```



- . remove(x) 

​	: set내에서 x라는 element를 삭제한다. 이 때, 없으면 Error

​	--> 리스트에서랑 똑같다.



- .discard(elem)

  : .remove와 똑같이 성분을 삭제하는 기능을 한다.

  : 하지만, 없더라도 Error가 나오지 않는다.

```python
a = {'사과', '바나나', '수박'}
a.discard('포도')
a.discard('수박')
print(a)

#-->{'바나나', '사과'}
# 이 처럼, 만약에 discard하려는 성분이 없으면 그냥 아무런 변화도 일어나지 않는다.
```



###  Dictionary (중요!)

: 변경 가능하고, 순서가 없고, 순회 가능한

: mutable, unordered, iterable

: {key: value}의 구조

: 비어 있는 딕셔너리 선언할 때는, ```a = {}```만 하면 된다. 혹은 ```a=dict()```



- .get(key[ , default])

  : key를 통해 value를 가져온다. default는 기본적으로 None이다.

```python
my_dict = {'apple': '사과', 'banana': '바나나', 'melon': '멜론'}
```

```python
my_dict['apple']
#--> '사과'
```

```python
my_dict.get('apple') #--> '사과'
```

```python
my_dict.get('burger', '응 없어~')

#--> '응 없어~'
# 왜냐하면, burger라는 key는 없기 때문이다. 그래서 default인 '응 없어~' 가 출력된다.
```



- .pop( , default)

  : 딕셔너리 안에 해당 키 값이 있으면 제거하고, 그 뒤의 딕셔너리를 반환한다. 

  : default를 선언하고, 만약 키 값이 없으면 default가 나온다.

```python
my_dict = {'apple': '사과', 'banana': '바나나'}

my_dict.pop('berry', '없다')

#-->'없다'
```



- .update()

  : 이미 딕셔너리 내에 존재하는 key에 대해서 새로운 value를 덮어 씌운다.

```python
my_dict = {'apple': '사과', 'banana': '바나나', 'melon': '멜론'}
my_dict.update(apple='맛있어')

my_dict['apple']

#--> '맛있어'
```



- 딕셔너리에서의 반복문의 사용 

  : 기본적으로는 key를 출력한다.

```python
grades = {'john':  80, 'eric': 90, 'justin': 90}
for student in grades:
    print(student)
    
#--> john
#--> eric
#--> justin
```

​	: 이 때, value를 호출하고 싶으면 student가 아닌 grades[student] 를 출력하면 된다.

```python
grades = {'john':  80, 'eric': 90, 'justin': 90}
for student in grades:
    print(grades[student])
#--> 80    
#--> 90    
#--> 90    
```



- 실습1 - 딕셔너리 순회

```python
blood = {'A': 40, 'B': 11, 'AB': 4, 'O': 45}

for type in blood:
    print('{}형은 {}명입니다!'.format(type, blood[type]))
    
#--> A형은 40명입니다!
#--> B형은 11명입니다!
#--> AB형은 4명입니다!
#--> O형은 45명입니다!
```



- 딕셔너리에 추가하기

```python
grades = {'john':  80, 'eric': 90, 'justin': 90}

grades['julie'] = 70

print(grades)

#-->{'john': 80, 'eric': 90, 'justin': 90, 'julie': 70}
```



- 실습2 - 딕셔너리 구축하기

```python
book_titles =  ['great', 'expectations', 'the', 'adventures', 'of', 'sherlock', 'holmes', 'the', 'great', 'gasby', 'hamlet', 'adventures', 'of', 'huckleberry', 'fin']
```

​	: book_titles 내의 title들을 세고, 이에 대한 딕셔너리를 만든다.