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