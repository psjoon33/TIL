# String

특징 : immutable, ordered, iterable



- .find(x)

  : x의 첫번째 위치를 반환. 없으면 -1

  

- .index(x)

  :x의 첫번째 위치를 반환. 없으면 Error



- .replace(old, new, [count])

  : string 내에서 old 문자를 new 문자로 count 만큼 변환한다.

  ```python
  letter = 'abababab'
  letter.replace('a', 'b', 2)
  #-->'bbbbabab'
  ```

  

- .strip([chars])    (.lstrip이나 .rstrip으로 쓰이기도 한다.)

  : chars(문자)를 지정하면 양쪽을 제거하거나, 왼쪽, 오른쪽만 제거할 수도 있다.

  : 만약 .strip([chars])를 했을 때, chars가 양쪽 끝에 있다면, 제거하는 것이다.

  : 이 때 주의할 점은 한 번 제거했는데도, 끝에 chars가 그대로 있으면 또 제거한다.

  ```python
  'hiehehihihihihi'.stripo('hi')
  
  #--> 'ehe'
  ```



- .split() : () 안의 값을 기준으로 나누어서, **'리스트'**로 반환한다.

```python
'a_b_c_d'.split('_')

#--> ['a', 'b', 'c', 'd']
```

만약 나누는 기준의 값이 끝에 있으면 리스트의 마지막에 '' 가 들어간다.

```python
'a_b_c_'.split('')

#--> ['a', 'b', 'c', '']
```

split()은 언제 많이 쓰냐면 주로 알고리즘을 풀 때 맨처음 인풋을 받을 때 많이 쓴다.



- 'separator'.join(iterable)

  : string 뿐만 아니라 모든 iterable한 container에 대해서 쓸 수 있다.

  : iterable한 container의 각각의 요소에 대해 'separator'를 추가해서, String으로 반환한다.

```python
word = '배고파'
'!'.split(words)
#--> '배!고!파'
```

```python
nums = ['1', '2', '3', '4', '5']
' '.join(nums)
#-->'1 2 3 4 5'
```

​	: 이 스킬 역시, 알고리즘의 문제를 풀 때 마지막에 출력할 때 많이 사용하는 기술이다.



- 문자 변형

  (1) .capitalize()

  : 앞글자를 대문자로 만들고 나머지는 모두 소문자로 만들어 반환한다.

  : 이 때 주의할 점은, ' '안의 제일 첫 문자만 대문자로 만든다는 것이다.

  ```python
  a = 'hi, Everyone. Nice to meet U'
  a.capitalize()
  
  #--> 'Hi, everyone. nice to meet u'
  ```

  : 또한, ' ' 안의 제일 앞 문자가 알파벳이 아니라 예를 들어 숫자면, 그 뒤 모든 알파벳을 소문자로 만든다.

  ```python
  b = '00ABC'
  b.capitalize()
  
  #--> '00abc'
  ```

  

  (2) .title()

  : 맨 처음과 어퍼스트로피나 문자열, 그리고 공백 이후를 대문자로 만들어 반환한다.

  ```python
  a = 'hi, i\'m sungjun park. nice to meet you.'
  a. title()
  
  #--> 'Hi, I\'M Sungjun Park. Nice To Meet You'
  # 여기서 ''안에 어퍼스트로피를 쓸 경우에는 어퍼스트로피 앞에 \를 추가한다.
  ```

  (3) .upper()

  : 간단하게 모두를 대문자로 만듦.

  ```python
  'abcdefg'.upper()
  #-->'ABCDEFG'
  ```

  (4) .lower()

  : 간단하게 모두를 소문자로 만든다.

  ```python
  'ABCDEFG'.lower()
  #-->'abcdefg'
  ```

  

  (5) .swapcase()

  : swap이라는 말 그대로, 소문자는 대문자로, 대문자는 소문자로 바꾼다.

  : 깨알 상식. 대문자 = upper case / 소문자 = lower case

  ```python
  a = 'abCDefGH'
  a.swapcase()
  #--> 'ABcdEFgh'
  ```

  

  