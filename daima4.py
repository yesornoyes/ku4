def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: Division by zero"

print("选择操作：")
print("1. 相加")
print("2. 相减")
print("3. 相乘")
print("4. 相除")

choice = input("请输入操作编号：")

num1 = float(input("请输入第一个数字："))
num2 = float(input("请输入第二个数字："))

if choice == '1':
    print(num1, "+", num2, "=", add(num1, num2))
elif choice == '2':
    print(num1, "-", num2, "=", subtract(num1, num2))
elif choice == '3':
    print(num1, "*", num2, "=", multiply(num1, num2))
elif choice == '4':
    print(num1, "/", num2, "=", divide(num1, num2))
else:
    print("无效的操作编号").
