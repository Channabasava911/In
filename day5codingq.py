# minimum sum of array
# l=[1,2,3,4,5]
# max1=-1
# max2=-1
# for i in l:
#     if i>max1:
#         max1=i
# for i in l:
#     if i>max2 and i!=max1:
#         max2=i
# # print(max1)
# # print(max2)
# avg=(max1+max2)/2
# ans=0
# for i in l:
#     if i>avg:
#         ans=ans+i
# print(ans)

# tossing a coin
# input:'HHHTT'
# output:
# s=input()
# hc=0
# tc=0
# score=0
# for i in s:
#     if i=='H' or i=='h':
#         tc=0 #for continuous 3 heads count of tc=0
#         hc=hc+1
#         score=score+2
#         if(hc==3):
#             break
#     else:
#         hc=0
#         tc=tc+1
#         score=score-1
#         if(tc==3):
#             break
# print(score)
    
# usage of modules  
# def p():
#     print("hello module")
# from day5codingq import p
# p()

# 16.finding missing and repeated element in a 2d array
#  to take input in 2d array: list into array of row and converting into 2d array
# a=[]
# r=3
# c=3
# for i in range(0,r):
#     sub=[]
#     print("Enter values of row ",i)
#     for j in range(0,c):
#         print("Enter values of column ",j)
#         ele=int(input())
#         sub.append(ele)
#         print(sub)
#     a.append(sub)
#     print(a)

# d={}
# ans=[]
# for i in range(0,r):
#     for j in range(0,c):
#         if a[i][j] not in d:
#             d[a[i][j]]=1
#         else:
#             d[a[i][j]]+=1
#             if d[a[i][j]]==2:
#                 ans.append(a[i][j])
# print(d)
# for i in range(1,r**2+1):
#     if i not in d:
#         ans.append(i)
# print(d)
# print(ans)

# 17.sum of encrypted integers
def process(n):
    #maximum and count
    max=-999
    c=0
    ans=0
    while n>0:
        dig=n%10
        if dig>max:
            max=dig
        c=c+1
        n=n//10
    # arrange
    while c>0:
        ans=ans*10+max
        c=c-1
a=list(map(int,input().split()))
    


    