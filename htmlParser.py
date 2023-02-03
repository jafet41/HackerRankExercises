import re

def myParser(myList):
    starts=list()
    ends=list()
    empties=list()

    pattStart="<[^/^>]+>"
    pattEnd="<\/.*?>"
    pattEmpty="<\s*([^\s>]+)([^>]*)\/\s*>"
    for n in range(len(myList)):
        for x in re.findall(pattStart, myList[n]):
            starts.append(x)
        for y in re.findall(pattEnd, myList[n]):
            ends.append(y)
        for z in re.findall(pattEmpty, myList[n]):
            empties.append(z)

    print("Starts: ", starts)
    print("Ends: ", ends)
    print("Empties: ", empties)

if __name__=='__main__':
    n=int(input())
    l=[]
    for i in range(n):
        newLine=input()
        l.append(newLine)
    print(l)
    myParser(l)