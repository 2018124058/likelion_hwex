# 4
num_list = []

while True:
    num = int(input("Enter a number: "))
    if num <= 0:
        break
    else:
        num_list.append(num)

print("The largest number entered was", float(max(num_list)))
result = float(max(num_list))
print(f"The largest number entered was {result: .2f}") # 소숫점 두자리수까지 

