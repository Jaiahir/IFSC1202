x = input("Enter a string: ")

source = x.find("f")
if source == -1:
    print("Zero f")
else:
    source = x.find("f", source + 1)
    if source == -1:
        print("One f")
    else:
        print(source)