
class carshowroom:
    def __init__(self):
        self.cgst=1000
        self.sgst=1000
    def carcompany(self):
        while True:
            # print("*"*15)
            print("Choose the carcompany from the below:")
            print("1.Mercedes")
            print("2.Toyota")
            carc=input("What do you want to choose?")
            self.selectmodel(carc)
            
            
    def selectmodel(self,carc):
        while True:
            if(carc=="mercedes"):
                print("*****Welcome to Mercedes*****")
                print("Choose the model of company:")
                print("1.amg")
                print("2.pw")
                mod1=input("What do you want to choose?")
                while True:
                    if(mod1=="amg"):
                        while True:
                            print("1.petrol")
                            print("2.diesel")
                            var1=int(input("Select the variant of model:"))
                            if(var1==1):
                                self.price(var1,mod1)
                                break
                            elif(var1==2):
                                self.price(var1,mod1)
                                break
                            else:
                                print("Invalid! please enter valid variant")
                                continue
                            break
                        break
                        
                    elif(mod1=="pw"):
                        while True:
                            print("1.petrol")
                            print("2.diesel")
                            var1=int(input("Select the variant of model:"))
                            if(var1==1):
                                self.price(var1,mod1)
                                break
                            elif(var1==2):
                                self.price(var1,mod1)
                                break
                            else:
                                print("Invalid! please enter valid variant")
                                continue
                            break
                        break
                            
                    else:
                        print("Invalid! please enter valid model")
                        break
                    continue
        
            elif(carc=="toyota"):
                print("*****Welcome to Toyota*****")
                print("Choose the model of company:")
                print("1.Fortuner")
                print("2.LC")
                mod1=input("What do you want to choose?")
                while True:
                    if(mod1=="fortuner"):
                        print("1.petrol")
                        print("2.diesel")
                        var1=int(input("Select the variant of model:"))
                        if(var1==1):
                            self.price(var1,mod1)
                            break
                        elif(var1==2):
                            self.price(var1,mod1)
                            break
                            
                        else:
                            print("Invalid! please enter valid variant")
                            continue
                        
                    elif(mod1=="lc"):
                        print("1.petrol")
                        print("2.diesel")
                        var1=int(input("Select the variant of model:"))
                        if(var1==1):
                            self.price(var1,mod1)
                            break
                        elif(var1==2):
                            self.price(var1,mod1)
                            break
                            
                        else:
                            print("Invalid! please enter valid variant")
                            continue
                    else:
                        print("Invalid! please enter valid model")
                        break
            else:
                print("Invalid Comany Name...!")
                break
            break
                        
                
    def price(self,var1,mod1):
        if(var1==1 and mod1=="amg"):
            price=100000
            self.display(mod1,price,self.sgst,self.cgst) 
        elif(var1==2 and mod1=="amg"):
            price=100500
            self.display(mod1,price,self.sgst,self.cgst) 
        elif(var1==1 and mod1=="pw"):
            price=300000
            self.display(mod1,price,self.sgst,self.cgst) 
        elif(var1==2 and mod1=="pw"):
            price=300500
            self.display(mod1,price,self.sgst,self.cgst) 
        elif(var1==1 and mod1=="fortuner"):
            price=400000
            self.display(mod1,price,self.sgst,self.cgst) 
        elif(var1==2 and mod1=="fortuner"):
            price=400500
            self.display(mod1,price,self.sgst,self.cgst) 
        elif(var1==1 and mod1=="lc"):
            price=500000
            self.display(mod1,price,self.sgst,self.cgst) 
        elif(var1==2 and mod1=="lc"):
            price=500500
            self.display(mod1,price,self.sgst,self.cgst) 
        # total_price=self.price+self.sgst+self.cgst
        # print(total_price)
    def display(self,mod1,price,sgst,cgst):
        print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
        print("        Total Bill          ")
        print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
        print("Model:            ",mod1)
        print("Cost:             ",price)
        print("sgst:             ",self.sgst)
        print("cgst:             ",self.cgst)
        print("--------------------------------")
        total_price=price+self.sgst+self.cgst
        print("Total price:      ",total_price)
        print("---------------------------------")
        
                   
c=carshowroom()
c.carcompany()