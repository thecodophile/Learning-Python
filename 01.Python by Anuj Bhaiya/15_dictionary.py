# Python dictionary is an unordered collection of items. While other compound data types have only value as an element, a dictionary has a key:value pair.

marks = {'Somnath': 98, 'Santu': 88, 'Pritam': 99, 'Anuj': 89, 1: 99, 2: 33}
print(marks)

print(marks['Santu'])
print(marks[1])

# for loop in dictionary
print("For loops in dictionary: looping through keys")
for i in marks:
    print(i)
print("For loops in dictionary: looping through value")
for i in marks:
    print(marks[i])

'''
Updating Dictionary items>>

you can also update a dictionary by modyfying existing key-value pair or by merging another dictionary to an existing one.

we can add new items or change the value of existing items using assignment operator.

If the key is already present, value gets updated, else a new key:value pair is added to the dictionary.
'''
marks['Rohit'] = 88  # add
print(marks)

marks['Anuj'] = 99  # update
print(marks)
