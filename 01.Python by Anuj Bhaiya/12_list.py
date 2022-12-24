my_list = [1, 2, 3, "somnath", None, 5.6]
print(my_list)
print(my_list[0])

fruits = ["Apple", "Guava", "Papaya"]
print(fruits[1])
print(fruits[-1])

numbers = [0, 1, 2, 3, 4, 5, 6]
# slicing
new_numbers = numbers[2:5]
new_numbers_reverse = numbers[::-1]
print(new_numbers)
print(new_numbers_reverse)

# update list
# list is mutable means, we can update list
fruits[0] = 'Mango'
print(fruits)

# delete list element
# del fruits[2]
print(fruits)

# delete entire fruit list
# del fruits

# List comprehension>>
# list comprehension is an elegant and concise way to create a new list from an existing list in Python
# new_list = [expression  for item in list  if condition]
# example -> a = [2** x for x in range(10)]

a = [x for x in range(10)]
print(a)

b = [x for x in range(100) if x % 2 == 0]  # with some if condition
print(b)

c = [3 ** x for x in range(10)]
print(c)


# List Methods
# append -> insert element in the last of the list
a = [1, 2, 3]
# a[3] = 4  # this will throw an error
a.append(4)
print(a)

# insert
a.insert(1, 0.5)
print(a)

# sort
a = [9, 5, 7, 44, 12, 2, 45, 88, 1, 6]
a.sort()
print(a)
# sort change the original list

fruits.sort()
print(fruits)

# pop -> remove element
a.pop(0)
print(a)

# clear -> clear the entire list elements
# a.clear()
# print(a)

# reverse-> change the original list
a.reverse()
print(a)

# index -> tell the index number
print(fruits.index('Mango'))

# count -> count of given element
print(fruits.count('Mango'))


# Lists functions>>

# len(list)
e = len(fruits)
print(e)

# max(list)
f = max(a)
print(f)

# min(list)
g = min(a)
print(g)

# sum(list)
h = sum(a)
print(h)

# list(seq)-> convert to list
i = "somnath"
j = list(i)
print(j)


# for loop in list
car = ['swift', 'ritz', 'ferrari']
for c in car:
    print(c)
