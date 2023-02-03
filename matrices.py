#A=[[5,8,12],[1,10,9],[8,2,32]]

# A=[[] for i in range(3)]
# print(A)
# for i in range(3):
#     if i==0:
#         A[i]=[5,8,12]
#     elif i==1:
#         A[i]=[1,10,9]
#     elif i==2:
#         A[i]=[8,2,32]
#     for j in range(3):
#         print(A[i][j], end=" ")
#     print("")

A=[]
print(A)
for i in range(3):
    if i==0:
        A.append([5,8,12])
    elif i==1:
        A.append([1,10,9])
    elif i==2:
        A.append([8,2,32])
    for j in range(3):
        print(A[i][j], end=" ")
    print("")

print("===============")
print(A)