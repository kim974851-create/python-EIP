numbers = [1, 2, 3, 4]
result = [n * 2 for n in numbers]
print(result)

print()


nums = list(range(1, 11))
list = [n for n in nums if n % 3 == 0]
print(list)

print()

numbers = [1, 2, 3, 4, 5]
labels = ["e" if n % 2 == 0 else "o" for n in numbers]
print(labels)

print()

text = "Python Programming"

# text를 한 글자씩 순회하면서
# ch.lower()로 소문자 변환 후 모음(aeiou)에 포함되면 추가
view = [ch for ch in text if ch.lower() in "aeiou"]

print(view)  # ['o', 'o', 'a', 'i'] 출력


# P → 모음 아님 ❌
# y → 모음 아님 ❌
# t → 모음 아님 ❌
# h → 모음 아님 ❌
# o → 모음 ✅ → 추가
# n → 모음 아님 ❌
# → 공백 ❌
# P → 모음 아님 ❌
# r → 모음 아님 ❌
# o → 모음 ✅ → 추가
# g → 모음 아님 ❌
# r → 모음 아님 ❌
# a → 모음 ✅ → 추가
# m → 모음 아님 ❌
# m → 모음 아님 ❌
# i → 모음 ✅ → 추가
# n → 모음 아님 ❌
# g → 모음 아님 ❌
#
# 결과 → ['o', 'o', 'a', 'i']

print()

matrix = [ [1, 2, 3], [4, 5, 6] ]

# matrix의 각 row를 순회하고
# row 안의 각 숫자 n을 순회하면서
# n % 2 == 0 → 짝수만 추가
evens = [n for row in matrix for n in row if n % 2 == 0]

print(evens)  # [2, 4, 6] 출력

nums = [3, 5, 7, 9]

# nums의 각 n을 순회하면서
# n**2 (제곱) 계산 후 50 이상이면 추가
overs = [n**2 for n in nums if n**2 >= 50]

print(overs)  # [81] 출력

# n = 3 → 3**2 = 9  → 9 >= 50 ❌
# n = 5 → 5**2 = 25 → 25 >= 50 ❌
# n = 7 → 7**2 = 49 → 49 >= 50 ❌
# n = 9 → 9**2 = 81 → 81 >= 50 ✅ → 추가
#
# 결과 → [81]
print()

numbers = [1, 2, 2, 3, 4, 4, 5, 6]

# { } → 집합(set) 컴프리헨션 → 중복 자동 제거!
# 짝수(n % 2 == 0)인 n만 골라서 *2 후 set에 추가
result = {n * 2 for n in numbers if n % 2 == 0}

print(result)  # {4, 8, 12} 출력

print()

# n = 1 → 홀수 ❌
# n = 2 → 짝수 ✅ → 2*2 = 4  추가
# n = 2 → 짝수 ✅ → 2*2 = 4  중복 → 제거!
# n = 3 → 홀수 ❌
# n = 4 → 짝수 ✅ → 4*2 = 8  추가
# n = 4 → 짝수 ✅ → 4*2 = 8  중복 → 제거!
# n = 5 → 홀수 ❌
# n = 6 → 짝수 ✅ → 6*2 = 12 추가

scores = {"Kim": 85, "Lee": 92, "Park": 58, "Choi": 77}

# { key: value } → 딕셔너리 컴프리헨션
# scores.items() → (name, score) 쌍으로 순회
# score >= 80 인 경우만 새 딕셔너리에 추가
passed = {name: score for name, score in scores.items() if score >= 80}

print(passed)  # {'Kim': 85, 'Lee': 92} 출력

print()

nums = [1, 2, 3, 4, 5]

# tuple() 안에 제너레이터 표현식 사용
# 홀수(n % 2 == 1)인 n만 골라서 **2 후 tuple로 변환
result = tuple(n**2 for n in nums if n % 2 == 1)

print(result)  # (1, 9, 25) 출력

