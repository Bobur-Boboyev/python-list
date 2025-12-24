names = []

while True:
    name = input("Name (type stop to exit): ")
    if name.lower() == 'stop':
        break
    names.append(name)

print(len(names))