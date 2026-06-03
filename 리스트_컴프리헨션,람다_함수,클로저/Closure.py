from pip._internal.cli import index_command


def outer():
    x = 10
    def inner():
        return x
    return inner  # inner 함수 자체를 반환 (괄호 없음!)

f = outer()  # f = inner 함수
print(f())   # inner() 실행 → 10 출력

print()

def outer():
    msg = "Hi"
    def inner():
        return msg + " there"  # outer의 msg를 기억
    return inner  # inner 함수 자체 반환 (괄호 없음!)

# outer() 실행 → inner 함수가 fn에 저장됨
fn = outer()
# fn() 호출 → inner() 실행 → "Hi" + " there" → "Hi there" 출력
print(fn())

print()


def outer():
    x = 5
    def inner():
        return x + 2  # outer의 x를 기억
    return inner  # inner 함수 자체 반환

# outer() 첫 번째 호출 → a에 inner 저장 (x=5 기억)
a = outer()
# outer() 두 번째 호출 → b에 inner 저장 (x=5 기억, a와 독립!)
b = outer()

# a() → 5 + 2 = 7
# b() → 5 + 2 = 7
# 결과 → 7 7
print(a(), b())

print()

def maker(n):
    def inner():
        return n * 2
    return inner  # ← 괄호 제거!

f1 = maker(3)  # f1 = inner 함수 (n=3 기억)
f2 = maker(7)  # f2 = inner 함수 (n=7 기억)

# f1() → 3 * 2 = 6
# f2() → 7 * 2 = 14
# 결과 → 6 14
print(f1(), f2())

print()

# nonlocal 이란?
# global → 전역변수 수정
# nonlocal → 바깥 함수(outer)의 변수 수정

def counter():
    c = 0         # counter()의 지역변수
    def inc():
        nonlocal c  # 바깥 함수의 c를 직접 수정하겠다고 선언
        c += 1
        return c
    return inc    # inc 함수 자체 반환

cnt = counter()      # cnt = inc 함수 (c=0 기억)
print(cnt(), cnt(), cnt())  # 1 2 3 출력

print()

def make_adder(a):
    # lambda x: x + a → a를 기억한 채로 함수 반환
    # def inner(x): return x + a 와 동일
    return lambda x: x + a

# make_adder(5) → a=5 기억한 lambda 저장
add5 = make_adder(5)
# add5(10) → x=10 대입 → 10 + 5 = 15 출력
print(add5(10))

print()
def outer():
    items = []
    def add_item(x):
        items.append(x)  # 클로저로 items 기억
        return items
    return add_item  # ← 괄호 제거!

f = outer()       # f = add_item 함수 (items=[] 기억)
print(f(1))       # items = [1]    → [1] 출력
print(f(2))       # items = [1, 2] → [1, 2] 출력 items에 누적되며 출력 ✅





