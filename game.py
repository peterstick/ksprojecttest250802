import random

weaponLevel = 0


print("게임에 오신 것을 환영합니다.")


while True:

    print("""
        0. 종료하기.
        1. 무기 강화
       """)

    choice = input("숫자를 입력하세요 (0을 입력할 시 종료)")


    if choice == "0":
        print("게임을 종료합니다.")
        exit()


    upgradeRates = [
        {"up": 70, "keep": 30, "down": 0, "break": 0},
        {"up": 60, "keep": 25, "down": 10, "break": 5},
        {"up": 50, "keep": 30, "down": 15, "break": 5},
        {"up": 45, "keep": 30, "down": 20, "break": 5},
        {"up": 40, "keep": 30, "down": 20, "break": 10},
        {"up": 35, "keep": 30, "down": 25, "break": 10},
        {"up": 30, "keep": 30, "down": 30, "break": 10},
        {"up": 25, "keep": 30, "down": 30, "break": 15},
        {"up": 20, "keep": 30, "down": 30, "break": 20},
        {"up": 15, "keep": 30, "down": 30, "break": 25},
        {"up": 0, "keep": 100, "down": 0, "break": 0},
    ]

    ran_num = random.randint(0,99)

    rate = upgradeRates[weaponLevel]


    if ran_num < rate["up"]:
        print("강화에 성공했다. 무기 레벨 +1")
        weaponLevel += 1
        if weaponLevel == 10:
            print("최고 레벨에 도달했습니다.")
        print("현재 무기 레벨 :",  weaponLevel)
    elif ran_num < rate["up"] + rate["keep"]:
        print("아무 일도 일어나지 않았다.")
        weaponLevel = weaponLevel
        print("현재 무기 레벨 :", weaponLevel)
    elif ran_num < rate["up"] + rate["keep"]+ rate["down"]:
        if weaponLevel <= 0:
            print("더 이상 낮아질 레벨이 없습니다.")
            exit()
        print("강화에 실패했다. 무기 레벨 -1")
        weaponLevel -= 1
        print("현재 무기 레벨 :", weaponLevel)
    else:
        print("조졌다 박살났다. 무기 레벨 0")
        weaponLevel = 0
        print("현재 무기 레벨 :", weaponLevel)




