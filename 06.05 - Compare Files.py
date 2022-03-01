fileA = open("06.05 CompareFileA.txt","r").readlines()
fileB = open("06.05 CompareFileB.txt","r").readlines()

difflines = 0

for i in range(len(fileA)):
    wordsA = fileA[i]
    wordsB = fileB[i]
    
    if wordsA != wordsB:
        print("Line: {} - File A: {}".format(i+1, wordsA))
        print("Line: {} - File B: {}".format(i+1, wordsB))
        difflines += 1
        
print("{} differences".format(difflines))