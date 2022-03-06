x = input("Enter a string: ")

c = 0
if len(x) > 0:
    c = 1
    for ch in x:
        if ch == ' ':
            c += 1

print(c, "words")