def perform(a,b,op):
    match op:
        case '**' : return a**b 
        case '//' : return a//b 
        case '*' : return a*b 
        case '+' : return a+b 
        case '-' : return a-b 
        case _ : return None
        
expression = input()
op_list = ['//','**','*','/','+','-']
op = None
for i in op_list:
    ls = expression.split(i)
    if len(ls) == 2:
        op = i
        break
else:
    print('Invalid expression')

print(perform(float(ls[0]),float(ls[1]),op))

