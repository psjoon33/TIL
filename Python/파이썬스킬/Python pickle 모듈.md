# Python pickle 모듈

- 일반 텍스트를 파일로 저장할 때에는 파일 입출력을 이용한다.
- 하지만 리스트나, 클래스같은 텍스트가 아닌 자료형은 일반적인 파일 입출력 방법으로는 데이터를 저장하거나 불러올 수 없다.
- 그래서 python 에서는 이런 텍스트 이외의 자료형을 파일로 저장하기 위해 ```pickle``` 이라는 모듈을 제공한다.



```python
text = 'hello world'

with open('hello.txt', 'w') as f:
    f.write(text) 
    
# 를 하면, text를 담은 hello.txt라는 파일이 잘 생성된다.
# 하지만,,,,

li = ['a', 'b', 'c'] 
with open('li.txt', 'w') as f:
    f.write(li)
    
# 를 하면 에러가 난다.
```



### pickle 모듈을 활용하여 데이터 입력 및 로드

1. import pickle
2. pickle 모듈을 이용하면 원하는 데이터를 자료형의 변경없이 파일로 저장하여 그대로 로드할 수 있다.
3. pickle로 데이터를 저장하거나 불러올 때에는 파일을 바이트 형식으로 읽거나 써야한다. (wb, rb)
4. 모든 python 객체를 저장하고 읽을 수 있다.



**입력**

```python
import pickle
li = ['a', 'b', 'c']
st = 'd'
with open('li.txt', 'wb') as f:
    pickle.dump(li, f)
	pickle.dump(st, f)
    
# 라고 입력을 하면, li.txt 라는 파일이 저장된다. 이 파일은 단순하게 읽은수는 없고 pickle.load로 읽을 수 있다.
```



**로드**

```python
import pickle
with open('li.txt', 'rb') as f:
    data1 = pickle.load(f)    # 여기서 중요한 것은 단 한줄씩 읽는다는 것이다.
    data2 = pickle.load(f)
print(data1)      #--> ['a', 'b', 'c']
print(data2)      #--> 'd'

# 라고 출력이 된다.
```



### 응용

만약에 여러 데이터가 저장되어 있는 pickle 파일에 대해서 한 번에 로드하고 싶다면,,,,?!

```python
import pickle
with open('li.txt', 'rb') as f:
    data_set = []
    while True:
        try:
            data = pickle.load(f)
        except:
            break

for d in data_set:
    print(d)
    
# 를 입력하면
# ['a', 'b', 'c']
# 'd' 
# 가 출력이 된다.


```

