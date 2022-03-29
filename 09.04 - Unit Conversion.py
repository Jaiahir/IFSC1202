def readfile(filename):
    file = open(filename, 'r') 
    lines = file.readlines()

    count = -1
    list = []
    c = 0

    words = []
    
    for l in lines:
        count += 1

    values = [[0.0 for i in range(count)] for j in range(count)]
    
    for l in lines:
        if c == 0:
            list = l.split()
        else:
            val = l.split()
            for i in range(len(val) - 1):
                values[c - 1][i] = float(val[i + 1])
        c += 1
    return list, values


def main():
    FromValue = float(input("Enter From Value: "))
    FromUnit = input("Enter From Unit (mm, cm, m, km, in, yd, mi): ")
    ToUnit = input("Enter To Unit (mm, cm, m, km, in, yd, mi): ")
    list, values = readfile("09.04 Conversion.txt")

    if FromUnit not in list:
        print("FromUnit is not valid")
    elif ToUnit not in list:
        print("ToUnit is not valid")
    else:
        fromunit_index = list.index(FromUnit)
        tounit_index = list.index(ToUnit)
        result = values[fromunit_index - 1][tounit_index - 1] * FromValue

        print(FromValue,"",FromUnit," => ",round(result, 7),"",ToUnit)

                
if __name__ == "__main__":
    main()