import math
class Stack:
    def __init__(self) -> None:
        self.list = []
    
    def push(self,data):
        self.list.append(data)
    
    def pop(self):
        return self.list.pop()
    
    def __len__(self):
        return len(self.list)
        
    def peek(self):
        return self.list[-1]
    def __str__(self):
        return f'{self.list}'

list = [4,0,5,0,1,9,0,0]
# stack = Stack()
# for i in list:
#     if i != 0 :
#         stack.push(i)

# print(stack,len(stack),len(list))
# zeros = (len(list)-len(stack))
# list[len(stack):] = [0]*(zeros)    

# for i in range(len(stack)-1,-1,-1):
#     list[i] = stack.pop()

# print(list,stack,len(stack),len(list))

# number = []

# for i in list:
#     if i>0:
#         number.append(i)
# list = number + [0]*(len(list)-len(number))
# print(list)

number = 0
for i in list:
    if i > 0:
        number = number*10 + i
print(number)
digit = int(math.log10(number)) + 1

i = 1
while number !=0:
    list[digit - i] = number % 10
    number //=10
    i+=1
list[digit:] = [0] *(len(list) - digit)

print(list)
     