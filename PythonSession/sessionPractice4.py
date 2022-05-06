enter = True
num_list = []

while enter:
    num = input("숫자를 입력해주세요: ")
    if num == 'q':
        enter = False
    else:
        num_list.append(int(num))

min = num_list[0]
max = num_list[0]

i = 0 
while i < len(num_list):
    if min > num_list[i]:
        min = num_list[i]
    if max < num_list[i]:
        max = num_list[i]
    i += 1

print(len(num_list), "개의 숫자 중 최솟값은 ", num_list.index(min) + 1, "번째 수" , min, "입니다")  # min(num_list)
print(len(num_list), "개의 숫자 중 최댓값은 ", num_list.index(max) + 1, "번째 수" , max, "입니다")  # max(num_list)
        
    