name = "shuvzsh"
print(name)
print(name[0])
print(name[1])
print(name[2])
print(name[3])
print(name[4])
# print(name[5]) throws an error


poem = '''ABCDEFG IJKLMNOP QRS TUV WX Y&Z 
Now I know my ABC'''

print(poem)
print(len(name))
print(poem.lower())
print(poem.upper())
print(name.strip())
print(len(name.strip()))

print(name.replace("sh", "ar"))

print(name.isdigit())
print(name.isnumeric())
print(name.isalpha())
print(name.isspace())

print(name[0:3])
print(name[1:2])
print(name[2:3])
print(name[1:-1]) # is same as [1 : (-1 + len(name)) or name [1:6]]
print(name[1:6])

text = "apple,banana,orange"
items = text.split(",")

print(items)






