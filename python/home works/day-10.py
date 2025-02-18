#first home work problem/
'''for i in range(1 ,11):
    print(f"3 X {i} = {3*i}.")

#second home work problem/
total = 0
for i in range(1,11):
    total = total + i
print(total)

#third home work problem/
name = input("Enter your name: ")

for i in name:
    print(i)'''

#forth home work problem/
vowels = "aeiou"

count = 0

user = input("Enter the string: ")

for letter in user:
    if letter in vowels:
        count += 1
        print(letter)
print(f"There are {count} vowels in user.")