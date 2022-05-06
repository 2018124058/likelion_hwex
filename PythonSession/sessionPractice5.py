
h = int(input("나무 막대의 높이 H를 입력해주세요: "))
x = int(input("낮 동안 올라가는 높이 X를 입력해주세요: "))
y = int(input("밤 동안 미끄러지는 높이 Y를 입력해주세요: "))

day = 1
height = 0

while True:
    height += x
    if height >= h:
            break
    else:
        height -= y
    day += 1 

print(day)

