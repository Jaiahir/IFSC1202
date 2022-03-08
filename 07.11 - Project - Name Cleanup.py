def ProperCase(s):
    if s == "":
        return ""
    ch = s[0].upper()
    return (ch + s[1:len(s)].lower())

def RemoveNewLine(s):
    return s.replace("\n", "")

def trim(s):
    s = s.strip()
    return " ".join(s.split())

def FirstName(s):
    s = trim(s)
    last = s.find(" ")
    return s[0:last]

def LastName(s):
    s = trim(s)
    first = s.rfind(" ")
    return s[first + 1:len(s)]

def MiddleName(s):
    s = trim(s)
    first = s.find(" ")
    last = s.rfind(" ")
    return s[first + 1: last]

def mainOutput():

    print("{:<10} {:<10} {:<10}".format("First", "Middle", "Last"))
    print("{:<10} {:<10} {:<10}".format("----------", "----------", "----------"))

    file = open("07.11 Names.txt", "r")
    names = file.readlines()

    for name in names:
        name = RemoveNewLine(name)
        name = trim(name)

        firstName = FirstName(name)
        middleName = MiddleName(name)
        lastName = LastName(name)

        firstName = ProperCase(firstName)
        middleName = ProperCase(middleName)
        lastName = ProperCase(lastName)

        print("{:<10} {:<10} {:<10}".format(firstName, middleName, lastName))


mainOutput()