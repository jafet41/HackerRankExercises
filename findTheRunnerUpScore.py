def getRunnerUp(arr1):
    winner=max(arr1)
    sorted_data=sorted(arr1,reverse=True)
    for x in range(len(sorted_data)):
        if sorted_data[x]<winner:
            runnerUp=sorted_data[x]
            return runnerUp
    return

if __name__ == '__main__':
    n = int(input())
    arr =list( map(int, input().split()) )
    print(getRunnerUp(arr))