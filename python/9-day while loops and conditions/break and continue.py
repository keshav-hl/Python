#break in while loop/
sheep = 1

while sheep <= 10:
    print(f"sheep count is {sheep}")
    if sheep == 5:
        print(f"{sheep} is Enough.")
        break
    sheep += 1

#continue in while loop/
sheep = 1

while sheep <= 5:
    if sheep == 4:
        sheep += 1
        continue
    print(f"There are {sheep} sheeps.")
    sheep += 1