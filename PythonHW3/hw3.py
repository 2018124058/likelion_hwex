# 3
name_list = []

while True:
    name = input("Enter a name (q to quit): ")
    if name == "q":
        break
    else:
        if " " in name:
            split_name = name.split() # 리스트 
            for i in split_name:
                name_list.append(i)
        else:
            name_list.append(name)

num_a = 0
for i in name_list:
    num_a += i.count("a")

print("Number of names and letter 'a': ", len(name_list), ",", num_a)