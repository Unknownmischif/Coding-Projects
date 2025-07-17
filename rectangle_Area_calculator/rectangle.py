import calculate

length = float(input("Enter the length of said rectangle"))
width = float(input("Enter the width of said rectangle"))

area = calculate.area(length, width)
perimeter = calculate.perimeter(length, width)

print(f"The area of the ractangle is: {area}")
print(f"The perimetr of the ractangle is: {perimeter}")