# 입력받은 단어의 모음 개수 세기 

word = input("단어를 입력해주세요: ")

# 첫번째 방법: or 연산자 활용 

i = 0
result = 0

while i < len(word):
    c = word[i]
    if c == 'a' or c == 'A' or c == 'e' or c == 'E'or c == 'i' or c == 'I' or c == 'o' or c == 'O' or c == 'u' or c == 'u':
        result += 1
    i += 1

print(result)

# 두번째 방법: list와 in 활용 

character = ['a', 'i', 'o', 'e', 'u', 'A', 'I', 'O', 'E', 'U']

j = 0
result2 = 0

while j < len(word):
    if word[j] in character:
        result2 += 1
    j += 1

print(result2)
