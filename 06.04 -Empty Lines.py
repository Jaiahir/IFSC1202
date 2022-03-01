fileread = "06.04 EmptyLinesInput.txt"
filewrite = "06.04 EmptyLinesOutput.txt"
file = open(filewrite,"w")

recordcount=0
writtencount=0

with open(fileread,"r") as f:
    for line in f:
        recordcount+=1
        if line.strip():
            writtencount+=1
            file.write(line)
file.close()
print(recordcount,"records read")
print(writtencount,"records written")