name = "Somnath"
# multiline string paragraph
paragraph = '''This is a 
multiline
String
Paragraph. This is for testing'''

print(paragraph)

print(name[0])
print(name[3])
print(name[6])
print(name[-1])  # python supported negative indexing
# print(name[7])    #This will cause en error-> string index out of range

print("print the entire name using for loop")
for i in name:
    print(i)

# for i in paragraph:
#     print(i)

# string slice
x = "AnujBhaiya"

print("x[1:4] -> ", x[1:4])
print("x[:4] -> ", x[:4])
print("x[4:] -> ", x[4:])

print("x[:9:2] -> ", x[:9:2])  # we can also define steps
print("Original sring-> ", x)  # slicing method can't change original string

print("x[::-1] -> ", x[::-1])  # negative indexing and negative step size
print("x[0:9:-1] -> ", x[0:9:-1])  # This will print nothing
print("x[-1:0:-1]", x[-1:0:-1])
print("x[-1:0:1]", x[-1:0:1])  # This will print nothing

# string concatination
a = "Somnath"
b = "Dey"
c = a+b
print(c)
print(a*2)  # string multiplication

# python string methods

password = "abcd23"
print(password.isalpha())  # is all string character alphabet or not?

s = '123'
print(s.isdigit())  # is all string character digit or not?

_name = "somnath"
print(_name.islower())
print(_name.isupper())

print("Convert to lower case-> ", name.lower())
print(name)  # this method can't change the original string
print("Convert to upper case-> ", name.upper())

x = "     santu     "
print("x.lstrip() ->", x.lstrip())
print("x.rstrip() ->", x.rstrip())
