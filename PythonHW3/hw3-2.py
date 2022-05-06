# 3
names = []
num_letter = 0

while True:
    name = input('Enter a name (q to quit): ').lower().split()
    if 'q' in name:
        break
    names += name

num_names = len(names)

for name in names:
    num_letter += str(name).count('a')

print('Number of names and letter ''a'':',num_names,num_letter)