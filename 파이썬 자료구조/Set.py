nums = {1, 2, 3}
nums.add(3)
nums.add(4)
nums.add(4)
print(nums)
print(len(nums))

print()

s = {10, 20, 30}
s.discard(40)
print(s)
s.remove(20)
print(s)

print()

a = {"apple", "banana"}
b = {"banana", "cherry", "date"}
u1 = a.union(b)
u2 = a | b
print(u1)
print(u2)

print()

user1 = {"movie", "music", "game", "travel"}
user2 = {"music", "travel", "cook"}
u1 = user1.intersection(user2)
u2 = user1 & user2
print(u1)
print(u2)

print()

all_tasks = {"login", "signup", "payment", "logout"}
done = {"login", "logout"}
u1 = all_tasks.difference(done)
u2 = all_tasks - done
print(u1)
print(u2)

print()

data = [3, 1, 2, 3, 4, 2, 5, 1]
s = set(data)
result = sorted(list(s))
print(result)

print()

s1 = "programming"
s2 = "algorithm"
set1 = set(s1)
set2 = set(s2)
common = set1.intersection(set2)
print(common)

print()

a = {1, 2, 3}
b = {4, 5, 6}
c = [5, 6, 7]
a.update(b)
print(a)
a.update(c)
print(a)



