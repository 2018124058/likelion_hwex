# 2

sentence = input("Enter a sentence: ")

vowels = ['a', 'e', 'i', 'o', 'u']
result = 0 

i = 0
while i < len(sentence):
    if sentence[i] in vowels:
        result += 1
    i += 1 
    
print(f"Your sentence contains {result} vowel.")
