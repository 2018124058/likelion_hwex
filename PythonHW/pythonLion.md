# 라이언 파이썬 강의 메모 

DRY(don't repeat yourself)  
들여쓰기의 중요성  
- 어디서부터 어디까지 반복할지 알려준다  

## time
```
import time
time.sleep(1) # 1초 쉬기
```
## random
```
import random
random.choice(list_name) # 랜덤으로 하나 뽑기 
```

`break # 반복문 멈추기`


## list
```
# list 정의
food = ["치킨", "샐러드", "파스타"] 

# 일부 정보 불러오기 
# 인덱스: 0부터. 음수면 뒤부터. 
print(food[0]) # 첫번째 값인 치킨 출력
# 값 추가
food.append("김밥")
# 값 삭제
del foods[0]
```


## dictionary  
정의 `{key:value}`  
값 추가 `dictionary_name[key] = value`
값 삭제 `del dictionary_name[key]`  

```
# dictionary 정의
information = {"고향":"강릉", "취미":"영화관람", "좋아하는 음식":"국수"}
print(information)

# 일부 정보 불러오기 
print(information.get("고향")) # 강릉
# 추가하기 
information["특기"] = "낮잠"
# 없애기
del information["취미"]
# 정보 묶음 개수
len(information)
# dictionary 비우기 
information.clear()
```
## 반복  
```
# food 리스트 모든 값 출력 
for x in food:
    print(x)

# information dictionary 모든 값 출력 
for x, y in information.items():
    print(x)
    print(y)

# dictionary의 key만 출력 
for x in information:
    print(x)
```  

## 집합 (set)  
- list와 다르게 순서가 없다  
- 겹치는 요소x 
- 합집합, 차집합, 교집합 연산   

```
food = ["피자", "된장찌개", "샐러드", "된장찌개"]
food_set1 = set(food) # food list를 set으로. 중복된 요소는 하나만 남는다  
food_set2 = set(["피자","된장찌개","샐러드"]) # 같은 결과

food = list(food_set1) # set을 list로 변환 
```  

```
# 집합 연산
menu1 = set(["파스타", "샐러드", "돈까스"])
menu2 = set(["돈까스", "김밥", "쫄면])
# 합집합
menu3 = menu1 | menu2 # 중복된 돈까스는 하나만 남음
# 교집합  
menu1 & menu2
# 차집합
menu1 - menu2 
```

## if  
```
import random
food_today = random.choice(["돈까스","샐러드","파스타"])

if (food == "돈까스"):
    print("곱배기")  # if 조건 만족 시 실행
else:
    print("그냥")    # if 조건 불만족 시 실행 
print("종료")        # if 조건 만족 여부와 상관없이 실행
```

## input 함수
`input("안내메세지") # 사용자 입력 받기`  
```
lunch = []
while True:            # 반복 
    print(lunch)
    item = input("음식 입력: ")
    if (item == "q"):
        break
    else: 
        lunch.append(item) # 리스트에 인풋값을 추가 
```

## 함수  
함수 정의
```
def 함수이름():
    실행내용    # 들여쓰기 유의하기 
```
