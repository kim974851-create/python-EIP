text = "Python"
# text[1:5] = "ytho", text[-1] = "n", text[::2] = "Pto"
result = text[1:5] + text[-1] + text[::2]
print(result)  # ythonPto

print()

s = "Hello, Python!"
print(s[7:13])   # Python  (인덱스 7~12)
print(s[-7:-1])  # Python  (뒤에서 7~2번째)
print(s[::2])    # Hlo yhn (2칸 간격)

print()

text = "Python"
for i in range(len(text)):
    if i % 2 == 0:
        print(text[i], end="")  # 짝수 인덱스 → 문자
    else:
        print("-", end="")      # 홀수 인덱스 → -
print()  # P-t-o-n

text = "Python3.10"
digits = ""
letters = ""
for ch in text:
    if ch.isdigit():
        digits += ch    # 숫자만 추가
    else:
        letters += ch   # 문자만 추가
print(letters)  # Python.
print(digits)   # 310

print()

text = "Python"
slice1 = text[1:5:2]   # 인덱스 1~4, 2칸 간격 → "yh"
slice2 = text[-5:-1:2] # 뒤에서 5~2번째, 2칸 간격 → "yh"
print(slice1, slice2, slice1 == slice2)  # yh yh True

print()

s = "Python"
slice1 = text[::-1]      # 문자열 뒤집기 → "nohtyP"
slice2 = text[-1:-7:-1]  # 끝~처음 역순 → "nohtyP"
print(slice1, slice2)    # nohtyP nohtyP

print()

s = "ABCDEFGHIJ"
slice1 = s[-1:-6:-2]  # 끝에서 역순 2칸 간격 → "JHF"
slice2 = s[8:3:-2]    # 8번째에서 역순 2칸 간격 → "IGA"
print(slice1, slice2) # JHF IGA

print()

text = "Python"
a = text[-1:2:-1]  # 끝~3번째 역순 → "noh"
b = text[-1:5:-1]  # 시작 <= 끝 → 빈 문자열
print(a)  # noh
print(b)  # (빈 문자열)

print()

text = "Python"
slice1 = text[5:1:1]   # 간격 양수, 시작 > 끝 → 빈 문자열
slice2 = text[-1:-6:2] # 간격 양수, 역방향 → 빈 문자열
print(slice1)               # (빈 문자열)
print(slice2)               # (빈 문자열)
print(len(slice1 + slice2)) # 0