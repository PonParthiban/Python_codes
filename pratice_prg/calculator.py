#Calculator program
print("--------------------------------------Calculator-------------------------------")
opera = input("Enter the operation (+,-,*,/): ")
num1 = int(input("Enter the value of num1: "))
num2 = int(input("Enter the value of num2: "))
if opera == "+":
     result = num1 + num2
     print(round(result, 3))
elif opera == "-":
     result = num1 - num2
     print(round(result, 3))
elif opera == "/":
     result = num1 / num2
     print(round(result, 3))
elif opera == "*":
     result = num1 * num2
     print(round(result, 3))
else:
     print("invalid choice!!,try again...")