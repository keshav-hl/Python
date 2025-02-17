#first home work problem/
t = (1,2,3,4,5)
s = (6,7,8,9,10)

print(t[1:3])
print(t+s)

#second home work problem/
mf = {"apple","banana","cherry"}
ff = {"mango","papaya","banana"}

union = mf | ff
print(union)

intersection = mf & ff
print(intersection)

diff = mf - ff
print(diff)

sy_diff = mf ^ ff
print(sy_diff)

mf.add("sugar")
print(mf)

mf.discard("sugar")
print(mf)

#third home work problem/
k = [1,2,3,4,5]

t = tuple(k)
s = set(k)
print(t,s)

s.add(100000)
print(t,s)
