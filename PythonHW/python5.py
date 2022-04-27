import random, time

print("5개의 메뉴를 추가해주세요! 5개가 입력되면 오늘의 메뉴를 추천해드려요.")
print("동일한 메뉴는 안돼요!")
print()

menu = []

while len(menu) < 5:
    food = input("메뉴 추가: ")
    if (set(menu) & set([food]) == set([food])):
        print("이미 있는 메뉴예요! 다른 메뉴를 입력해주세요.")
        print("")
    else:
        menu.append(food)
        print("현재 메뉴 수: ", len(menu))
        print("")

if len(menu) == 5:
    
    i = 3
    while i > 0:
        print(i)
        time.sleep(1)
        i -= 1
    print("")
    
    print(menu)
    print("과연 오늘의 메뉴는?")
    print("")
    
    i = 3
    while i > 0:
        print(i)
        time.sleep(1)
        i -= 1
    print("")

    today_menu = random.choice(menu)
    print("오늘의 메뉴는", menu.index(today_menu), "번째 메뉴,", today_menu, "입니다.")
