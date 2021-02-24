# [Python] argparse의 사용법 (파이썬 인자값 추가하기)

참조 : https://brownbears.tistory.com/413



### ArgumentParser()

이 객체에는 다음과 같은 것들을 입력받을 수 있다.

1. description

   : 인자 도움말 전에 표시할 텍스트 (기본값 : none)

   : 스크립트에 -h 옵션을 주어 실행 시, usage 아래에 노출

   : 아래의 예시에서 사용..

.....



### add_argument()

이 메서드는 아래와 같은 것들을 입력받는다.

1. default

   : 인자가 명령행에 없는 경우 생성되는 값.

2. type

   : 명령행 인자가 변환되어야 할 형

3. required 

   : 명령행 옵션을 생략 할 수 있는지 아닌지

4. help

   : 인자가 하는 일에 대한 간단한 설명

.... 

그 외에 입력받는 것들은, 참조링크를 활용하면 된다.



-----------

### 사용법

```python
# 파일이름 use.py

# 사용하려면 import 해 줌
import argparse

# 인자값을 받을 수 있는 인스턴스 생성
parser = argparse.ArgumentParser(description='사용법테스트입니다')

# 입력받을 인자값 등록(add_argument)
parser.add_argument('--target', required=True, help='어느 것을 요구하냐')
parser.add_argument('--env', required=False, default='dev', help='실행환경은 뭐냐')

# 입력받은 인자값을 args에 저장
args = parser.parse_args()

# 입력받은 인자값 출력
print(args.target)
print(args)


```

**인자값을 안 주면**

```python
# 위의 상태에서 인자값을 안주고 실행을 시키면, 
$ python use.py
# 를 하면 에러가 뜬다,,,,

# 그래서 일단 스크립트에 -h 옵션을 주고 실행해 보면
$ python use.py -h
# 를 해보면, 다음과 같다.

usage: use.py [-h] --target TARGET [--env ENV]     #required가 True이면 []가 없고, False이면 []가 있다.

사용법 테스트입니다    #description에 해당하는 부분이 나타난다.

optional arguments:    # 어떤 인자값이 입력받아야 하는지 나타난다.
  -h, --help       show this help message and exit
  --target TARGET  어느 것을 요구하냐
  --env ENV        실행환경은 뭐냐
```

**인자값을 주면**

```python
# 다음과 같이 terminal에 실행하면
$ python use.py --target=테스트 --env=local

# 아래와 같이 나타난다.
테스트
local

# 그리고 required=False인, --env에는 아무것도 주지 않으면
$ python use.py --target=테스트

#아래와 같이 나타난다.
테스트
dev

```

당연히 target 에 아무런 입력값도 주지 않으면 error



또 참조해야할 사이트 : https://greeksharifa.github.io/references/2019/02/12/argparse-usage/#argument-%EC%9D%B4%EB%A6%84-%EC%A0%95%EC%9D%98































