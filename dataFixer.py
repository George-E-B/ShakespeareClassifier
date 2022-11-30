##parse and format data from Open Source Shakespeare so it can be directly fed into DL algorithm

def parseData(): #only take lines of paragraphs without other extraneous data
    formattedLines = []
    with open("./data/Paragraphs.txt", "r") as file:
        originalFile = file.read()
        lineStarted = False
        curLine = ""
        for i in range(3, len(originalFile)):
            if originalFile[i-3] + originalFile[i-2] + originalFile[i-1] == "[p]":
                curLine = ""
                lineStarted = True
            if lineStarted and originalFile[i] == "\n":
                formattedLines.append(curLine)
                curLine = ""
                lineStarted = False
            elif lineStarted:
                curLine = curLine + originalFile[i]
    return formattedLines

with open("./data/formatParagraphs.txt", "w") as file:
    file.write(str(parseData()))