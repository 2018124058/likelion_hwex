# 1부터 입력받은 수까지 합 구하는 함수

n = int(input("숫자 입력: "))

def mysum(n):
    result = 0
    i = 1
    while i <= n:
        result += i
        i += 1
    print(result)

mysum(n)