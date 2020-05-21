selectable = ["itemOne", "itemTwo", "itemThree", "itemFour", "itemFive"]

userinput = "1,3,5"

otherinput = "1..3"

# This is for "1,2,3" selection syntax
userinput = [int(x) - 1 for x in userinput.split(",")]
newList = []
for item in userinput:
    newList.append(selectable[item])
print(newList)


# Below is for ".." selection syntax
otherinput = [int(s) - 1 for s in otherinput.split("..")]
start, end = otherinput
print(selectable[start : end + 1])
