# Missing alphabets
#input: welcome to geeksforgeeks
#output: abdhijnpquvxyz
# s=input()
# s1="abcdefghijklmnopqrstuvwxyz"
# s2=""
# for i in s1:
#     if i not in s:
#         s2=s2+i
# print(s2)

# input:x=48 y=18
# output:6   because y=0 and x=6
# def process(x,y):
#     while y>0:
#         if x<y:
#             temp=x
#             x=y
#             y=temp
#         t=x-y
#         x=y
#         y=t
#     print(x)
                

# x=int(input())
# y=int(input())
# process(x,y)


# fellis function
# using recursion
# def f(n):
#     if n==0 or n==1:
#         return 1
#     else:
#         return (f(n-1)+7*f(n-2)+(n//4))%(10**9+7)

# n=int(input())
# print(f(n))

# iteration
# n=int(input())
# x=[1,1]
# for i in range(2,n+1):
#     ans=(x[i-1]+7*x[i-2]+(i//4))%(10**9+7)
#     x.append(ans)
# print(x[n])

# corner seat
# s=list(input().split())
# chair=input()
# # find index
# z=999
# c_ind=s.index(chair)

# # till c-index
# for i in range(0,c_ind):
#     if s[i]=='-':
#         if abs(c_ind-i)-1<z:
#             z=abs(c_ind-i)-1
            
# # right side
# for i in range(c_ind+1,len(s)):
#     if s[i]=='-':
#         if abs(i-c_ind)-1<z:
#             z=abs(i-c_ind)-1
# print(z)

# special fibonacci
# def f(n):
#     if n==0 or n==1:
#         return 1
#     else:
#         return (f(n-1)*f(n-1) +(n-2)*(n-2))%(47)

# n=int(input())
# print(f(n))

# iteration
# n=int(input())
# x=[1,1]
# for i in range(2,n+1):
#     ans=(x[i-1]*x[i-1]+(i-2)*(i-2))%47
#     x.append(ans)
# print(x[n])

# maximum product
# input:n=8,sum=18
# a=11 12 2 8 10 11 7 8
# output:80
# 10 8
# n=int(input())
# maxprod=-1
# a=list(map(int,input().split()))
# for i in range(0,len(a)):
#     for j in range(i+1,len(a)):
#         if a[i]+a[j]==18:
#             if a[i]>a[j]:
#                 prod=a[i]*a[j]
#                 if prod>maxprod:
#                     maxprod=prod
#                     c=a[i]
#                     d=a[j]                                             
# print(maxprod)
# print(c,d)

# bitterness
# n=3
# a=list(map(int,input().split()))
# b=list(map(int,input().split()))
# mini=999
# for i in range(len(a)):
#     if a[i]+b[i]<mini:
#         mini=a[i]+b[i]
    
# print(mini)   

# 2nd approach
# a1=list(map(int,input().split()))
# a2=list(map(int,input().split()))
# n=[]
# for i in range(0,len(a1)):
#     sm=a1[i]+a2[i]
#     n.append(sm)
# print(min(n))
     
# input:1 2 3 4 5
# output: [13, 9, 3, 5, 15]
a=list(map(int,input().split()))
ts=0
cs=0
ls=0
rs=0
ans=[]
for i in a:
    ts+=i

# left right diff
for i in a:
    ls+=i
    rs=ts-ls
    cs=abs(rs-ls)
    ans.append(cs)
    
print(ans)
        
        
    
    



    