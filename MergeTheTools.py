def merge_the_tools(string, k):
    # your code goes here
    n=len(string)
    l=n/k
    output=''
    ini=0
    while ini<n:
        for i in range(k):
            x=string[i+ini]
            if x in string[ini:(ini+i)]:
                continue
            else:
                output+=x
        print(output)
        ini+=k
        output=''
    return

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)