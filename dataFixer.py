##parse and format data from Open Source Shakespeare so it can be directly fed into DL algorithm

def parseBetter():
    lines = []
    with open("./data/Paragraphs - Copy.txt", "r") as f:
        all = f.read()
        foundTill = False
        category = 0
        curLine = ""
        for ch in all:
            if category == 5:
                curLine = ""
            if category == 6:
                curLine = curLine + ch
            if ch == "~":
                if not foundTill:
                    foundTill = True
                else:
                    category += 1
                    foundTill = False
                if category == 7:
                    lines.append(curLine)
            if (category >= 1 and category <= 3) or (category >= 9 and category < 13):
                if ch == ",":
                    category += 1
            if category > 12:
                category = 0
    return lines


def parseData(): #only take lines of paragraphs without other extraneous data
    lines = []
    with open("./data/Paragraphs.txt", "r") as file:
        originalFile = file.read()
        lineStarted = False
        curLine = ""
        for i in range(3, len(originalFile)-1):
            if originalFile[i-3] + originalFile[i-2] + originalFile[i-1] == "[p]" or originalFile[i-1] == "~":
                curLine = ""
                lineStarted = True
            if lineStarted and (originalFile[i] == "\n" or originalFile[i] == "~") and not curLine.isupper() and curLine != "" and check(curLine):
                lines.append(curLine)
                curLine = ""
                lineStarted = False
            elif lineStarted:
                curLine = curLine + originalFile[i]
    return lines

def check(line):
    for ch in line:
        if not (ch.isdigit() or ch == ","):
            return True
    return False

with open("./data/formatParagraphs.txt", "w") as file:
    file.write(str(parseBetter()))