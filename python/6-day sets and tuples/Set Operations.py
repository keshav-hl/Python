#Union, it combines tow sets and removes the duplicate element/
set1 = {1, 2, 3}
set2 = {3, 4, 5}
union_set = set1 | set2 
print(union_set)

#Intersection, it prints the duplicate element in terminal/
intersection_set = set1 & set2  
print(intersection_set)

#Difference, it removes the similar element in set1 and prints only set1/
difference_set = set1 - set2 
print(difference_set)

#Symmetric Difference, it prints combining the two sets without any duplicated values/
sym_diff_set = set1 ^ set2 
print(sym_diff_set)
