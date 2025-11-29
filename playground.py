import random
import time


# def print_times_table(number: int):
#     print(number, "*", 1, "=", number * 1)
#     print(number, "*", 2, "=", number * 2)
#     print(number, "*", 3, "=", number * 3)
#     print(number, "*", 4, "=", number * 4)
#     print(number, "*", 5, "=", number * 5)
#     print(number, "*", 6, "=", number * 6)
#     print(number, "*", 7, "=", number * 7)
#     print(number, "*", 8, "=", number * 8)
#     print(number, "*", 9, "=", number * 9)
#
# def example_function(input_arg:int)


cAnswer = random.randrange(1, 100)
count=1


while True:
    user_input = int(input("한번 답해보거라 인간 : "))


    if user_input > cAnswer:
        print("down")
        count += 1
    elif user_input < cAnswer:
        print("up")
        count += 1


    if user_input == cAnswer:
        print("정답이다 끄지라")
        count=0
        break

