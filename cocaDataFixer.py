##coca-sample data formatter

def parseData(): #only take lines of text without other extraneous data
    formattedLines = []
    with open("./data/text_fic.txt", "r") as file:
        originalFile = file.read()
        lineStarted = False
        isNum = False
        curLine = ""
        for i in range(3, len(originalFile)-1):
            curCh = originalFile[i]
            if curCh == "@" or isNum:
                isNum = originalFile[i+1].isdigit()
            else:
                if (originalFile[i-3] + originalFile[i-2] + originalFile[i-1] == "<p>"):
                    if lineStarted:
                        formattedLines.append(curLine[:-4])
                        lineStarted = False
                    else:
                        lineStarted = True
                    curLine = ""
                elif lineStarted:
                    curLine = curLine + originalFile[i]
    return formattedLines

with open("./data/adversFormatParagraphs.txt", "w") as file:
    file.write(str(parseData()))
