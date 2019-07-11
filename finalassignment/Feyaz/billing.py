#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 31 20:11:48 2019

@author: ghost
"""
#Structure:
#The menu is declared in global scope
#an option is given to display the menu
#then we input the indexes, corresponding to which a list is made with indexes
#the list is passed into a func checkoffers
#after applying an offer, if any, the cost is printed out,
#the bill is prepared with a time index for bill number, 
#so it looks intimidating
#


from datetime import datetime
#variable to find no of items on menu, because the free addons are separate items on the menu.
no_of_items=7
#Mc Donalds' had the same system. Bill clerks could ring up free drinks for their friends.
#This system was corrected, I'm just lazy here.

#function to apply checkout stuff, ie, make the final bill, finalise quantities of items, apply discounts, etc
def checkout(billmaking):
    billmaking.sort()
    quantity={}
    for x in range(1,no_of_items+2):
        quantity[x]=0
    for item in billmaking:
        if((item) in quantity):
           quantity[item]+=1
    pizzano=quantity[3]+quantity[1]+quantity[2]
    if pizzano>2:
        choice=input("You can get a free drink! Either Conke(A) or Bepis(B)! Enter N to opt out:").upper()
        if(choice=="A"):
            quantity[8]+=1
        elif(choice=="B"):
            quantity[9]+=1
    print("Calculating total costs:")
    for x in range(1,no_of_items+2):
        if quantity[x]!=0:
            print(str(quantity[x])+" x "+ menu[x-1].name)
    finalcost=0
    for x in range(1,8):
        finalcost+=quantity[x]*menu[x-1].cost
    print("Bill total before VAT is "+ str(finalcost)+ ".Will that be cash or credit?")
    #One more thing I want to say, people usually gloss over the amount being displayed before VAT. Some people get angry enough
    #that they'd walk out without their order. So, McD noticed that if people took their wallet out to pay before they saw the 
    #final cost, they were more likely to pay the full price. It's a salesman trick.
    finalcost*=1.116
    print("+++++\nFinal cost after VAT is: "+str(round(finalcost,2)))
    return (finalcost, quantity)   

#class for each item on the menu. intro function serves no purpose.
class item:
    def __init__(self, name, cost, ind):
        self.name=name
        self.cost=cost
        self.ind=ind
    def intro(self):
        print("Hello! I'm a " + self.name+"!")
        
#Menu initialised in global scope       
menu=[]
menu.append(item("Pepperoni Mamma mia", 400, 1))
menu.append(item("Veg express", 350, 2))
menu.append(item("Chicken Heartattack", 450, 3))
menu.append(item("Non veg Calzone", 400, 4))
menu.append(item("Pasta", 400, 5))
menu.append(item("Conke", 40, 6))
menu.append(item("Bepis", 40, 7))
menu.append(item("Conke(Free on offer)", 0, 8))
menu.append(item("Bepis(Free on offer)", 0, 9))

#to print out every item the clerk is allowed to access. 
def display_menu():
    for x in range(no_of_items):
        print("Item "+str(x+1)+ ": " +menu[x].name+ ": Rs."+ str(menu[x].cost))
    print("======")

#class for bill, so we can store each bill
class bill:
    def __init__(self, quantity, amount, orderType, index):
        print("making a bill beep boop beep boop")
        self.quantity=quantity
        self.amount=amount
        self.orderType=orderType
        self.index=index

#driver code + other stuff
def main():
    #as long as the store is open,
    storeOpen=True
    #keep a steady list of bills
    bill_list=[]
    while(storeOpen):
        menuop=input("Welcome to Pizza hut! \nWanna see the menu?Y/N:")
        if(menuop.upper()=="Y"):
            display_menu()
        else:
            print("Hope you know what you're doing!", end="")
        #this goes on the bill
        ordertype=input("Is this a takeout meal?").upper()
        #if they're taking 2 number threes, they need to enter 3 in two separate turns
        print("taking orders now. Enter any non number to exit")
        entry=True
        #list to store the values they input, for later sorting and calc
        billmaking=[]
        while(entry):
            no=input("Enter menu index:")
            if no.isnumeric() == False:
                break
            no=int(no)
            billmaking.append(no)
        #dictionary to save the relative quantities, and to be stored on the bill.
        quant={}
        #unpacking values from checkout.
        outcost, quant= checkout(billmaking)
        #making the bill index the date, and time.
        now=datetime.now()
        billindex=now.strftime("%d/%m/%y::%H:%M")
        #adding the bill to the list of bills.
        bill_list.append(bill(quant,outcost,ordertype,billindex))
        #checking if it's closing time, and if it is, stop the billing.
        closingTime=input("is it closing time?Y/N:").upper()
        if closingTime=="Y":
            print("*sings closing time by semisonic*")
            #seriously, if you haven't heard it yet, and you're bored, check them out.
            storeOpen=False
        else:
            print("*keeps working*")
        
if __name__=='__main__':
    main()