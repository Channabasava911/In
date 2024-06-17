# input[14,2,16,4,3,5]
# output[16,16,-1,5,5,-1]

l=[14,2,16,4,3,5]
top=-1
for i in l:
    if(top==-1):
        ans=-1
    elif(top>l[i]):
        ans=top
    elif(top<l[i]):
        l[i].pop()
print(ans)

        