# print("'1'. Addition \n", "'2'. Subtraction \n", "'3'. Multiplication \n", "'4'. Division \n")
# dialog = int(input("Select an operation: "))

menu = 0
while menu < 100:
   
                num1 = int(input("Enter the first number: "))
                operator = input("Enter an operator (+, -, *, /) - ")
                num2 = int(input("Enter the second number: "))
                
                if operator == "+":
                    print(num1 + num2)
                elif operator == "-":
                    print(num1 - num2)
                elif operator == "*":
                    print(num1 * num2)
                elif operator == "/":
                    print(num1 / num2)
                else:
                    print("Error")
menu += 1