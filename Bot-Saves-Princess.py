
def nextMove(n,r,c,grid):
    for x in range(n):
        for y in range(n):
            if(grid[x][y]=='p'):
                xP=y
                yP=x
                break
    #print("xP:",xP)
    #print("yP:",yP)
    diff_X=xP-c
    diff_Y=yP-r
    #print("diff_X:",diff_X)
    #print("diff_Y:",diff_Y)
    if abs(diff_X)>abs(diff_Y) and diff_X<0:
        return "LEFT"
    elif abs(diff_X)>abs(diff_Y) and diff_X>0:
        return "RIGHT"
    elif abs(diff_Y)>abs(diff_X) and diff_Y<0:
        return "UP"
    elif abs(diff_Y)>abs(diff_X) and diff_Y>0:
        return "DOWN"
    elif abs(diff_X)==abs(diff_Y) and diff_X<0:
        return "LEFT"
    elif abs(diff_X)==abs(diff_Y) and diff_X>0:
        return "RIGHT"


n = int(input())
r,c = [int(i) for i in input().strip().split()]
grid = []
for i in range(0, n):
    grid.append(input())

print(nextMove(n,r,c,grid))