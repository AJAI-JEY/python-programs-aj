a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

a, b = b, a  # Swapping without a third variable

print("After swapping:")
print("a =", a)
print("b =", b)
