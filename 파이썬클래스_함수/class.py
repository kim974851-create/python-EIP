# ===== 1. 기본 클래스 =====
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        return f"{self.name}, {self.age}"


p = Person("Kim", 30)
print(p.greet())  # Kim, 30

print()


# ===== 2. 나이 증가 클래스 =====
class CounterPerson:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def birthday(self):
        self.age += 1  # 호출할 때마다 나이 +1

    def info(self):
        return f"{self.name}, {self.age}"


p = CounterPerson("Lee", 25)
p.birthday()  # 26
p.birthday()  # 27
print(p.info())  # Lee, 27

print()


# ===== 3. 합격/불합격 판별 클래스 =====
class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def result(self):
        if self.score >= 60:
            return f"{self.name} PASS"
        else:
            return f"{self.name} FAIL"


s1 = Student("Kim", 75)
s2 = Student("Park", 58)

print(s1.result())  # Kim PASS
print(s2.result())  # Park FAIL

print()


# ===== 4. 상품 리스트 출력 =====
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def info(self):
        return f"{self.name}, ({self.price})"  # 쉼표 뒤 공백 추가


p1 = Product("Mouse", 15000)
p2 = Product("Keyboard", 30000)
p3 = Product("Monitor", 200000)
products = [p1, p2, p3]

for p in products:
    print(p.info())

print()


# ===== 5. 클래스 변수로 인스턴스 개수 세기 =====
# ===== 1. Person (greet) =====
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        return f"{self.name}, {self.age}"

# 1. Person("Kim", 30) → name="Kim", age=30 저장
p = Person("Kim", 30)
# 2. p.greet() 호출 → "Kim, 30" 반환 후 출력
print(p.greet())

print()


# ===== 2. CounterPerson =====
class CounterPerson:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def birthday(self):
        self.age += 1  # 호출할 때마다 age +1

    def info(self):
        return f"{self.name}, {self.age}"

# 1. CounterPerson("Lee", 25) → name="Lee", age=25 저장
p = CounterPerson("Lee", 25)
# 2. birthday() 첫 번째 호출 → age = 26
p.birthday()
# 3. birthday() 두 번째 호출 → age = 27
p.birthday()
# 4. p.info() → "Lee, 27" 출력
print(p.info())

print()


# ===== 3. Student =====
class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def result(self):
        # score >= 60 이면 PASS, 미만이면 FAIL
        if self.score >= 60:
            return f"{self.name} PASS"
        else:
            return f"{self.name} FAIL"

# 1. Student("Kim", 75) → score=75 저장
s1 = Student("Kim", 75)
# 2. Student("Park", 58) → score=58 저장
s2 = Student("Park", 58)
# 3. s1.result() → 75 >= 60 이므로 "Kim PASS" 출력
print(s1.result())
# 4. s2.result() → 58 < 60 이므로 "Park FAIL" 출력
print(s2.result())

print()


# ===== 4. Product =====
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def info(self):
        return f"{self.name}, ({self.price})"

# 1. p1, p2, p3 세 개의 Product 인스턴스 생성
p1 = Product("Mouse", 15000)
p2 = Product("Keyboard", 30000)
p3 = Product("Monitor", 200000)
# 2. products 리스트에 담음
products = [p1, p2, p3]
# 3. for문으로 순회하며 p.info() 호출 → 각 상품 이름과 가격 출력
for p in products:
    print(p.info())

print()


# ===== 5. Counter =====
class Counter:
    count = 0  # 클래스 변수 - 모든 인스턴스가 공유

    def __init__(self, name):
        self.name = name
        Counter.count += 1  # 생성될 때마다 +1

# 1. Counter("A") 생성 → count = 1
c1 = Counter("A")
# 2. Counter("B") 생성 → count = 2
c2 = Counter("B")
# 3. Counter("C") 생성 → count = 3
c3 = Counter("C")
# 4. Counter.count 출력 → 3
print(Counter.count)

print()


# ===== 6. Rectangle =====
class Rectangle:
    def __init__(self, w, h):
        self.w = w
        self.h = h

    def area(self):
        return self.w * self.h  # 넓이 = 가로 * 세로

    def info(self):
        # area() 내부 호출 후 결과 포함해서 반환
        return f"w={self.w}, h={self.h}, area={self.area()}"

# 1. Rectangle(4, 5) → w=4, h=5 저장
r = Rectangle(4, 5)
# 2. r.info() → area() 호출 → 4*5=20 → "w=4, h=5, area=20" 출력
print(r.info())

print()


# ===== 7. Person (__str__) =====
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} ({self.age})"  # print() 시 자동 호출

# 1. Person("Choi", 40) → name="Choi", age=40 저장
p = Person("Choi", 40)
# 2. print(p) → __str__ 자동 실행 → "Choi (40)" 출력
print(p)


# ===== 8. Temp (소멸자) =====
class Temp:
    def __init__(self, name):
        self.name = name
        print(self.name, "생성")  # 인스턴스 생성 시 출력

    def __del__(self):
        print(self.name, "소멸")  # 인스턴스 삭제 시 자동 호출

# 1. Temp("obj1") → __init__ 실행 → "obj1 생성" 출력
t = Temp("obj1")
# 2. del t → __del__ 실행 → "obj1 소멸" 출력
del t
# 3. "끝" 출력
print("끝")

print()


# ===== 9. Person (기본값) =====
class Person:
    def __init__(self, name, age=20):  # age 기본값 20
        self.name = name
        self.age = age

    def info(self):
        return f"{self.name}, {self.age}"

# 1. Person("Kim") → age 생략 → 기본값 20 적용
p1 = Person("Kim")
# 2. Person("Lee", 35) → age=35 직접 전달
p2 = Person("Lee", 35)
# 3. p1.info() → "Kim, 20" 출력
print(p1.info())
# 4. p2.info() → "Lee, 35" 출력
print(p2.info())




