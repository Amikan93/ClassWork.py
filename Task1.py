# if __name__ == "__main__":
#     print("1 == 1", 1 == 1)
#     print("1 == 2", 1 == 2)
#     print("1 != 1", 1 != 1)
#     print("1 != 2", 1 != 2)
#     print("1 > 1", 1 > 1)
#     print("1 > 2", 1 > 2)
#     print("2 > 1", 2 > 1)
#     print("1 < 1", 1 < 1)
#     print("1 < 2", 1 < 2)
#     print("2 < 1", 2 < 1)
#     print("1 >= 1", 1 >= 1)
#     print("1 >= 2", 1 >= 2)
#     print("2 >= 1", 2 >= 1)
#     print("1 <= 1", 1 <= 1)
#     print("1 <= 2", 1 <= 2)
#     print("2 <= 1", 2 <= 1)
    
#     print(bool(""))
#     print(bool(0.0))
#     print(bool(None))

# if __name__ == "__main__":
#     competent = True
#     responsible = True
#     print(competent and responsible)

#     competent = True
#     responsible = False
#     print(competent and responsible)

#     competent = True
#     responsible = False
#     print(competent or responsible)

#     competent = False
#     responsible = False
#     print(competent or responsible)

#     previously_fired = True
#     print(not previously_fired)

#     previously_fired = False
#     print(not previously_fired)

#     time = int(input("Enter the current time in hours: "))% 24
#     ticket = False
#     money = True 
#     luggage = False
#     print(money or ticket and not luggage and time > 6)
#     print((money or ticket) and not luggage and time > 6)

# if __name__ == "__main__":
#     first, second = int(input("Enter the first number: ")), int(
#         input("Enter the second number: ")
#     )

#     if first > second:
#         print("The first number is greater than the second number")
#     else: 
#         print("The second number is greater then the first number")


# if __name__ == "__name__":
#     first, second, third = int(input("Input the first number: ")), int(input("Input the second number: ")), int(input("Input the third number: "))

#     if first + second > third:
#         print("The first number is greater than the second number")
#     else: 
#         print("The second number is greater then the first number")


# number = int(input("Enter number:"))
# check_number = (number) % 2

# if check_number:
#     print("Odd number")
# else:
#     print("Even number")

# number = int(input("Enter number:"))
# check_number = (number) // 7

# if check_number:
#     print("Number is multiple 7")
# else:
#     print("Number is not multiple 7")

# number1, number2 = int(input("Enter one number:"), int(input("Enter two number:"))
# )

# if number1 > number2:
#    print("Great")
# else:
#    print("Loose")

# number1, number2 = int(input("Enter two number:"))

# if number1 > number2:1
#    print("Great")

# number1 = int(input("Enter first number:"))
# number2 = int(input("Enter second number:"))

# choice = int(input("Enter" + 1 or "Enter " + 2))

# if choice == 1:
#     print(f"The sum of the three numbers is {number1 + number2}")
# elif choice == 2:
#     print(f"The product of the three numbers is {number1 - number2}")
# elif choice == 'raz':
#     print(f"The product of the three numbers is {(number1 + number2)/2}")
# else:
#     print("Invalid choice")

# def display_board(board, start_position=None, end_position=None):
#     print("  a b c d e f g h")
#     print("-----------------")
#     for i in range(8):
#         print(i + 1, end="|")
#         for j in range(8):
#             if (j+i)%2 == 0:
#                 print("$" +board[i][j], end="")
#             else:
#                 print(board[i][j], end=" ")

#             print("|" + str(i + 1))
#         print(" --------------- ")
#         print(" a b c d e f g h")