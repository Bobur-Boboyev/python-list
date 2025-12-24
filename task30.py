words = []
palindromes = []

for i in range(5):
    word = input(f"{i+1}-word: ")
    words.append(word)
    if word.lower() == word[::-1].lower():
        palindromes.append(word)

print(palindromes)