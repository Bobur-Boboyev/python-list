numbers = []

for i in range(10):
    number = int(input(f"{i+1}-number: "))
    numbers.append(number)

ls = []

for s in numbers:
    if numbers.count(s) == 1:
        ls.append(s)

print(numbers)
print(ls)