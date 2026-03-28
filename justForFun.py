import time
import random
# print("마법의 소라고동님")
#
# time.sleep(3)
#
# print("왜")
#
# time.sleep(1)
#
# print("배고파요")
#
# time.sleep(1)
#
# print("안돼")

while True:
    print("마법의 소라고동님")
    time.sleep(2)
    print("왜.")
    question=input()
    time.sleep(2)
    answer = random.randint(1,7)

    if answer == 1:
        print("안돼.")
    elif answer == 2:
        print("그래.")
    elif answer == 3:
        print("언젠가는.")
    elif answer == 4:
        print("가만히 있어.")
    elif answer == 5:
        print("그것도 안돼.")
    elif answer == 6:
        print("다시 한번 물어봐.")
    elif answer == 7:
        print("다 안 돼.")
