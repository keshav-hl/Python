#Debugging in python/
i = 0

while i<=5:
    print(i, end="  ")
    i += 1

#debugging Example - 2/
for i in range(2,11):
    print(" ")
    for j in range(1,11):
        print(f"{i} X {j} = {i*j}.")

#Example - 3/
l = [12,23,34,45,56,67,78,89]
cl = [ ]

for i in range(len(l)):
    v = l[i]
    c = l[-1]
    x = v*c
    if x%2==0:
        cl.append(x)
        print(cl)