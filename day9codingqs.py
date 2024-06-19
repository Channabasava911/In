# pattern
# rows=int(input())  #4
# ans=0
# for i in range(2,rows+1): #2,3,4
#     n=i  #2,3,4
#     while n>1: #2 3 4
#         ans+=2*n #2*2=4 #4+2*3 #4+2*3+2*2=14 #14+2*4 
#         n=n-1 #1 2
# ans+=rows  #36
# print(ans)

# best grade
# s=input()
# p=int(input())
# k=int(input())
# s1=list(s)
# st=0
# end=len(s1)
# mini=999
# if abs(p-k-1)>=0:
#     st=abs(p-k-1)
# if p+k<len(s1):
#     end=p+k
# print(st,end)
# for i in range(st,end):
#     mini=min(ord)

# input:2 3 1 4
# output:5
# x,n,y,m=map(int,input().split())
# time=max(x,y)
# while True:
#     if time>=x and (time-x)%n==0 and time>=y and (time-y)%m==0:
#         print(time)
#         break
#     time+=1

# Generated numbers
# input: 10 3 5
# output:6
# n=10
# a=3
# b=5

# a1=n//a
# b1=n//b
# c=0

# for i in range(0,a1+1):
#     for j in range(b1+1):
#         if i*a+j*b<10:
#             c+=1
# print(c)


# s=input()
# s=s[::-1]
# print(*s,sep="")

# s=input()
# print(s[::-1])

# s=input()
# l=list(s)

# i=0
# j=len(l)-1
# while i<=j:
#     temp=l[i]
#     l[i]=l[j]
#     l[j]=temp
#     i=i+1
#     j=j-1
# print(''.join(l))


# 333222111
# 332211
# 321
# for i in range(3,0,-1):
#     for j in range(3,0,-1):
#         k=i
#         while k>0:
#             print(j,end="")
#             k=k-1
#     print()

# input:50 66 23
# output:23
# a=list(map(int,input().split()))
# mini=999
# for i in a:
#     if i<mini:
#         mini=i
# print(mini)



#   *
#  **
# ***
# ***
#  **
#   *
for i in range(1,4):
    for s in range(1,3-i+1):
        print(" ",end="")
    for j in range(1,i+1):
        print("*",end="")
    print()
for i in range(3,0,-1):
    for s in range(0,3-i):
        print(" ",end="")
    for j in range(1,i+1):
        print("*",end="")
    print()
    
            
    
    
    


    