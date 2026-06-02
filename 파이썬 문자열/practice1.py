text = "   PyThOn  3  "

# .lower() : 소문자 변환
# .strip() : 양쪽 끝 공백 제거
# "." + ... + "." : 앞뒤에 점 추가
result = "." + text.lower().strip() + "."

# 출력: .python  3.  (중간 공백 2칸은 그대로 유지)
print(result)

print()

# capitalize() : 첫 글자만 대문자, 나머지는 소문자
print(text.capitalize())
# 출력: Python is fun

# title() : 각 단어의 첫 글자를 대문자로 변환
print(text.title())
# 출력: Python Is Fun

print()

s = "     hi    "

# len(s) : 원본 문자열의 전체 길이
# len(s.strip()) : 양쪽 공백 제거 후 길이
print(len(s), len(s.strip()))
# 출력: 11 2


text = "banana"

# find() : 찾는 문자열의 첫 번째 인덱스 반환, 없으면 -1
print(text.find("na"))
# 출력: 2

# index() : 찾는 문자의 첫 번째 인덱스 반환, 없으면 오류 발생
print(text.index("a"))
# 출력: 1

# find() : 찾는 문자열이 없으면 -1 반환 (오류 없음)
print(text.find("z"))
# 출력: -1

print()

url = "https://example.com/index.html"

# startswith() : 해당 문자열로 시작하면 True, 아니면 False
print(url.startswith("https"))
# 출력: True

# endswith() : 해당 문자열로 끝나면 True, 아니면 False
print(url.endswith(".html"))
# 출력: True

# ".htm"으로 끝나지 않으므로 False
print(url.endswith(".htm"))
# 출력: False

print()

# count(x) : 문자열 안에서 x가 몇 번 등장하는지 반환
# 겹치는 부분은 세지 않음 ("ss"가 연속으로 있어도 각각 별도로 셈)
text = "mississippi"
print(text.count("ss"))   # → 2  ("missssippi" 에서 ss가 2번)
print(text.count("i"))    # → 4  (i가 총 4번 등장)

print()


# replace(a, b) : 문자열 안의 a를 모두 b로 교체
# isdigit()     : 문자열이 숫자로만 이루어졌으면 True
# len()         : 문자열의 글자 수 반환
text = "010-1234-5678"
text = text.replace("-", "")  # → "01012345678"  (하이픈 제거)
print(text.isdigit())           # → True   (이제 숫자만 남음)
print(len(text))                # → 11    (총 11자리)

print()

# split(sep) : sep 기준으로 문자열을 잘라 리스트로 반환
# join(list) : 리스트 요소를 구분자로 이어 하나의 문자열로 반환
data = "red,green,blue"
colors = data.split(",")          # → ["red", "green", "blue"]
print(colors[0], colors[-1])     # → red blue  (첫 번째, 마지막 요소)
result = "-".join(colors)         # → "red-green-blue"
print(result)

print()

# isalnum() : 영문자 + 숫자로만 구성되면 True  (공백·특수문자 있으면 False)
# isalpha() : 영문자(또는 한글)로만 구성되면 True
# isdigit() : 숫자로만 구성되면 True
# ※ 공백(" ")은 세 메서드 모두 False
codes = ["ABC123", "12345", "Hello", " "]
for c in codes:
    print(c.isalnum(), c.isalpha(), c.isdigit())
# "ABC123" → True  False False  (문자+숫자 혼합 → alnum만 True)
# "12345"  → True  False True   (숫자만)
# "Hello"  → True  True  False  (문자만)
# " "      → False False False  (공백은 모두 False)

print()

# isspace() : 문자열이 공백 문자(\n, \t 포함)로만 이루어지면 True
# strip()   : 문자열 양쪽 끝의 공백을 제거한 문자열 반환
s1 = "  "
s2 = "   a   "
print(s1.isspace(), s2.isspace())  # → True False  (s2는 'a'가 있어서 False)
print(len(s2.strip()))              # → 1    (공백 제거 후 "a" 만 남아 길이 1)

print()

# split() 인자 없이 호출 : 연속 공백 무시하고 단어 단위로 분리
# list.count(x) : 리스트 안에서 x가 몇 번 등장하는지 반환
# x in list     : x가 리스트에 있으면 True
sentence = "python is fun and python is powerful"
words = sentence.split()       # → ["python","is","fun","and","python","is","powerful"]
print(len(words))              # → 7   (단어 7개)
print(words.count("python"))   # → 2   ("python" 2번 등장)
print("fun" in words)         # → True ("fun"이 리스트에 존재)
