# input: row:4
#        column:4
# output:
# * * * * 
# *     * 
# *     * 
# * * * * 

# def pat(row,col):
#     for i in range(1,row+1):
#         for j in range(1,col+1):
#             if i==1 or i==row or j==1 or j==col:
#                 print("*",end=" ")
#             else:
#                 print(" ",end=" ")
#         print()
        
# row=int(input())
# col=int(input())
# pat(row,col) 


#       * 
#     * * * 
#   * * * * * 
# * * * * * * * 
# for i in range(0,4):
#     for s in range(0,4-i-1):
#         print(" ",end=" ")
#     for j in range(0,2*i+1):
#         print("*",end=" ")
#     print()
    
    
# for i in range(1,4):
#     for s in range(1,4-i-1):
#         print(" ",end=" ")
#     for j in range(1,2*i+1):
#         k=1
#         print(k,end=" ")
#         k=k+1
#     print()


#input: 5
# output:
#     1
#    212
#   32123
#  4321234
# 543212345
def pyr(n):
    for i in range(1,n+1):
        print(" "*(n-i),end="")
        for j in range(i,0,-1):
            print(j,end="")
        for j in range(2,i+1):
            print(j,end="")
        print()
num=int(input())
pyr(num)
        


