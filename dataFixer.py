##parse and format data from Open Source Shakespeare so it can be directly fed into DL algorithm

def parseData(): #only take lines of paragraphs without other extraneous data
    formattedLines = []
    with open("./data/tokenisedParagraphs.txt", "r") as file:
        originalFile = file.read()
        curLine = ""
        for i in range(0, len(originalFile)):
            if originalFile[i] == "\n" and curLine != "" and curLine != "\n":
                curLine = curLine.replace("\n","")
                formattedLines.append(curLine)
                curLine = ""
            curLine = curLine + originalFile[i]
    return formattedLines

with open("./data/formatParagraphs.txt", "w") as file:
    print(len(parseData()))
    file.write(str(parseData()))