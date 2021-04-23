num1 = int(input("Enter 1st Number"))
num2 = int(input("Enter 2nd Number"))
print("Addition is",num1+num2)
print("Subtraction is",num1-num2)
print("Multiplication is",num1*num2)
try:
    print("Division is",num1/num2)
except:
    print("Cannot divisible by zero")