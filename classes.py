#Initializing class 

class car:
    country_standards = {"Kenya", "UG"} #Car class variable
    price_change = 1.05
    def __init__(self, color, brand, name, price) -> None:
        self.color = color
        self.brand = brand
        self.name = name
        self.price = price
    def car_desc(self):
        return '{} {} {} {}'.format(self.color, self.name, self.brand, self.price)

    def price_increase(self):
        new_price =self.price * self.price_change
        return new_price

#Instance variables
car1=car("White","VW","Polo",5000)
car2=car("Black","Ford","Figo",3500)

print(car1.car_desc())
print(car2.car_desc())

print(car1.country_standards)
print("Price after import is:", car1.price_increase())

# car1.color = "White"
# car2.color = "Black"

# print(car1.color)
# print(car1.brand)
# print(car1.name)
# print(car1.price)