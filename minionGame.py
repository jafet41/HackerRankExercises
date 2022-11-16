def count1(strA,subS):
    count=0
    lenSubS=len(subS)
    for i in range(len(strA)):
        tmp=strA[i:]
        if tmp[:lenSubS]==subS:
            count+=1
    return count

def minion_game(string):
    # your code goes here
    if (not string.isupper()):
        print("Only capital letters accepted")
        return

    vowels = ['A','E','I','O','U']
    stuartScore=0
    kevinScore=0
    #Calculating the Scores
    toSkip=[]
    totalSubs=0
    for x in range(len(string)):
        for y in range(x+1, len(string)+1):
            subString=string[x:y]
            if subString[0] in vowels:
                if count1(string, subString)>1 and subString not in toSkip:
                    toSkip.append(subString)
                    kevinScore+=count1(string, subString)
                elif count1(string, subString)==1:
                    kevinScore+=count1(string, subString)
                elif subString in toSkip:
                    continue
                totalSubs+=1
            else:
                if count1(string, subString)>1 and subString not in toSkip:
                    toSkip.append(subString)
                    stuartScore+=count1(string, subString)
                elif count1(string, subString)==1:
                    stuartScore+=count1(string, subString)
                elif subString in toSkip:
                    continue
                totalSubs+=1

    #Getting the winner (if any)
    if stuartScore > kevinScore:
        print("Stuart "+str(stuartScore))
    elif kevinScore >stuartScore:
        print("Kevin "+str(kevinScore))
    elif kevinScore==stuartScore:
        print("Draw")


if __name__ == '__main__':
    s = input()
    minion_game(s)