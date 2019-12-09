'''a = float(input("Enter the length of any side of the cube: "))

xa = 6 * (a * a)
vol = a * a * a

print(f"The surfice of the cube with side {a} is: {xa}")
print(f"The volume of this cube is: {vol}")'''


def cube_area(a):
    # a = float(input("Enter the length of any side of the cube: "))
    a = float(a)
    xa = 6 * (a * a)
    vol = a * a * a
    print(f"The surfice of the cube with side {a} is: {xa}")
    print(f"The volume of this cube is: {vol}")
    return(xa, vol)


cube_area(12)
