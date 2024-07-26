set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
print("Original sets:")
print(set1)
print(set2)
print("Difference of set1 and set2 using difference():")
print(set1.difference(set2))
print("Difference of set2 and set1 using - operator:")
print(set2 - set1)
intersection=set1|set2
print(f'The intersection of set 1 and 2 is ',intersection)
union=set1&set2
print(f'The union of set 1 and 2 is ',union)