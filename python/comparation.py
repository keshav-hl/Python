#comparison operator/
a = 10
b = 20

print(a == b)  
print(a != b)
print(a > b)
print(a < b)
print(a <= b)
print(a >= b)

#logical operator/
a = 10
b = 20
print(a<=10 and b>10)
print(a<10 and b>10)
print(a<10 or b>10)
print(not(a>10))
print(not(a>=10))

#membership operator/
n = "keshav"
a = "shiva"
print("k" in n)
print(("a" in n) and ("a" in a))
print(("a" in n) or ("k" in a))
print(not("j" in n))
