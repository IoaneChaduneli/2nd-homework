expression = input("Enter expression: ")

expression_list = expression.split()

x = float(expression_list[0])
y = expression_list[1]
z = float(expression_list[2])

if  y == "+":
    result = x + z
elif y == "-":
    result = x -z
elif y == "/":
    result = x / z
    if z == 0:
        print(ZeroDivisionError)
elif y == "*":
    result = x * z

print(result)