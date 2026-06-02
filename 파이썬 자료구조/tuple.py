t = (5, 3, 5, 7, 5)
# count() : 해당 값이 몇 번 등장하는지 반환
# index() : 해당 값의 첫 번째 인덱스 반환
print(t.count(7))  # 출력: 1
print(t.index(7))  # 출력: 3

print()

data = (10, 20, 30)
# 튜플 언패킹 : 순서대로 각 변수에 값 할당
a, b, c = data
total = a + b + c
print(a, b, c, total)  # 출력: 10 20 30 60

print()

t = (1, 2, 3)
# 튜플은 수정 불가 → 리스트로 변환 후 수정 → 다시 튜플로 변환
temp = list(t)
temp[1] = 99
t = tuple(temp)
print(t)  # 출력: (1, 99, 3)

print()

nums = (10, 20, 30, 40, 50)
# nums[0] : 첫 번째 요소, nums[-1] : 마지막 요소
print(nums[0], nums[-1])   # 출력: 10 50
# [1:4] : 인덱스 1~3 슬라이싱
print(nums[1:4])           # 출력: (20, 30, 40)
# [-4:-1] : 뒤에서 4번째 ~ 뒤에서 2번째 슬라이싱
print(nums[-4:-1])         # 출력: (20, 30, 40)

print()

scores = (90, 75, 88, 92)
# max()로 최댓값 찾고 index()로 그 위치 반환
high_idx = scores.index(max(scores))
print(high_idx, scores[high_idx])  # 출력: 3 92

print()

t = (("Kim", 20)), ("Lee", 25), ("Park", 23)
# for문으로 (이름, 나이) 언패킹, 나이 23 이상만 출력
for name, age in t:
    if age >= 23:
        print(name, age)
# 출력:
# Lee 25
# Park 23

print()

t = (1, 2, 3, 4, 5, 6)
# x % 2 == 0 : 짝수인 요소 개수 카운트
even_count = 0
for x in t:
    if x % 2 == 0:
        even_count += 1
print(even_count)  # 출력: 3

print()

t = ("apple", "banana", "apple", "cherry", "banana", "apple")
# count() : "apple" 등장 횟수, index() : "banana" 첫 번째 인덱스
print(t.count("apple"), t.index("banana"))  # 출력: 3 1

print()

# (42) : 괄호일 뿐 튜플 아님 → 정수로 인식
t1 = (42)
print(t1)   # 출력: 42
# (42,) : 쉼표가 있어야 튜플로 인식
t2 = (42,)
print(t2)   # 출력: (42,)

print()

a = 10
b = 20
# 튜플 스왑 : 임시 변수 없이 두 값을 교환
a, b = b, a
print(a, b)  # 출력: 20 10
