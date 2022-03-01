file = open("06.03 FTemps.txt", "r")

def FahrToCel(C):
    C = (float(F) - 32)*5/9 
    C = round(C,1)
    return C

recordcount = 0

for F in file:
    C = (float(F) - 32)*5/9 
    C = round(C,1)
    file = open("06.03 CTemps.txt", "a") 
    file.write(str(FahrToCel(C))) 
    file.write('\n')
    file.close()
    recordcount = recordcount + 1
    
print(str(recordcount)+" records written")

