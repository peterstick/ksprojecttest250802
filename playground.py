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








def updown():
    cAnswer = random.randint(1, 100)
    count=1



    while True:
        try:
            user_input = int(input("한번 답해보거라 인간 : "))
        except ValueError:
            print("숫자를달라고")
            continue

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



def quiz():
    print("WELCOME TO QUIZ!")
    words = {'apple':1,'banana':2,'grape':3,'melon':4}
    cAnswer = random.choice(list(words.keys()))


    while True:
        user_input=input("힌트따윈없는이불합리한퀴즈를때려맞추거라 : ")

        if user_input != cAnswer:
            print("오답이다 연금술사")

        if user_input == cAnswer:
            print("정답이다 연금술사")
            break






def stop_watch():
    print("WELCOME TO UP STOPWATCH")





while True:
    print('''
    ================메뉴================
    A. Up & Down 게임
    B. 영어 낱말 맞추기
    C. Stop watch 게임
    Z. 프로그램 종료
    ====================================
    ''')
    user_input = input("값을 입력하세요 : ")

    if user_input.lower() == "a":
        updown()

    elif user_input.lower() == "b":
        quiz()
    elif user_input.lower() == "c":
        stop_watch()
    elif user_input.lower() == "z":
        break
