fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newList = [x for x in fruits if "a" in x]
newList2 = [x for x in range(10) if x < 5]
newList3 = [x.upper() for x in fruits]
newList4 = ["hello" for x in fruits]
newList5 = [x if x != "banana" else "orange" for x in fruits]
print(newList5) 