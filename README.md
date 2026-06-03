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
01 파이썬 기본

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

