# python-EIP
정보처리기사-파이썬
## 오늘 진행한 과정

**1. GitHub 레포 생성**
- `python-EIP` 레포 만들기 (README 포함)

**2. IntelliJ 터미널에서 Git 초기화**
```bash
git init
git branch -m main
```

**3. GitHub 레포 연결**
```bash
git remote add origin https://github.com/kim974851-create/python-EIP.git
```

**4. 첫 커밋**
```bash
git add .
git commit -m "06.01 첫 커밋"
```

**5. 충돌 해결 후 푸시**
```bash
git pull origin main --allow-unrelated-histories --no-rebase
git push -u origin main
```

---

## 앞으로는 이것만!
```bash
git add .
git commit -m "날짜 + 내용"
git push
```

---
# 01 파이썬 기본

## 1. 산술 연산자
```python
a, b = 10, 3

print(a + b)   # 13  덧셈
print(a - b)   # 7   뺄셈
print(a * b)   # 30  곱셈
print(a / b)   # 3.333... 나눗셈 (실수)
print(a // b)  # 3   몫 (정수)
print(a % b)   # 1   나머지
print(a ** b)  # 1000 거듭제곱
```

---

## 2. 비교 연산자
```python
a, b = 10, 3

print(a == b)  # False  같다
print(a != b)  # True   다르다
print(a > b)   # True   크다
print(a < b)   # False  작다
print(a >= b)  # True   크거나 같다
print(a <= b)  # False  작거나 같다
```

---

## 3. 논리 연산자
```python
a, b = True, False

print(a and b)  # False  둘 다 True여야 True
print(a or b)   # True   하나라도 True면 True
print(not a)    # False  반전
```

---

## 4. 비트 연산자
```python
a, b = 5, 3
# 5 = 0101
# 3 = 0011

print(a & b)   # 1   AND  0101 & 0011 = 0001
print(a | b)   # 7   OR   0101 | 0011 = 0111
print(a ^ b)   # 6   XOR  0101 ^ 0011 = 0110
print(~a)      # -6  NOT  비트 반전
print(a << 1)  # 10  왼쪽 시프트 0101 → 1010
print(a >> 1)  # 2   오른쪽 시프트 0101 → 0010
```

---

## 5. 기타 연산자
```python
# 할당 연산자
a = 10
a += 3   # a = 13
a -= 3   # a = 10
a *= 3   # a = 30
a //= 3  # a = 10
a **= 2  # a = 100
a %= 3   # a = 1

# 멤버십 연산자
nums = [1, 2, 3]
print(1 in nums)      # True  포함되면 True
print(5 not in nums)  # True  포함 안되면 True

# 식별 연산자
a = [1, 2]
b = a
c = [1, 2]
print(a is b)   # True  같은 객체
print(a is c)   # False 값은 같지만 다른 객체
print(a == c)   # True  값이 같다
```

---


```
✅ 산술 연산자 (+ - * / // % **)
✅ 비교 연산자 (== != > < >= <=)
✅ 논리 연산자 (and or not)
✅ 비트 연산자 (& | ^ ~ << >>)
✅ 기타 연산자 (할당 / 멤버십 / 식별)
```
# 제어문 / 반복문 

## 1. 조건문 (if / elif / else)
```python
score = 85

if score >= 90:
    print("A")
elif score >= 80:   # 위 조건 False일 때
    print("B")      # 85 >= 80 → True → "B" 출력
elif score >= 70:
    print("C")
else:               # 모든 조건 False일 때
    print("F")
```

---

## 2. 삼항 연산자
```python
x = 10
result = "양수" if x > 0 else "음수"
print(result)  # 양수
```

---

## 3. for 문
```python
# 리스트 순회
nums = [1, 2, 3, 4, 5]
for n in nums:
    print(n)  # 1 2 3 4 5

# range 사용
for i in range(5):         # 0 1 2 3 4
    print(i)

for i in range(1, 6):      # 1 2 3 4 5
    print(i)

for i in range(0, 10, 2):  # 0 2 4 6 8 (2씩 증가)
    print(i)

# enumerate (인덱스 + 값)
fruits = ["apple", "banana", "cherry"]
for i, fruit in enumerate(fruits):
    print(i, fruit)
# 0 apple
# 1 banana
# 2 cherry

# zip (두 리스트 동시 순회)
names = ["Kim", "Lee", "Park"]
scores = [85, 92, 78]
for name, score in zip(names, scores):
    print(name, score)
# Kim 85
# Lee 92
# Park 78
```

---

## 4. while 문
```python
# 기본
cnt = 0
while cnt < 5:
    print(cnt)  # 0 1 2 3 4
    cnt += 1

# 무한루프 + break
while True:
    n = int(input("숫자 입력: "))
    if n == 0:
        break   # 0 입력하면 종료
    print(n)
```

---

## 5. break / continue / pass
```python
# break → 반복문 완전 종료
for i in range(10):
    if i == 5:
        break       # 5에서 멈춤
    print(i)        # 0 1 2 3 4

# continue → 해당 회차 건너뜀
for i in range(5):
    if i == 2:
        continue    # 2는 건너뜀
    print(i)        # 0 1 3 4

# pass → 아무것도 안 함 (자리만 채움)
for i in range(5):
    if i == 2:
        pass        # 그냥 넘어감
    print(i)        # 0 1 2 3 4
```

---

## 6. 중첩 반복문
```python
for i in range(2, 10):
    for j in range(1, 10):
        print(f"{i} x {j} = {i*j}")
```

---

## 7. for - else / while - else
```python
# break 없이 정상 종료되면 else 실행
for i in range(5):
    if i == 10:     # 조건 안 걸림
        break
else:
    print("정상 종료")  # 출력됨

for i in range(5):
    if i == 3:      # break 걸림
        break
else:
    print("정상 종료")  # 출력 안 됨
```

---

## 8. match 문 (Python 3.10+)
```python
# 기본 match
command = "go"

match command:
    case "go":
        print("이동")       # 출력됨
    case "stop":
        print("정지")
    case "back":
        print("후진")
    case _:                 # default (else 역할)
        print("알 수 없음")

# 여러 값 동시 매칭
status = 404

match status:
    case 200:
        print("OK")
    case 400 | 404:         # 400 또는 404
        print("클라이언트 오류")  # 출력됨
    case 500:
        print("서버 오류")
    case _:
        print("기타")

# 튜플 매칭
point = (0, 1)

match point:
    case (0, 0):
        print("원점")
    case (0, y):            # x=0, y는 아무 값
        print(f"y축: {y}")  # y축: 1 출력
    case (x, 0):
        print(f"x축: {x}")
    case (x, y):
        print(f"좌표: {x}, {y}")

# 조건 추가 (guard)
score = 85

match score:
    case n if n >= 90:      # n에 score 값이 들어옴
        print("A")
    case n if n >= 80:
        print("B")          # 출력됨
    case n if n >= 70:
        print("C")
    case _:
        print("F")
```

---

**if vs match 비교:**

| | if / elif | match |
|--|--|--|
| 범위 조건 | ✅ 자유롭게 | ⚠️ guard 필요 |
| 값 매칭 | 가능 | ✅ 더 깔끔 |
| 패턴 매칭 | ❌ | ✅ 튜플, 리스트 등 |
| Python 버전 | 전체 | 3.10 이상만 |

---


```
✅ 조건문 (if / elif / else)
✅ 삼항 연산자
✅ for문 (range / enumerate / zip)
✅ while문
✅ break / continue / pass
✅ 중첩 반복문
✅ for-else / while-else
✅ match문 (3.10+)
```
# 파이썬 문자열 처리

## 1. 문자열 생성
```python
# 작은따옴표
s1 = 'Hello'

# 큰따옴표
s2 = "Hello"

# 따옴표 혼용 (문자열 안에 따옴표 포함할 때)
s3 = "It's a pen"     # 작은따옴표 포함
s4 = 'He said "Hi"'  # 큰따옴표 포함

# 이스케이프 문자
s5 = "Hello\nWorld"   # \n → 줄바꿈
s6 = "Hello\tWorld"   # \t → 탭
s7 = "He said \"Hi\"" # \" → 큰따옴표 출력

print(s5)
# Hello
# World

print(s6)  # Hello	World

# 문자열 반복 / 연결
s = "Hi" + " " + "Python"  # Hi Python
s = "Ha" * 3               # HaHaHa
```

---

## 2. 여러 줄 문자열
```python
# 삼중 따옴표 (''' 또는 """)
s1 = """Hello
Python
World"""

print(s1)
# Hello
# Python
# World

s2 = '''첫째 줄
둘째 줄
셋째 줄'''

print(s2)
# 첫째 줄
# 둘째 줄
# 셋째 줄

# 줄바꿈 없이 여러 줄 작성 (\ 사용)
s3 = "Hello " \
     "Python " \
     "World"
print(s3)  # Hello Python World
```

---

## 3. 문자열 인덱싱과 슬라이싱
```python
s = "Python"
#    012345   (양수 인덱스)
#   -6-5-4-3-2-1  (음수 인덱스)

# 인덱싱
print(s[0])   # P  (첫 번째)
print(s[3])   # h
print(s[-1])  # n  (마지막)
print(s[-2])  # o

# 슬라이싱 → s[시작:끝:간격]
print(s[0:3])   # Pyt  (0,1,2 → 3 미포함)
print(s[2:])    # thon (2부터 끝까지)
print(s[:3])    # Pyt  (처음부터 3 미포함)
print(s[:])     # Python (전체)
print(s[::2])   # Pto  (2칸씩 건너뜀)
print(s[::-1])  # nohtyP (역순)

# 활용 예시
s = "Hello Python"
print(s[6:])    # Python
print(s[:5])    # Hello
print(s[-6:])   # Python (뒤에서 6번째부터)
```

---


```
✅ 문자열 생성 (따옴표 / 이스케이프 / 반복 / 연결)
✅ 여러 줄 문자열 (삼중따옴표 / 백슬래시)
✅ 인덱싱 (양수 / 음수)
✅ 슬라이싱 [시작:끝:간격]
```
