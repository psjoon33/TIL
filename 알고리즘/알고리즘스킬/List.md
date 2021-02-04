# List

: 변경 가능하고, 순서가 있고, 순회가 가능하다.

: mutable, sequence, iterable



- .append(x)

  :리스트에 x를 추가한다.



- .extend(iterable)

  : . 앞에 리스트가 온다.

  : 리스트에 iterable한 container를 이어 붙힌다.

  : 이 때 기존의 리스트에 iterable한 컨테이너의 요소 하나하나를 추가하여 리스트로 반환한다.

```python
let = ['a', 'b', 'c', 'd']
let.extend(['a', 'b', 'c'])
print(let)

#-->['a', 'b', 'c', 'd', 'a', 'b', 'c']
```

​	: .sort()와 마찬가지로 기존의 값 자체를 아예 바꿔버린다. 

```python
a = ['a', 'b', 'c', 'd']
a.extend((1, 2, 3))
print(a)

#-->['a', 'b', 'c', 'd', 1, 2, 3]
```

```
['a', 'b', 'c', 'd', 1, 2, 3]
```

**여기서 사실, .extend(iterable)은 += 랑 똑같은 기능을 한다.**

```python
a = ['a', 'b', 'c', 'd']
a += (1, 2, 3)
print(a)

#--> ['a', 'b', 'c', 'd', 1, 2, 3]
```



- .insert(i, x)

  : 리스트의 i 번째 위치에 x를 추가한다.

```python
a = [0]*5
a.insert(3, 5)
print(a)

#--> [0, 0, 0, 5, 0, 0]
```



- .remove(x)

  :앞의 리스트에서 x를 찾아 삭제한다. 가장 앞에 있는 1개만.

  : 없으면 Error



- .sort()

  : 정렬을 한다. (오름차순으로)

  : sorted() 랑 주의해서 사용할 것.



- .reverse()

  : 기존의 순서를 뒤집는다.

  #--> 그렇다면,   .sort()와 .reverse()를 함께 사용함으로써 내림차순을 만들 수 도 있다.



- List Comprehension

  : 표현식과 제어문을 통해 리스트를 생성한다.

  : 기존에 여러줄이 필요했던 코드를 한 줄로 축약 할 수 있다.

```python
# 1~10 까지의 수들의 세제곱으로 이루어진 리스트

cubic_number = [i**3 for i in range(1, 11)]

print(cubic_number)

#-->[1, 8, 27, 64, 125, 216, 343, 512, 729, 1000]
```



​	: 여기서 for만 쓰는게 아니라, for에다가 if도 추가해서 사용할 수 있다.

```python
# 10 이하의 짝수의 제곱으로 이루어진 리스트

nums = [i**2 for i in range(1, 11) if i % 2 ==0]

print(nums)

#-->[4, 16, 36, 64, 100]
```



- 실습1 - 곱집합

  :두 리스트의 가능한 모든 조합을 담은 pair 리스트를 작성하시오

  ```python
  girls = ['jane', 'ashley', 'mary']
  boys = ['justin', 'eric', 'david']
  ```

  ```python
  #모든 girl, boy 의 pair를 만들어보자
  
  p = [(girl, boy) for girl in girls for boy in boys]
  print(p)
  
  #-- > [('jane', 'justin'), ('jane', 'eric'), ('jane', 'david'), ('ashley', 'justin'), ('ashley', 'eric'), ('ashley', 'david'), ('mary', 'justin'), ('mary', 'eric'), ('mary', 'david')]
  ```

  

- 실습2 - 피타고라스의 정리

  : x<y<z<=50을 만족하는 모든 피타고라스 해를 찾으시오

```python
pyta = [(x, y, z) for x in range(1, 49) for y in range(x+1, 50) for z in range(y+1, 51) if x**2+y**2 == z**2]

print(pyta)

#-->[(3, 4, 5), (5, 12, 13), (6, 8, 10), (7, 24, 25), (8, 15, 17), (9, 12, 15), (9, 40, 41), (10, 24, 26), (12, 16, 20), (12, 35, 37), (14, 48, 50), (15, 20, 25), (15, 36, 39), (16, 30, 34), (18, 24, 30), (20, 21, 29), (21, 28, 35), (24, 32, 40), (27, 36, 45), (30, 40, 50)]
```





