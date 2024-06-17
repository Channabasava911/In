# one
# sample input-1:
#  total size of array=6
# values in an array=1 1 2 2 2 3
# output:2 count of 2 is greater than 1

# sample input-2:
#  total size of array=6
# values in an array=1 1 2 2 2 2
# output:-1 because of same no of votes


# n=int(input())
# arr=list(map(int,input().split()))
# d={}
# if n==1:
#     print(arr[0])
# else:
#     for i in arr:
#         if i in d:
#             d[i]+=1
#         else:
#             d[i]=1
# ans=-1
# vals=list(d.items())
# print(vals)
# vals.sort(reverse=True,key=lambda x:x[1]) 
# print(vals)
# if(len(vals)==1):
#     ans=vals[0][0]
# else:
#     if vals[0][1]==vals[1][1]:
#         ans=-1
#     else:
#         ans=vals[0][0]
# print(ans)       

# two
# ip:an integer value N:6 
# output:7

# def isprime(no):
#     for i in range(2,(int)(no**0.5)+1):
#         if(no%i==0):
#             return False
#     return True
# num=int(input())
# k=num+1

# while True:
#     if isprime(k):
#         print(k)
#         break
#     k=k+1

# three
# input:6 28 66 120 190 270
# output:378
# n=6
# k=22
# for i in range(1,7):
#     print(n)
#     n=n+k
#     k=k+16

# a=2
# b=3
# for i in range(1,7):
#     n=a*b
#     print(n)
#     a=a+2
#     b=b+4
 
    
# def next_greater(arr):
#     n=len(arr)
#     ans=[0]*n
#     stack=[-1]
#     for i in range(n-1,-1,-1):
#         cur=arr[i]
#         while stack.top()!=-1 and stack.top()>=cur:
#             stack.pop()
#         ans[i]=stack.pop()
#         stack.append(cur)
#     return ans
# arr=[14,2,16,4,3,5]
# print(next_greater(arr))
    
        



