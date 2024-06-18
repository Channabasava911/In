# input: n=5
# a=5 4 1 3 2
# [1, 2, 3, 4, 5]
# output:6

# n=int(input())
# ans=0
# a=list(map(int,input().split()))
# a.sort()
# print(a)
# i=0
# j=len(a)-1
# while i<=j:
#     dif=abs(a[j]-a[i])
#     ans=ans+dif
#     i=i+1
#     j=j-1
       
# print(ans)


# input:5
# output:1 1 1
# 1
# n=int(input())
# count=0
# f=0
# for a in range(1,n):
#     for b in range(1,n):
#         for c in range(1,n):
#             if a**2+b**2+a*b+b*c+c*a==n:
#                 print(a,b,c)
#                 f=1
#                 count=count+1
                

# print(count)
# if f==0:
#     print("Not possible")


# input:1010000
# output:1019002
# n=1010000
# ans=0
# c=1000
# sum=0
# k=1 #no of commas
# while c<n:
#     m=c*1000
#     num=min(n-c+1,m-c)
#     ans=ans+num*k
#     c=m
#     k=k+1
# print(ans)


# input:a="abcd"
        #s="xyz"
# output:86
# a="abcd"
# s="xyz"
# dif=0
# min=999
# ans=0
# for i in a:
#     for j in s:
#         dif=ord(j)-ord(i)
#         if min>dif:
#             min=dif
#             ans=ans+min
# print(ans)


    
    

             
    