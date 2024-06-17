# # armstrong number
# one
# no=int(input("Enter no"))
# revno=no
# num=str(no)
# lengt=len(num) 
# sum=0
# no=int(num)
# while(no!=0):
#     rem=no%10
#     sum=sum+pow(rem,lengt)
#     no=no//10
# if(sum==revno):
#     print("Armstrong")
# else:
#     print("Not a armstrong")
    
# two
# no=int(input("Enter a number"))
# revno=no
# org=revno
# count=0
# sum=0
# while(no>0):
#     count=count+1
#     no=no//10
# #no=0
# while(revno!=0):
#     rem=revno%10
#     p=rem**count
#     sum=sum+p
#     revno=revno//10
# if(sum==org):
#     print("Armstrong")
# else:
#     print("Not a armstrong")

#disarum number
# no=int(input("Enter a number"))
# revno=no
# org=revno
# count=0
# sum=0
# while(no>0):
#     count=count+1
#     no=no//10
# #no=0
# while(revno!=0):
#     rem=revno%10
#     p=rem**count
#     count=count-1
#     sum=sum+p
#     revno=revno//10
    
# if(sum==org):
#     print("Disarum")
# else:
#     print("Not a disarum")

# n=int(input("Enter no of rows:"))
# for i in range(n):
#     for j in range(n):
#         if(i==0 or j==0 or j==n-1 or i==n-1):
#             print("*",end="")
#         else:
#             print("")
#     print("\n")

#chessboard
# e_r="2468"
# o_r="1357"

# e_c="bdfh"
# o_c="aceg"

# s="a1"
# if s[0] in e_c:
#     if s[1] in e_r:
#         print("black")
#     else:
#         print("white")
# else:
#     if s[1] in e_r:
#         print("white")
#     else:
#         print("black")

# identifying defective chocolate for a prisoner,they are arranged in circular
# no=int(input("Enter no of prisoners:"))
# s=int(input("Enter starting point:"))
# c=int(input("Enter no of chocolates:"))
# last=(s+c-1)%no
# if(last==0):
#     last=no
# print(last)

    
# register()

# def loginregister():
#     d={}
#     print("Welcome to Registrattion")
#     uname=input("Enter username:")
#     passd=input("Enter password:")
#     name=input("Enter name:")
#     pno=input("Enter phonenumber:")
    
#     d[uname]=passd
#     while True:
#         print("Welcome to login")
#         lname=input("Enter login username:")
#         lpassd=input("Enter login password:")
#     #if user exists or not
#         if lname in d:
#             if(d[lname]==lpassd):
#                 print("login success")
#                 break
#             else:
#                 print("Invalid credentials")
#         else:
#             print("user not found")
            
# loginregister()


# input:[4,0,5,0,1,9,0,0]
# output:[4, 5, 1, 9, 0, 0, 0, 0]
# l=[4,0,5,0,1,9,0,0]
# n=8
# i=0
# j=0
# for i in range(n):
#     if(l[i]!=0):
#         l[j]=l[i]
#         j=j+1
# while(j<n):
#     l[j]=0
#     j=j+1
# print(l)

# def power(x,n):
#     if(n==0):
#         return 1
#     return x * power(x,n-1)
# print(power(3,3))

#Maximum repeating frequency of a vowel in a string and returning a specific vowel
# str="helloworld"
# max=0
# vowel=''
# count=0
# for i in ['a','e','i','o','u']:
#     for j in str:
#         if j==i:
#             count=count+1
#     if(max<count):
#         vowel=i
#         max=count
# print(vowel)

# input:[2,1,0,1,1,2,0,0]
# output:[0,0,0,1,1,1,2,2]
# zero-one-two-sort
# l=[2,1,0,1,1,2,0,0]
# c_0=0
# c_1=0
# c_2=0

# for i in range(len(l)):
#     if(l[i]==0):
#         c_0=c_0+1
#     elif(l[i]==1):
#         c_1=c_1+1
#     else:
#         c_2=c_2+1
# j=0
# while c_0>0:
#     l[j]=0
#     j=j+1
#     c_0=c_0-1

# while c_1>0:
#     l[j]=1
#     j=j+1
#     c_1=c_1-1

# while c_2>0:
#     l[j]=2
#     j=j+1
#     c_2=c_2-1
# print(l)
    
        