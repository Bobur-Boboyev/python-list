list_length = int(input("Enter the number of elements for the lists: "))

list1 = []
list2 = []

for i in range(1, list_length + 1):
    value = int(input(f"List 1 - Element {i}: "))
    list1.append(value)

for i in range(list_length):
    value = int(input(f"List 2 - Element {i}: "))
    list2.append(value)

list1 = list2
list2 = list1

print(list1)
print(list2)