your_list = []

while True:
    element = input("Enter anything: ")
    if (element == "q"):
        break
    else:
        your_list.append(element)

print(your_list)