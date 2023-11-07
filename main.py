a = int(input("Please enter the a:"))
b = int(input("Please enter the b:"))
c = int(input("Please enter the c:"))
def quadraticFormula1(a,b,c):
    y = (-b + ((b ** 2 - 4 * a * c) ** 0.5)) / (2 * a)
    return (y)

def quadraticFormula2(a,b,c):
    y = (-b - ((b ** 2 - 4 * a * c) ** 0.5)) / (2 * a)
    return (y)

print("The quadratic formula's answer is: ")
print(quadraticFormula1(a,b,c))
print(quadraticFormula2(a,b,c))

quit()