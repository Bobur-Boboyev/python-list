words = ["u", "olma", "kitoblar", "python", "men", "dasturchi"]
small = []
medium = []
large = []

for w in words:
    if len(w) <= 3:
        small.append(w)
    elif 4 <= len(w) <= 6:
        medium.append(w)
    else:
        large.append(w)

print(small)
print(medium)
print(large)