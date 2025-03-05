#for looping example/
l = [21,23,11,34,21,54,32,65,67]
dl = []

for num in l:
    dl.append(num)

    dl.sort()
print(dl)

#example - 2/
ll = [21,23,11,34,21,54,32,65,67]
total = 0

for number in ll:
    total += number
    print(total)

#dictionaries in for loop/
dic = {"name" : "keshav", "age" : 20, "gender" : "male"}

for key in dic.keys():
    print(key)

#values printing in loop/
for value in dic.values():
    print(value)

#items use in loop/
student_marks = {"keshav" : 20, "pramod" : 30, "shiva" : 40, "dilip" : 50}

for key, values in student_marks.items():
    print(f"{key} -- {values}.")

#Example - 3/
student = ["keshav" , "pramod", "shiva", "dilip"]
marks = [65,76,44,90]

student_mark = {}

for index, student in enumerate(student):
    student_mark[student] = marks[index]
print(student_mark)

#same but different method/
student = ["keshav" , "pramod", "shiva", "dilip"]
marks = [65,76,44,90]

student_mark = {}

for i in range(1, len(student)):
    student_mark[student[i]] = marks[i]
print(student_mark)

#list Comprehension/
#Example - 1/
l = [7,8,43,46,22,65,785,432]
print(l)
dl = [x for x in l]
dl.sort()
print(dl)

#Example - 2/
dl = [x*2 for x in l]
print(dl)

#Example - 3 indexing in list comprehension/
name = ["keshav","pramod","dilip","shiva"]

i = [i[1] for i in name]
print(i)

#Example - 4 even number printing/
l = [x for x in range(1,11)]
ll = [x for x in l if x % 2 == 0]
print(ll)

#dictionary comprehension/
names = ["keshav","pramod","dilip","shiva"]

dnames = {name:len(name) for name in names}
print(dnames)

#Example - 2/
cp = {
    "bangluru" : 54,
    "mysuru" : 60,
    "mangluru" : 23,
    "ramanagara" : 10
}

lcp = {key:values for key, values in cp.items() if values>30}
print(lcp)


#split method Example - 1/
name = "What is your name."
s = name.split()
print(s)

name = "What_is_your_age"
x =name.split("_")
print(x)

#Example - 2/
s = input("Enter the number: ").split()
x = [int(num) for num in s]
print(x)
