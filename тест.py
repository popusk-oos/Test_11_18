def copy(a=[1, 2, "Nikita", 888]):
    b = []
    for item in a:
        b.append(item)
    return b


print(copy([1,2,3]) == [1,2,3])
print(copy([1,2,3]) != [1,2])
