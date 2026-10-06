items = {"apple","banana","orange"}

items.add("mango")
print(items)

items.update(["grape","dragon"])
print(items)

# items.remove("banana") error
# items.discard("bananaaee") # no error
a = items.pop()
print(items)
print(a)