import collections
class Pizza:
    def __init__(self, name, price, sauce = "tomato"):
        self.name = name
        self.price = price
        self.sauce = sauce


class Starters:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class Beverages:
    def __init__(self, name, price):
        self.name = name
        self.price = price


pizza1 = Pizza("Margherita" , 100, "Chilli")
pizza2 = Pizza("Tomato sauce", 150)
pizza3 = Pizza("Mozzarella", 300)
starter1 = Starters("Onion rings", 60)
starter2 = Starters("Honey Chilli Potatoes", 100)
drinks1 = Beverages("Coca Cola", 50)
drinks2 = Beverages("Thick Shake", 150)
pizzas = {1: pizza1.name, 2: pizza2.name, 3: pizza3.name, 4: starter1.name, 5: starter2.name, 6: drinks1.name, 7: drinks2.name}
prices = {1: pizza1.price, 2: pizza2.price, 3: pizza3.price, 4: starter1.price, 5: starter2.price, 6: drinks1.price, 7: drinks2.price}
orderType = int(input("Enter 1 for dine in 2 for delivery"))
print("-"*40)
print("Welcome to Dominos Pizza")
print("-"*40)
print("The menu is as follow")
print("1.{} {} ".format(pizza1.name, pizza1.price))
print("2.{} {} ".format(pizza2.name, pizza2.price))
print("3.{} {} ".format(pizza3.name, pizza3.price))
print("4.{} {} ".format(starter1.name, starter1.price))
print("5.{} {} ".format(starter2.name, starter2.price))
print("6.{} {} ".format(drinks1.name, drinks1.price))
print("7.{} {} ".format(drinks2.name, drinks2.price))
print()
print("enter the number to order by placing space and if complete press enter")
a = [int(x) for x in input().split()]
b=[]

for i in range(0, len(a)):
    if a[i] > 0 and a[i] < 8:
        b.append(a[i])

counter = collections.Counter(b)
price = 0
for i in counter.keys():
    print(pizzas.get(i),counter.get(i))
    price = price+counter.get(i)*prices.get(i)
print("The Net Order Amount is : ", price)
print()
print("-"*40)
if orderType == 2 :
    print("The Order Will reach to your place Soon")
else:
    print("Thanks For Your Order")
print("-"*40)