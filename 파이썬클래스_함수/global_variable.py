x = 10
def show():
    print(x)
show()
print(x)

print()

cnt = 0
def inc():
    global cnt
    cnt += 1
inc()
inc()
print(cnt)

print()

# 전역 value = 100
value = 100
#test() 내부 -> value = 50 -> 지역변수 -> print(value) -> 50 출력
def test():

    value = 50
    print(value)
 # 함수 종료 후 -> print(value) -> 전역 value = 100 출력
test()
print(value)

print()

#nums = [1, 2, 3] (전역 리스트)
nums = [1, 2, 3]
# add_item() -> nums.append(4) -> 리스트 객체의 '내용'을 수정하는 것이므로 -> global 선언 없이도 전역 리스트에 영향
def add_item():
    nums.append(4)
add_item()
#add_item() 호출 후 nums -> [1, 2, 3, 4] 출력
print(nums)
# ===== 1. 전역변수 읽기 =====
x = 10  # 전역변수 x = 10

def show():
    # 함수 내부에서 전역변수 x를 읽기만 함 → global 선언 불필요
    print(x)  # 10 출력

show()    # 10 출력
print(x)  # 10 출력 (전역변수 그대로)

print()


# ===== 2. global로 전역변수 수정 =====
cnt = 0  # 전역변수 cnt = 0

def inc():
    global cnt  # 전역변수 cnt를 직접 수정하겠다고 선언
    cnt += 1    # 전역 cnt에 +1

inc()  # cnt = 1
inc()  # cnt = 2
print(cnt)  # 2 출력

print()


# ===== 3. 지역변수 vs 전역변수 =====
value = 100  # 전역변수 value = 100

def test():
    value = 50   # 전역변수와 이름이 같지만 → 지역변수로 새로 생성
    print(value) # 지역변수 50 출력 (전역변수에 영향 없음)

test()        # 50 출력
print(value)  # 전역변수 그대로 100 출력

print()


# ===== 4. 리스트는 global 없이 내용 수정 가능 =====
nums = [1, 2, 3]  # 전역 리스트

def add_item():
    # 리스트 자체를 교체하는 게 아니라
    # 리스트 내부 내용을 수정 → global 선언 없이도 전역에 영향
    nums.append(4)

add_item()
print(nums)  # [1, 2, 3, 4] 출력

print()


# ===== 5. 리스트를 재할당하면 지역변수가 됨 =====
nums = [1, 2, 3]  # 전역 리스트

def reset():
    nums = [0, 0, 0]    # 새 리스트를 대입 → 지역변수 nums 생성 (전역과 별개)
    print("in:", nums)  # in: [0, 0, 0] 출력

reset()          # in: [0, 0, 0] 출력
print("out.", nums)  # 전역 nums 그대로 → out. [1, 2, 3] 출력

print()


# ===== 6. 여러 함수에서 같은 전역변수 수정 =====
total = 0  # 전역변수 total = 0

def add(x):
    global total
    total += x  # total에 더하기

def sub(x):
    global total
    total -= x  # total에 빼기

add(10)  # total = 10
sub(3)   # total = 7
add(5)   # total = 12
print(total)  # 12 출력

print()


# ===== 7. func1(지역) vs func2(전역) =====
x = 100  # 전역변수 x = 100

def func1():
    x = 50           # 지역변수 x = 50 (전역 x와 별개)
    print("func1:", x)  # func1: 50 출력

def func2():
    global x         # 전역변수 x를 직접 사용
    x = x + 10       # 전역 x = 100 + 10 = 110
    print("func2:", x)  # func2: 110 출력

func1()              # func1: 50 출력 (전역 x 그대로 100)
func2()              # func2: 110 출력 (전역 x가 110으로 바뀜)
print("global:", x)  # global: 110 출력

print()


# ===== 8. 함수 호출 횟수 카운트 =====
count = 0  # 전역변수 count = 0

def process(data):
    global count
    print("prc:", data)  # 전달받은 data 출력
    count += 1           # 호출될 때마다 count +1

process("A")  # prc: A, count = 1
process("B")  # prc: B, count = 2
process("C")  # prc: C, count = 3
print("total:", count)  # total: 3 출력

print()
import copy

# 원본 리스트 생성 (숫자, 내부 리스트, 숫자로 구성)
a = [10, [1, 2], 20]

# ===== 얕은 복사 =====
# a.copy() → 바깥 리스트는 새로 만들지만
# 내부 리스트 [1, 2]는 주소값만 복사 → a와 b가 같은 [1,2]를 공유
b = a.copy()

# ===== 깊은 복사 =====
# deepcopy(a) → 바깥 + 내부 리스트까지 전부 새로 만듦
# a와 c는 완전히 독립
c = copy.deepcopy(a)

# b[1]은 a[1]과 같은 리스트를 가리키므로
# b[1][0] = 99 → a[1][0]도 99로 바뀜 ← a가 바뀌는 이유!
b[1][0] = 99

# b[2]는 숫자(int) → 독립적으로 복사됨
# b[2] = 200 으로 바꿔도 a[2]는 그대로 20
b[2] = 200

# c[1]은 deepcopy로 새로 만든 리스트 → a[1]과 완전히 독립
# c[1][1] = 77 로 바꿔도 a[1][1]은 그대로 2
c[1][1] = 77

# c[0]도 독립 → a[0]에 영향 없음
c[0] = 1000

# a = [10, [99, 2], 20]  ← b[1][0]=99 때문에 a[1][0]도 바뀜
print("a = ", a)
# b = [10, [99, 2], 200] ← b[1][0]=99, b[2]=200
print("b = ", b)
# c = [1000, [1, 77], 20] ← 완전 독립, a에 영향 없음
print("c = ", c)

print()

import copy

# 원본 리스트 생성
a = [1, [5, 6], "X", 10]

# ===== 얕은 복사 =====
# 바깥 리스트는 새로 만들지만
# 내부 리스트 [5, 6]은 주소값만 복사 → a와 b가 같은 [5,6]을 공유
b = a.copy()

# ===== 깊은 복사 =====
# 바깥 + 내부 리스트까지 전부 새로 만듦 → a와 c는 완전 독립
c = copy.deepcopy(a)

# b[1]은 a[1]과 같은 리스트를 공유하므로
# append(99) → a[1]도 [5, 6, 99]로 바뀜 ← a가 바뀌는 이유!
b[1].append(99)

# b[2]는 문자열(str) → 독립적으로 복사됨
# "Y"로 바꿔도 a[2]는 그대로 "X"
b[2] = "Y"

# b 자체에 50 추가 → 바깥 리스트는 독립이므로 a에 영향 없음
b.append(50)

# c[1]은 deepcopy로 새로 만든 리스트 → a[1]과 완전 독립
# c[1][0] = 100 으로 바꿔도 a[1][0]은 그대로 5
c[1][0] = 100

# c 자체에 "NEW" 삽입 (index 1) → a에 영향 없음
c.insert(1, "NEW")

# c[3]은 깊은 복사로 독립 → "Z"로 바꿔도 a에 영향 없음
c[3] = "Z"

# a = [1, [5, 6, 99], "X", 10]  ← b[1].append(99) 때문에 a[1]도 바뀜
print("a = ", a)
# b = [1, [5, 6, 99], "Y", 10, 50]  ← append(99), "Y", append(50)
print("b = ", b)
# c = [1, "NEW", [100, 6], "Z"]  ← insert("NEW"), [100,6], "Z"
print("c = ", c)














