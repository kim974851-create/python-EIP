ict methods · PY
# ══════════════════════════════════════════════════
# 딕셔너리(Dictionary) 기초 ~ 심화
# ══════════════════════════════════════════════════
# 딕셔너리란?
#   { 키(key) : 값(value) } 형태로 데이터를 저장하는 자료구조
#   리스트는 순서(인덱스)로 접근,  딕셔너리는 키(이름)로 접근
#   키는 중복 불가 / 값은 중복 가능


# ──────────────────────────────────────────────────
# 1. 기본 접근 / 값 수정 / 새 키 추가
# ──────────────────────────────────────────────────
# dict[key]        : key에 해당하는 값을 읽음
# dict[key] = 값   : 이미 있는 key면 값을 덮어씀
#                    없는 key면 새로운 쌍을 추가함

info = {"name": "Kim", "age": 25}

print(info["name"])            # → Kim  (키 "name"의 값을 읽음)

info["age"] = info["age"] + 1  # "age" 키가 이미 있으므로 25 → 26 으로 덮어씀
info["city"] = "Seoul"         # "city" 키가 없으므로 새로 추가됨

print(info)
# → {'name': 'Kim', 'age': 26, 'city': 'Seoul'}

print()

# ──────────────────────────────────────────────────
# 2. get() — 안전한 값 읽기
# ──────────────────────────────────────────────────
# dict[key]        : 키가 없으면 KeyError(오류) 발생 ← 위험
# dict.get(key)    : 키가 없으면 None 반환           ← 안전
# dict.get(key, X) : 키가 없으면 X 반환              ← 기본값 지정

settings = {"theme": "dark", "volume": 70}

v1 = settings.get("volume")          # "volume" 키 있음 → 70
v2 = settings.get("brightness")      # "brightness" 키 없음 → None
v3 = settings.get("brightness", 50)  # "brightness" 키 없음 → 기본값 50

print(v1, v2, v3)   # → 70 None 50

print()

# ──────────────────────────────────────────────────
# 3. keys() — 키 목록 / in 으로 존재 확인
# ──────────────────────────────────────────────────
# dict.keys()      : 딕셔너리의 모든 키를 모아서 반환
# "x" in dict.keys() : "x"라는 키가 존재하면 True
# ※ "x" in dict  처럼 keys() 없이 써도 동일하게 동작함

product = {"id": 101, "name": "Mouse", "price": 15000}

print("price" in product.keys())   # → True  ("price" 키 있음)
print("stock" in product.keys())   # → False ("stock" 키 없음)

print()

# ──────────────────────────────────────────────────
# 4. values() — 값만 꺼내서 순회
# ──────────────────────────────────────────────────
# dict.values() : 딕셔너리의 모든 값을 모아서 반환
# 키는 필요 없고 값만 필요할 때 사용

scores = {"kor": 80, "eng": 75, "math": 90}

total = 0
for s in scores.values():  # s 에 80, 75, 90 순서로 들어옴
    total += s             # 80 → 155 → 245
print(total)               # → 245

print()

# ──────────────────────────────────────────────────
# 5. items() — 키·값 쌍을 동시에 순회
# ──────────────────────────────────────────────────
# dict.items() : (키, 값) 튜플 쌍을 하나씩 반환
# for name, score in dict.items() 처럼 두 변수로 동시에 받을 수 있음
# ← 키만 필요하면 keys(), 값만 필요하면 values(), 둘 다 필요하면 items()

scores = {"kim": 85, "Lee": 92, "Park": 76, "Choi": 95}

high = []
for name, score in scores.items():  # (키, 값) 쌍을 순서대로 꺼냄
    if score >= 90:                  # 90점 이상인 경우만
        high.append(name)            # 이름(키)을 리스트에 추가
print(high)   # → ['Lee', 'Choi']

print()

# ──────────────────────────────────────────────────
# 6. update() — 다른 딕셔너리로 일괄 업데이트
# ──────────────────────────────────────────────────
# base.update(extra) 동작 규칙:
#   extra의 키가 base에 이미 있으면 → 값을 덮어씀
#   extra의 키가 base에 없으면     → 새로 추가함

base  = {"a": 1, "b": 2}
extra = {"b": 5, "c": 10}

base.update(extra)
#   "b": 2 → 5  로 덮어써짐  (base와 extra 둘 다 "b" 보유)
#   "c": 10     새로 추가됨   (base에 "c" 없었음)

print(base)   # → {'a': 1, 'b': 5, 'c': 10}

print()

# ──────────────────────────────────────────────────
# 7. 두 리스트를 딕셔너리로 합치기
# ──────────────────────────────────────────────────
# 같은 인덱스끼리 짝지어 { 이름 : 점수 } 딕셔너리를 만드는 패턴
# range(len(names)) → 0, 1, 2  (인덱스 번호를 순서대로 생성)

names  = ["Kim", "Lee", "Park"]
points = [100, 85, 90]

result = {}
for i in range(len(names)):
    result[names[i]] = points[i]
    # i=0 : result["Kim"]  = 100
    # i=1 : result["Lee"]  = 85
    # i=2 : result["Park"] = 90

print(result)   # → {'Kim': 100, 'Lee': 85, 'Park': 90}

print()

# ──────────────────────────────────────────────────
# 8. get()으로 빈도 세기 (등장 횟수 카운트)
# ──────────────────────────────────────────────────
# 핵심 공식:  count[item] = count.get(item, 0) + 1
#
#   처음 등장하는 단어  → count.get(item, 0) 이 0 반환 → 0 + 1 = 1
#   이미 있는 단어     → count.get(item, 0) 이 기존 값 반환 → 기존값 + 1
#
# 예시 (item = "apple"):
#   1회차 : count.get("apple", 0) → 0  → count["apple"] = 1
#   2회차 : count.get("apple", 0) → 1  → count["apple"] = 2
#   3회차 : count.get("apple", 0) → 2  → count["apple"] = 3

data = ["apple", "banana", "apple", "orange", "banana", "apple"]
count = {}
for item in data:
    count[item] = count.get(item, 0) + 1

print(count)   # → {'apple': 3, 'banana': 2, 'orange': 1}

print()

# ──────────────────────────────────────────────────
# 9. 중첩 딕셔너리 — 딕셔너리 안에 딕셔너리
# ──────────────────────────────────────────────────
# 구조:  { 학번 : { "name": 이름, "score": 점수 } }
#
# students["S1"]            → {"name": "Kim", "score": 82}
# students["S1"]["name"]    → "Kim"
# students["S1"]["score"]   → 82
#
# items()로 꺼내면:
#   sid  = "S1",  info = {"name": "Kim", "score": 82}
#   sid  = "S2",  info = {"name": "Lee", "score": 91}  ...
#
# info["score"] 로 안쪽 딕셔너리의 값에 다시 접근

students = {
    "S1": {"name": "Kim",  "score": 82},
    "S2": {"name": "Lee",  "score": 91},
    "S3": {"name": "Park", "score": 77},
    "S4": {"name": "Choi", "score": 95},
}

passed = []
for sid, info in students.items():   # sid=학번, info=내부 딕셔너리
    if info["score"] >= 90:          # 안쪽 딕셔너리의 "score" 값 접근
        passed.append(info["name"])  # 90점 이상이면 이름 수집

print(passed)   # → ['Lee', 'Choi']
