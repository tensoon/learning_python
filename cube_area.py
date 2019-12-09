'''a = float(input("Enter the length of any side of the cube: "))

ca = 6 * (a ** 2)
vol = a ** 3

print(f"The surfice of the cube with side {a} is: {ca}")
print(f"The volume of this cube is: {vol}")'''


def cube_area(a):
    # a = float(input("Enter the length of any side of the cube: "))
    a = float(a)
    ca = 6 * (a ** 2)
    vol = a ** 3
    print(f"The surfice of the cube with side {a} is: {ca}")
    print(f"The volume of this cube is: {vol}")
    return(ca, vol)


cube_area(12)
