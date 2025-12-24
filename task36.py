ls = []
number_of_words = int(input("Enter the number of elements for the lists: "))

for i in range(number_of_words):
    word = input(f"Enter word {i + 1}: ")
    ls.append(word)

longest_word = ls[0]
    
for i in ls:
    if len(i) > len(longest_word):
        longest_word = i

print(longest_word)