#VAT Calculator - 26/09/2022
#Declare Variables
product = input("Which product would you like to calculate the VAT of? ")
price = float(input("What is the price of your product in GBP? "))
price = "{:.2f}".format(price)

#Define Function
def vatCalc(price, product):
    price = price / 100
    price = price * 20
    print("The VAT of " + product + " is £",price)
#End Function
vatCalc(price, product)


    
    
