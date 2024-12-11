class Car:
    Price=0
    Color=0
    Company=0
    def detail(self):
       
        print("Price ",self.Price )
        print("Color ", self.Color )
        print("Company ", self.Company )

print("CAR 1 ")
car1=Car()
car1.Price=2500000
car1.Color="cyan blue"
car1.Company="ford"
car1.detail()
print()

print("CAR 2 ")
car1=Car()
car1.Price=4500000
car1.Color="Black"
car1.Company="mahindra"
car1.detail()
print()

print("CAR 3 ")
car1=Car()
car1.Price=1500000
car1.Color="Black"
car1.Company="KIA"
car1.detail()


