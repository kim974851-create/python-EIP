# ──────────────────────────────────────────────
# 1. 기본 함수 - 두 수를 더한 뒤 2배 반환
# ──────────────────────────────────────────────
def add(a, b):
    result = a + b
    return result * 2  # ⚠️ 주의: 더한 값을 2배로 반환함 (단순 덧셈 아님)

x = add(3, 5)   # 3+5=8, 8*2=16
print(x)        # 출력: 16

print()

# ──────────────────────────────────────────────
# 2. 별 출력 함수 - n개의 *를 한 줄에 출력
# ──────────────────────────────────────────────
def print_stars(n):          # ✅ 오타 수정: print_starts → print_stars
    print("*" * n)

print_stars(3)   # 출력: ***
print_stars(5)   # 출력: *****

print()

# ──────────────────────────────────────────────
# 3. 거듭제곱 함수 - 기본값(default) 매개변수 사용
# ──────────────────────────────────────────────
def power(base, exp=2):      # exp를 생략하면 자동으로 제곱(2승)
    return base ** exp

print(power(3))     # 3² = 9
print(power(2, 5))  # 2⁵ = 32

print()

# ──────────────────────────────────────────────
# 4. 인사 함수 - 기본값 매개변수 + 조건 분기
# ──────────────────────────────────────────────
def greet(name="Guest", lang="ko"):
    if lang == "ko":
        print(f"안녕, {name}")
    else:
        print(f"Hello, {name}")

greet()              # name="Guest", lang="ko" → 안녕, Guest
greet("Kim")         # name="Kim",   lang="ko" → 안녕, Kim
greet("John", "en")  # name="John",  lang="en" → Hello, John

print()

# ──────────────────────────────────────────────
# 5. 가변 인수(*args) - 전달된 숫자 중 최댓값 반환
# ──────────────────────────────────────────────
def max_value(*args):   # *args : 인수를 튜플로 수집
    return max(args)

print(max_value(3, 8, 1, 6))    # 출력: 8
print(max_value(-5, -2, -10))   # 출력: -2

print()

# ──────────────────────────────────────────────
# 6. 태그 + 가변 메시지 출력
#    첫 번째 인수는 태그, 나머지는 *msgs로 수집
# ──────────────────────────────────────────────
def tag_message(tag, *msgs):
    for m in msgs:
        print(f"[{tag}] {m}")

tag_message("INFO", "start", "processing", "done")
# 출력:
# [INFO] start
# [INFO] processing
# [INFO] done

print()

# ──────────────────────────────────────────────
# 7. 함수 합성 - add()를 내부에서 호출
#    ⚠️ 주의: 위에서 정의한 add()는 (a+b)*2를 반환함
# ──────────────────────────────────────────────
# add()가 두 번 정의됐지만 Python은 마지막 정의를 사용
# 여기서 add()를 단순 덧셈으로 재정의
def add(a, b):
    return a + b  # ✅ 이번엔 그냥 덧셈만

def calc(a, b, c):
    temp = add(a, b)   # add(2, 3) = 5
    return temp * c    # 5 * 4 = 20

print(calc(2, 3, 4))   # 출력: 20

print()

# ──────────────────────────────────────────────
# 8. 다중 반환값 - 최솟값, 최댓값, 합계를 튜플로 반환
# ──────────────────────────────────────────────
def min_max_sum(*nums):
    return min(nums), max(nums), sum(nums)  # 튜플로 묶어서 반환

a = min_max_sum(3, 1, 5, 2)
print(a)  # 출력: (1, 5, 11)

print()

# ──────────────────────────────────────────────
# 9. 짝수 필터 함수
#    ✅ 버그 수정 2곳:
#      (1) 함수명 오타: find_even_or_masg → find_even_or_msg
#      (2) 들여쓰기 버그: if evens 체크가 for 루프 안에 있어서
#          첫 번째 요소 처리 후 바로 반환 → for 바깥으로 이동
# ──────────────────────────────────────────────
def find_even_or_msg(*nums):
    evens = []
    for n in nums:
        if n % 2 == 0:
            evens.append(n)   # 짝수만 리스트에 추가
    # 루프가 끝난 뒤 결과 판단 (들여쓰기 수정!)
    if evens:
        return evens          # 짝수가 하나라도 있으면 리스트 반환
    else:
        return "No Data."     # 짝수가 없으면 문자열 반환

result1 = find_even_or_msg(1, 3, 5, 7)   # 짝수 없음
result2 = find_even_or_msg(2, 4, 5, 7)   # 짝수: 2, 4

print(result1)  # 출력: No Data.
print(result2)  # 출력: [2, 4]
