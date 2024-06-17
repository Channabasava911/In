# oops
# class sum:
#     def __init__(self,a,b):
#        self.a=a
#        self.b=b
#     def add(self):
#         self.sum=self.a+self.b
#         self.mul=self.a*self.b
#         self.div=self.a//self.b
#         self.mod=self.a%self.b
#     def display(self):
#         print(self.sum)
#         print(self.mul)
#         print(self.div)
#         print(self.mod)
         
# object creation
# s=sum(6,5)
# s.add()
# s.display()

# class team1:
#     def __init__(self,a,b):
#         self.a1=a
#         self.b1=b
#     def strength(self):
#         self.s=10
#     def kn(self,c,d):
#         self.know="win"
#         score=c+d
#         print(score)
#     def details(self):
#         cs=self.s-10
#         print(cs,self.know)
        
# t=team1(2,1)
# t.strength()
# t.kn(1,2)
# t.details()

# single level inheritance
# class A:
#     def read(self,a,b):
#         self.a=a
#         self.b=b
#     def dis(self):
#         self.sum=self.a+self.b
# class B(A):
#     def mul(self):
#         self.m=self.sum*10
#         print(self.m)
# ob=B()
# ob.read(1,2)
# ob.dis()
# ob.mul()

# multilevel inheritance
# class A:
#     def read(self,a,b):
#         self.a=a
#         self.b=b
#     def dis(self):
#         self.sum=self.a+self.b
# class B(A):
#     def mul(self):
#         self.m=self.sum*10
#         print(self.m)
# class C(B):
#     def op(self):
#         self.operate=self.m+1
#         print(self.operate)
# o1=C()
# o1.read(1,2)
# o1.dis()
# o1.mul()
# o1.op()

# multiple inheritance
# class A:
#     def read(self,a,b):
#         self.a=a
#         self.b=b
#     def dis(self):
#         self.sum=self.a+self.b
# class B(A):
#     def mul(self):
#         self.m=self.sum*10
#         print(self.m)
# class C(B,A):
#     def kn(self):
#         self.l=self.m+2
#         print(self.l)
    
# o2=C()
# o2.read(1,2)
# o2.dis()
# o2.mul()
# o2.kn()

# hierarchial inheritance
# class A:
#     def read(self,a,b):
#         self.a=a
#         self.b=b
#     def dis(self):
#         self.sum=self.a+self.b
# class B(A):
#     def mul(self):
#         self.m=self.sum*10
#         print(self.m)
# class C(A):
#     def kn(self):
#         self.l=self.sum+3
#         print(self.l)
    
# o3=C()
# o3.read(1,2)
# o3.dis()
# o3.kn()

# o4=B()
# o4.read(3,4)
# o4.dis()
# o4.mul()

            
            
            
        
            
    

        
    
        


    
