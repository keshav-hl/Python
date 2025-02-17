#day-2 first_home work/
a = 2
b = 5

print(a+b)
print(a-b)
s= abs(a-b)
print(s)
print(a*b)
print(a/b)
print(" ")

#second_homework swapping two variables/
print(f"a: {a}, b: {b}")

temp = a
a = b
b = temp

print(f"a: {a}, b: {b}")
print(" ")

#solving same problem by xor gate/
x = 5
y = 2
print(f"x: {x}, y: {y}")

x = x^y
y = x^y
x = x^y

print(f"x: {x}, y: {y}")
print(" ")

#solving in another method/
c = 8
d = 4
print(f"c: {c}, d: {d}")

c = c + d
d = c - d
c = c - d

print(f"c: {c}, d: {d}")