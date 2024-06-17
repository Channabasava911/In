# # Maximum repeating frequency of a vowel in a string and returning a specific vowel
# s="helloworld"
# v="aeiou"
# ans=0
# coun=0
# max=-1
# d={}
# for i in s:
#     if i in v:
#         if i not in d:
#             d[i]=1
#         else:
#             d[i]=d[i]+1
#         if d[i]>max:
#             max=d[i]
#             ans=i
# print(d)
# print(ans)

# prime factors
# input:size of a=6
#       elements of a=11 21 32 45 1 23
#       prime factors for a number=6
# output:77
# Explanation:6=2**1 * 3**1
            #   sum=1*a[2]+1*a[3]=32+45=77

# def pf(n):
#     ans=[]
#     i=2
#     while i<=n:
#         if n%i==0:
#             ans.append(i)
#             n=n//i
#         else:
#             i=i+1
#     return ans
# ans=pf(6)
# s=0
# a=[11,21,32,45,1,23]
# for i in ans:
#     s=s+a[i]
# print(s)

# pizza party
# input: 100 17
# output:2  20=2+0=2
# one,two=map(int,input().split())
# ans=0
# while True:
#     if one%two==0:
#         ans=two
#         break
#     else:
#         two=two+1
# sum=0
# while(ans):
#     dig=ans%10
#     sum=sum+dig
#     ans=ans//10
# print(sum)

# finding equilibrium position index
# input:size=5
        # elements=2 4 3 2 7
        # array 1 based indexing
# output:3

# f=0
# a=[5,2,1,3,1,2,5]
# for i in range(0,len(a)):
#     i1=i
#     j=i+1
#     s1=0
#     s2=0
#     # left side
#     while i>=0:
#         s1=s1+a[i]
#         i=i-1
#     # right side
#     while j<len(a):
#         s2=s2+a[j]
#         j=j+1
#     if s1==s2:
#         print(i1+1)
#         f=1
#         break
# if f==0:
#     print(len(a)//2)


# finding index of a peak element
# input: size=5
        # 1 3 20 4 1
# output:2
# l=list(map(int,input().split()))
# max=-1
# for i in range(1,len(l)-1):
#     if l[i]>l[i-1] and l[i]>l[i+1]:
#         p=l[i]
#         if p>max:
#             max=p
#             ans=i
# print(ans)

# unique triplets
# input:7
        # 5 3 20 10 1 4 2
# output:3     (5,4,3),(20,3,1),(10,3,2)
# size=7
# c=0
# a=[5,3,20,10,1,4,2]
# tot=60
# for i in range(0,len(a)):
#     for j in range(i+1,len(a)):
#         for k in range(j+1,len(a)):
#             print("indexes:",i,j,k)
#             print("values:",a[i],a[j],a[k])
#             prod=a[i]*a[j]*a[k]
#             if prod==tot:
#                 print(prod)
#                 print()
#                 print("triplet",a[i],a[j],a[k])
#                 c=c+1
#                 print()
#         print()
# print(c)

# continuous max subarray sum 
# a=list(map(int,input().split()))
# cur_sum=0
# max_sum=0

# for i in a:
#     cur_sum=cur_sum+i
#     if cur_sum<0:
#         cur_sum=0
#     if cur_sum>max_sum:
#         max_sum=cur_sum
# print(max_sum)


# target sum
# input: 2 4 5 6
        # target=10
# output:[1,3]
# l=list(map(int,input().split()))
# t=int(input())
# l.sort()
# i=0
# j=len(l)-1
# ans=0
# while i<j:
#         cur_sum=l[i]+l[j]
#         if cur_sum==t:
#                 print(i,j)
#                 i+=1#checks for any other extra comnination
#                 j-=1
#         elif cur_sum<t:
#                 i=i+1
#         else:
#                 j=j-1

# minimum number of key presses
# total 11 keys: 0,1,2,3,4,5,6,7,8,9,00
# input:100
# output:2  (keys: 1 + 00)
        
# s=input()
# i=0
# c=0
# while i<len(s)-1:
#         if s[i]=="0" and s[i+1]=="0":
#             c+=1
#             i+=2
#         else:
#             c+=1
#             i+=1
# if i<len(s):
#     c+=1
# print(c)

# magic string
# input:aaabbbccdddd
# output:8  12-4=8

d={} 
max=-1
s=input()
for i in s:
    if i not in d:
        d[i]=1
    else:
        d[i]+=1
    if d[i]>max:
        max=d[i]
    
print(len(s)-max)
                


