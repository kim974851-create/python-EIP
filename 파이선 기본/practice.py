a = 7
b = 3
# // : 정수 나눗셈(몫), % : 나머지, ** : 거듭제곱
print(a // b, a % b, a**b)  # 2 1 343

# / : 실수 나눗셈 (항상 float 반환)
print(10 / 4)   # 2.5

# 정수 * 실수 → 결과는 실수형
print(10 * 4.0) # 40.0


x = 5
y = 10
# 비교 연산자: < 미만, == 같다, != 다르다
print(x < y, x == y, x != y)  # True False True

# 비트 AND: 두 비트가 모두 1일 때만 1  (101 & 011 = 001)
print(5 & 3)  # 1

# 비트 OR: 두 비트 중 하나라도 1이면 1  (101 | 011 = 111)
print(5 | 3)  # 7

# 비트 XOR: 두 비트가 다를 때만 1      (101 ^ 011 = 110)
print(5 ^ 3)  # 6

# ~ : 비트 NOT → -(n+1)
print(~5)   # -6

# << : 왼쪽 시프트 → × 2^n
print(8 << 2)  # 32  (8 × 2² = 32)

# >> : 오른쪽 시프트 → ÷ 2^n
print(8 >> 1)  # 4   (8 ÷ 2¹ = 4)


s = "banana"
# in : 문자열 포함 여부 확인
print('a' in s, 'z' in s, 'na' in s)  # True False True


x = 7
# and : 둘 다 True여야 True
print(x > 5 and x < 10)   # True  (7>5 이고 7<10)

# or : 하나라도 True면 True
print(x == 7 or x == 10)  # True  (7==7 이므로)

# not : True/False 반전
print(not (x < 5))         # True  (7<5 는 False → 반전 → True)


a = 4
b = 9
# 복합 조건: 4²==16 (True) and 9//3==3 (True)
print(a ** 2 == 16 and b // 3 == 3)  # True

# % : 나머지, // : 몫
print(b % a, b // a)   # 1 2  (9÷4 = 몫2 나머지1)

# (4+9)*2 = 26, 26 != 20 → True
print((a + b) * 2 != 20)  # True




