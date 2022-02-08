FromValue = float(input("Enter From Value: "))
FromUnit = str(input("Enter From Unit (in, ft, yd, mi): "))
ToUnit = str(input("Enter To Unit (in, ft, yd, mi): "))

miToin = FromUnit * 63360
miToft = FromUnit * 5280
miToyd = FromUnit * 1760

ydToin = FromUnit * 36
ydToft = FromUnit * 3
ydTomi = FromUnit * 0.0005681818181818

ftToin = FromUnit * 12
ftToyd = FromUnit * 0.3333333333
ftTomi = FromUnit * 0.0001893939393939

inToft = FromUnit * 0.08333333333333
inToyd = FromUnit * 0.02777777777778
inTomi = FromUnit * 0.00001578282828283

inToin = FromUnit * 1
ftToft = FromUnit * 1
ydToyd = FromUnit * 1
miTomi = FromUnit * 1

if FromUnit == mi and ToUnit == in:
    print(miToin)