중복 코드가 많이 섞여있네요, 정리해드릴게요!

```python
x = 8
if x > 10:
    print("A")
elif x > 5:      # 8 > 5 해당
    print("B")   # B 출력
else:
    print("C")


x = 5
if x >= 5:       # True → A 출력
    print("A")
if x > 5:        # False → else로
    print("B")
else:
    print("C")   # C 출력


x = 3
y = 7
# 삼항 연산자 : 조건이 True면 앞, False면 뒤
result = "X" if x > y else "Y"  # 3 > 7 False → "Y"
print(result)


x = 2
# match : 값에 따라 분기 (switch문과 유사)
match x:
    case 1:
        print("하나")
    case 2:
        print("둘")   # 2 해당
    case 3:
        print("셋")
    case _:           # 나머지 (default)
        print("기타")

print()

# range(1, 5) : 1~4 출력, end=" " : 줄바꿈 대신 공백
for i in range(1, 5):
    print(i, end=" ")  # 1 2 3 4

print()  # 줄바꿈

for i in range(5):
    if i == 3:
        break          # 3 되면 반복 종료
    print(i)           # 0 1 2

print()

# while : 조건이 True인 동안 반복
x = 3
while x > 0:
    print(x)
    x -= 1             # x = x - 1

print()

value = 7
if value < 0:
    print("음수")
else:
    # match 중첩 : 나머지 값에 따라 분기
    match value % 3:
        case 0:
            print("3의 배수")
        case 1:
            print("나머지 1")  # 7 % 3 = 1 해당
        case _:
            print("나머지 2")

print()

total = 0
for i in range(1, 10):
    if i % 2 == 0:
        continue       # 짝수 건너뜀
    if i > 7:
        break          # 7 초과시 종료
    total += i         # 홀수만 합산 (1+3+5+7)
print(total)           # 16

print()

# while else : break 없이 정상 종료시 else 실행
n = 1
while n <= 5:
    print("n =", n)
    if n == 10:        # 조건 미충족 → break 안됨
        break
    n += 1
else:
    print("End")       # 정상 종료 → else 실행


