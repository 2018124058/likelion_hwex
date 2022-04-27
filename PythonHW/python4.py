fruits = {}

while True:
    fruit_type = input("Enter a fruit type(q to quit): ")
    if (fruit_type == "q"):
        print(fruits)
        break
    else:
        fruit_weight = input("Enter the weight in kg: ")
        fruits[fruit_type] = fruit_weight