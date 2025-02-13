#Splitting a sentence into words/
sentence = "I love coding in Python"
words = sentence.split()
print(words)

#Splitting a string with commas/
data = "apple,banana,mango"
fruits = data.split(",")
print(fruits)

#Limiting the number of splits/
sentence = "Python is fun to learn"
words = sentence.split(" ", 2)
print(words)