import re
def minion_game(string):
    # your code goes here
    if (not string.isupper()):
        print("Only capital letters accepted")
        return
    if len(string)>1000000:
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
            subRE='(?='+subString+')'
            countSub=len(re.findall(subRE,subString))
            if subString[0] in vowels:
                if countSub>1 and subString not in toSkip:
                    toSkip.append(subString)
                    kevinScore+=countSub
                elif countSub==1:
                    kevinScore+=countSub
            else:
                if countSub>1 and subString not in toSkip:
                    toSkip.append(subString)
                    stuartScore+=countSub
                elif countSub==1:
                    stuartScore+=countSub

    #Getting the winner (if any)
    if stuartScore > kevinScore:
        print("Stuart "+str(stuartScore))
    elif kevinScore >stuartScore:
        print("Kevin "+str(kevinScore))
    elif kevinScore==stuartScore:
        print("Draw")

if __name__ == '__main__':
    s = input()
    import time
    start_time = time.time()
    minion_game(s)
    print("--- %s seconds ---" % (time.time() - start_time))