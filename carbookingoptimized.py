class carshowroom:
    def __init__(self):
        self.cgst=1000
        self.sgst=1000
        self.company = ['mercedes','toyota']
        self.d = {'mercedes':['amg','pw'] ,'toyota':['fortuner','lc'] }
    def carcompany(self):
            while True:
                print("Choose the car-company from the below:")
                print("1.Mercedes")
                print("2.Toyota")
                carc=input("What do you want to choose?").lower()
                if carc in self.company:
                    mod = self.model(carc,self.d[carc])
                    var = self.varient(mod)
                    self.price(mod,var)
                else:
                    print("Invalid company....!")
                    
    
    def model(self,carc,ls):
        print(f"*****Welcome to {carc}*****")
        print("Choose the model of company:")
        while True:
            print("Enter the models : ")
            for i in range(len(ls)):
                print(f"{i+1}. {ls[i]}")
            ch = input("Enter the model varient : ")
            if ch in ls:
                return ch
            else:
                print("Enter the valid model...!")
                
    def varient(self,var):
            while True:
                print(f"*****Make choice in {var}*****")
                ch = int(input("\n1.Petrol \n2.Diesel \nEnter Variant of a model: "))
                if (ch == 1):
                    return 1
                elif (ch == 2):
                    return 2
                else:
                    print("Enter the valid Variant...!")
         
    def price(self,mod,var):
        if mod  == "amg":
           price = 100000 if var == 1 else 100500
        elif mod == "pw":
           price = 300000 if var == 1 else 300500
        elif mod == "fortuner":
           price = 500000 if var == 1 else 500500
        elif mod == "lc":
           price = 1000000 if var == 1 else 1000500            
        self.display(mod,price,self.sgst,self.cgst)    
        
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