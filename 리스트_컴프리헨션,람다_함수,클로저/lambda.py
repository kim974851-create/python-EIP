add = lambda x, y: x+ y
result = add(7, 5)
print(result)

print()

f =  lambda x: x ** 2
nums = [1, 2, 3, 4]
result = [f(n) for n in nums]
print(result)

print()

data = [("apple", 3), ("banana", 1), ("cherry", 2)]

# sorted(대상, key=lambda 매개변수: 반환값)
# x → 리스트의 각 튜플 하나씩 받음
# x[1] → 튜플의 1번 인덱스(숫자)를 기준으로 정렬
sorted_data = sorted(data, key=lambda x: x[1])

# ("apple", 3)  → x = ("apple", 3)  → x[1] = 3
# ("banana", 1) → x = ("banana", 1) → x[1] = 1
# ("cherry", 2) → x = ("cherry", 2) → x[1] = 2
# 오름차순 정렬 → 1 < 2 < 3
# 결과 → [('banana', 1), ('cherry', 2), ('apple', 3)]
print(sorted_data)

print()

words = ["python", "is", "fun", "awesome"]

# sorted(대상, key=lambda 매개변수: 반환값, reverse=True)
# w → 리스트의 각 단어 하나씩 받음
# len(w) → 단어의 길이를 기준으로 정렬
# reverse=True → 내림차순 (길이 긴 것부터)
s_words = sorted(words, key=lambda w: len(w), reverse=True)

# "python"  → len("python")  = 6
# "is"      → len("is")      = 2
# "fun"     → len("fun")     = 3
# "awesome" → len("awesome") = 7
# 내림차순 정렬 → 7 > 6 > 3 > 2
# 결과 → ['awesome', 'python', 'fun', 'is']
print(s_words)

print()

nums = [-3, -2, -1, 0, 1, 2, 3, 4]

# filter(조건함수, 대상)
# x → 리스트의 각 숫자 하나씩 받음
# x % 2 == 0 → 짝수
# x > 0 → 양수
# 둘 다 만족하는 것만 필터링 후 list로 변환
result = list(filter(lambda x: x % 2 == 0 and x > 0, nums))

# -3 → 홀수 ❌
# -2 → 짝수지만 음수 ❌
# -1 → 홀수 ❌
#  0 → 짝수지만 0 > 0 아님 ❌
#  1 → 홀수 ❌
#  2 → 짝수 ✅ 양수 ✅ → 추가
#  3 → 홀수 ❌
#  4 → 짝수 ✅ 양수 ✅ → 추가
# 결과 → [2, 4]
print(result)

print()

# 핵심:
#
# 설명
# filter()	조건에 맞는 것만 걸러냄
# map()	모든 요소에 함수 적용
# lambda	간단한 함수를 한 줄로 표현


# nums = [1, 2, 3]
#
# enumerate(nums) →
# (0, 1)   ← 인덱스0, 값1
# (1, 2)   ← 인덱스1, 값2
# (2, 3)   ← 인덱스2, 값3
# t = (0, 1) → t[0]=0, t[1]=1 → (0, 1**2) = (0, 1)
# t = (1, 2) → t[0]=1, t[1]=2 → (1, 2**2) = (1, 4)
# t = (2, 3) → t[0]=2, t[1]=3 → (2, 3**2) = (2, 9)

# map() 결과를 list로 변환
# → [(0, 1), (1, 4), (2, 9)]
nums = [1, 2, 3]

# enumerate(nums) → (인덱스, 값) 튜플로 변환
# t[0] → 인덱스, t[1] → 값
# t[1] ** 2 → 값을 제곱
# map() → 모든 요소에 lambda 적용
# list() → map 결과를 리스트로 변환
pairs = list(map(lambda t: (t[0], t[1] ** 2), enumerate(nums)))

# 결과 → [(0, 1), (1, 4), (2, 9)]
print(pairs)

print()

nums = [1, 2, 3, 4, 5]

# 안쪽부터 실행
# 1. filter → 홀수만 걸러냄 → [1, 3, 5]
# 2. map → 걸러진 값에 *2 적용 → [2, 6, 10]
# 3. list → map 결과를 리스트로 변환
result = list(map(lambda x: x * 2, filter(lambda x: x % 2 == 1, nums)))

# 결과 → [2, 6, 10]
print(result)

print()

names = ["Kim", "Choi", "Lee"]

# max(대상, key=lambda 매개변수: 반환값)
# n → 리스트의 각 이름 하나씩 받음
# len(n) → 이름의 길이를 기준으로 가장 큰 값 찾기
long = max(names, key=lambda n: len(n))

# "Kim"  → len("Kim")  = 3
# "Choi" → len("Choi") = 4  ← 가장 길다!
# "Lee"  → len("Lee")  = 3
# 결과 → "Choi"
print(long)

def make(n):
    # lambda를 반환 → 함수를 반환하는 함수 (클로저)
    return lambda x: x * n

# make(2) → lambda x: x * 2 저장
times2 = make(2)
# make(5) → lambda x: x * 5 저장
times5 = make(5)

# times2(10) → 10 * 2 = 20
# times5(3)  → 3  * 5 = 15
# 결과 → 20 15
print(times2(10), times5(3))

students = [
    {"name": "Kim",  "score": 80},
    {"name": "Lee",  "score": 95},
    {"name": "Park", "score": 70}
]

# max(대상, key=lambda 매개변수: 반환값)
# s → 딕셔너리 하나씩 받음
# s["score"] → score 값을 기준으로 가장 큰 값 찾기
top = max(students, key=lambda s: s["score"])

# {"name": "Kim",  "score": 80} → s["score"] = 80
# {"name": "Lee",  "score": 95} → s["score"] = 95 ← 가장 크다!
# {"name": "Park", "score": 70} → s["score"] = 70

# top = {"name": "Lee", "score": 95}
# top["name"]  → "Lee"
# top["score"] → 95
# 결과 → Lee 95
print(top["name"], top["score"])



]

