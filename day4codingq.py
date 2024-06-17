# 6.No of times ant reaches initial position from destination
# input:no of moves:5
#       1 -1 1 -1 1
# output:2 times
# steps=int(input())
# a=list(map(int,input().split()))
# sp=0
# ans=0
# for i in a:
#     sp=sp+i
#     if sp==0:
#         ans=ans+1
# print(ans)

# 7. total chocolates picked by student A
# input:jars of chocolates=10 20 30
# output:total chocolates picked by student A=21

# jars=list(map(int,input().split()))
# n=int(input())
# div=0
# for i in jars:
#     div=div+(i//3)
#     # 3
#     if(i%3==2 or i%3==1):
#         div=div+1
# print(div)
    
    
# 8.dogs age
# input:an integer n representing age of dog:4
# output:return an integer value representing age of dog in human years
# note:1 dog year=7 human years
# d=int(input())
# print(d*7)

# 9:problems in  a diwali party
# first approach
# problems=int(input())
# tot=int(input())
# c=0
# s=0
# rt=4*60-tot
# for i in range(1,problems+1):
#     s=s+5*i
#     if s>rt:
#         break
#     c=c+1
# print(c)

# second approach
# problems=int(input())
# tot=int(input())
# s=0
# c=0
# rt=4*60-tot
# for i in range(1,problems+1):
#     if s<rt:
#         s=s+5*i
#         c=c+1
# print(c)

# 10.basketball 
# input:number of shots=5
# an integer k represents size of subarray:2
# an array of integers:[1,2,3,4,5]
# output:continuous maximum subarray:14

# in1=int(input())
# in2=int(input())
# a=list(map(int,input().split()))
# max=-1
# for i in range(0,len(a)-in2+1):
#     temp=a[i:i+2]
#     k,s=1,0
#     # s is for sum
#     for j in temp:
#         s=s+(j*k)
#         k=k+1
#     if s>max:
#         max=s
# print(s)

# 11.counting number of spaces
# str="Hello world hey"
# approach 1:
# print(str.count(" "))

# approach 2:
# count=0
# for i in str:
#     if i==' ':
#         count=count+1
# print(count)

# approach 3:
# str="Hello world hey"
# o=str.split(" ")
# n=len(o)-1
# print(n)

# 11.Encode a number
# input:167
# output:13649
# n=int(input())
# # n=167
# # sod
# def sod(n):
#     c=0
#     while n>0:
#         c=c+1
#         n=n//10
#     return c
# def rev(n):
#     ans=0
#     while  n>0: #167,16,1
#         digit=n%10 #7,6,1
#         sq=digit**2 #49,36,1
#         sod_sq=sod(sq)#2,2,1
#         ans=ans*(10**sod_sq)+sq #4936x(10**1)+1=49361
#         n=n//10#16,1,0
#     return ans
# ans=rev(n)

# def rev2(n):
#     ans2=0
#     while n>0:
#         digit=n%10
#         ans2=ans2*10+digit
#         n=n//10
#     return ans2
# print(rev2(ans))

# arduino program
# input: 1 -2 3 4
# output:6 sum of elements

# input:1 2 6 -5
# output:9
n=list(map(int,input().split()))
# print(sum(n))
sum=0
maxi=-1
for i in n:
    sum=sum+i
    if sum>maxi:
        maxi=sum
print(maxi)
    
    
    

    





    
    

    