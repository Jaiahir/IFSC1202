FromValue = float(input("Enter From Value: "))

inch = "inch"
ft = "ft"
yd = "yd"
mi = "mi"

FromUnit = str(input("Enter From Unit (inch, ft, yd, mi): "))
if FromUnit == inch or ft or yd or mi:
    print("")
else:
    quit("FromUnit is not valid")


ToUnit = str(input("Enter To Unit (inch, ft, yd, mi): "))
if ToUnit == inch or ft or yd or mi:
    print("")
else:
    quit("ToUnit is not valid")

miToin = FromValue * 63360
miToft = FromValue * 5280
miToyd = FromValue * 1760

ydToin = FromValue * 36
ydToft = FromValue * 3
ydTomi = FromValue * 0.0005681818181818

ftToin = FromValue * 12
ftToyd = FromValue * 0.3333333333
ftTomi = FromValue * 0.0001893939393939

inToft = FromValue * 0.08333333333333
inToyd = FromValue * 0.02777777777778
inTomi = FromValue * 0.00001578282828283

inToin = FromValue * 1
ftToft = FromValue * 1
ydToyd = FromValue * 1
miTomi = FromValue * 1

if FromUnit == mi and ToUnit == inch:
    print(round(miToin,7), "in")
elif FromUnit == mi and ToUnit == ft:
    print(round(miToft,7), "ft")
elif FromUnit == mi and ToUnit == yd:
    print(round(miToyd,7), "yd")
elif FromUnit == mi and ToUnit == mi:
    print(round(miTomi,7), "mi")
elif FromUnit == ft and ToUnit == inch:
    print(round(ftToin,7), "in")
elif FromUnit == ft and ToUnit == ft:
    print(round(ftToft,7), "ft")
elif FromUnit == ft and ToUnit == yd:
    print(round(ftToyd,7), "yd")
elif FromUnit == ft and ToUnit == mi:
    print(round(ftTomi,7), "mi")
elif FromUnit == yd and ToUnit == inch:
    print(round(ydToin,7), "in")
elif FromUnit == yd and ToUnit == ft:
    print(round(ydToft,7), "ft")
elif FromUnit == yd and ToUnit == yd:
    print(round(ydToyd,7), "yd")
elif FromUnit == yd and ToUnit == mi:
    print(round(ydTomi,7), "mi")
elif FromUnit == inch and ToUnit == inch:
    print(round(inToin,7), "in")
elif FromUnit == inch and ToUnit == ft:
    print(round(inToft,7), "ft")
elif FromUnit == inch and ToUnit == yd:
    print(round(inToyd,7), "yd")
elif FromUnit == inch and ToUnit == mi:
    print(round(inTomi,7), "mi")
