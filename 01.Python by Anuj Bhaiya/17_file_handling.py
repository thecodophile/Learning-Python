'''
> What is file?
-> File is a named location on disk to store related information. It is used to permanently store data in a non-volatile memory (e.g. hard disk)

in python, a file operation takes place in the following order.

1. Open a file
2. Read or write(perform operation)
3. Close the file

> How to Open a file?
-> Python has a built-in function open() to open a file. this fuction returns a file object. We can specify the mode while opening a file. In mode, we specify whether we want to read "r". Write "w" or append "a" to the file. We also specify if we want to open the file in text mode or binary mode.

We can also use statement instead of open() and close()
with open('filename.txt', 'w') as fileObject:
'''


# Reading a file usign Python->
'''
# by default file open in read mode
f = open("01.Python by Anuj Bhaiya/data.txt", 'r')

# print(f.readline())  # readline read newline character also
# print(f.readline())
# print(f.readline())
# print(f.readline())
# print(f.readline())

for line in f:
    print(line)

#Note-> if we did some error before file closed then the file will never detach. This will very expensive.

f.close()

'''
'''
# to overcome this pitfall we can ->

# this will ensure to close file automaticly, even if we encountered error.
with open("01.Python by Anuj Bhaiya/data.txt") as f:
    # for line in f:
    #     print(line)

    # print(f.read())  # read the entire file
    print(f.read(10))  # read 10 characters of the file
    print(f.read(10))  # read next 10 characters of the file

    f.seek(0)  # move mouse cursor to that position
'''

# Write in a file
lines_data = ['Santu\n', 'Gaurav\n', 'Kite']

with open("01.Python by Anuj Bhaiya/data.txt", 'w') as file:
    file.write("Somnath\n")  # but this will overwrite the entire file content.
    file.writelines(lines_data)  # write multiple lines

# But write mode is dengerous, because it will erase the entire file content and then overwrite it. If we want to apend data in the file with the existing data then->
with open("01.Python by Anuj Bhaiya/data.txt", 'a') as file:
    file.write("\nThis data will apend with existing data.")
