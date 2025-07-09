#Calculator program
print("--------------------------------------Calculator-------------------------------")
operation = input("Enter the operation (+,-,*,/): ")
num1 = int(input("Enter the value of num1: "))
num2 = int(input("Enter the value of num2: "))
if operation == "+":
     result = num1 + num2
     print(f"The sum of {num1} and {num2} is {round(result, 3)}")
elif operation == "-":
     result = num1 - num2
     print(f"The Difference of {num1} and {num2} is {round(result, 3)}")
elif operation == "/":
     result = num1 / num2
     print(f"The Divide of {num1} and {num2} is {round(result, 3)}")
elif operation == "*":
     result = num1 * num2
     print(f"The Product of {num1} and {num2} is {round(result, 3)}")
else:
     print("Invalid choice!!,try again...")