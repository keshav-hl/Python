# First Example/ On end point
if_true = True

while if_true:
    print("the condition is true...")

#Second Example/ It has end point/
condition = True
i = 1

while i <= 20:
    print(f"The condition is {i}..")
    i += 1

#Third Example/ same as the above but different code/
condition = True
i = 1

while condition:
    print(f"The condition is {i}...")
    i += 1
    if i > 20:
        break