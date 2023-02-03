def computeSecond(records):
    grades=[records[x][1] for x in range(len(records))]
    names=[records[x][0] for x in range(len(records))]
    tuples=list(zip(names,grades))
    sortedTuple=sorted(tuples,key=lambda x:x[1])
    minGrade=sortedTuple[0][1]
    seconds=[]
    flag=True
    for n in range(len(sortedTuple)):
        if sortedTuple[n][1]>minGrade:
            if flag:
                secondGrade=sortedTuple[n][1]
                flag=False
            if (not seconds) or (secondGrade==sortedTuple[n][1]):
                seconds.append(sortedTuple[n][0])
    seconds.sort()
    return seconds

if __name__ == '__main__':
    records=[]
    for i in range(int(input())):
        name = input()
        score = float(input())
        records.append([name,score])
    output=computeSecond(records)
    for x in range(len(output)):
        print(output[x])