newfile = open("newfile.txt", "w+")

string = "This is the content that will be written to the text file."

newfile.write(string)
newfile.close()

readfile = open("newfile.txt", "r")
getStr1 = readfile.readline(10)
getStr2 = readfile.readline()
print("content :", getStr1)
print("content :", getStr2)
readfile.close()