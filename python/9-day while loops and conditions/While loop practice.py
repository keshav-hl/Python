#Example 1 / how many time the student will attempt the exam and he will give up/
fail = True
i = 1

while fail:
    if i % 2 != 0:
        i += 1
        continue
    print(f"Attempt of student {i}..")
    i += 1
    if i > 20:
        break
print("Give up!")

#Example 2 / how to print the name iteration/
i = 0

while i <= 10:
    x = 0
    while x < i:
        print("keshav", end="-")
        x += 1
    i += 1

#10 keshav/
for i in range(10):
    print("keshav")

