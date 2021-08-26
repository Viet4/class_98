def countWords ():
    giveFile = input("Enter the file name: ")
    numberOfWords = 0
    fileName = open(giveFile, 'r')
    for lines in fileName:
        words = lines.split()
        numberOfWords = numberOfWords + len(words)
    print(numberOfWords)

countWords()
    