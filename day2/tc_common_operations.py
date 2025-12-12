# Time complexity common operations

list = [1, 23, 4, 5345, 65, 45, 45, 4, 654, 54, 5, 4, 54, 5, 4, 54, 5, 4]

# 1. Copy => O(n)
list2 = list.copy()  # O(n)
print(list2)


# 2. Append => O(1)
list.append(3)


# 3. Pop last => O(1)
list.pop()


# 4. Pop intermediate => O(n)
list.pop(4)

# 5. Insert => O(n)
list.insert(3, 40)


# 6. Get Item => O(1)
list[4]


# 7. Set item => o(1)
list[4] = 34

# 8. Delete item => O(n)
list.remove(34)


# 9. Iteration / Looping => O(n)
for i in list:
    pass

# 10. Get slice => O(k)
# K refers to the inner lenth of the slice
list[2, 4]

# 11. Del slice => O(n)
del list[2:5]
del list[:2]  # delete ing 0,1,2
del list[8:]  # from 8th to the last element
del list[::2]  # every second element
del list[:]  # clear

# 12. Set Slice=> O (K+n)

# 13. Extend [1] => O(k)

# 14. Sort => O(n log n)

# 15. Multiply => O(nk)

# 16. x in s => O(n)
10 in list

# 17. min(s) , max (1)=> O(n)
min(list)
max(list)
# 18. length => O(1)
len(list)


# ----------------Sets Operations--------->
mySet = {23, 23, 23, 23, 2, 32, 32, 3, 2, 32, 3, }

# 1. X in s => Avg Case = O(1) Worst Case => O(n)


# ----------------Dictionaries Operations--------->

dict = {
    "a": 23,
    "b": 132,
    "c": 23,
    "d": 23,
    "e": 53,
    "f": 634,
}

# 1. Key in d => Avg Case => O(1) , Worst Case=> O(n)

# 2. Copy[3] =>  Avg Case => O(1) , Worst Case=> O(n)
# 3. Get Item =>  Avg Case => O(n) , Worst Case=> O(n)
# 4. set item  =>  Avg Case => O(1) , Worst Case=> O(n)
# 5. delete item =>  Avg Case => O(1) , Worst Case=>O(n)
# 6. iteration =>  Avg Case => O(n) , Worst Case=>O(n)
