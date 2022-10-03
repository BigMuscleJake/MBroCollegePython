#FizzBuzz - 26/09/2022
#Declare Variables
value = 1
Continue = True

#Iteration
while Continue:
    #Selection
    if value % 3 == 0 and value % 5 == 0:
        print("FizzBuzz")
    elif value % 3 == 0:
         print("Fizz")
    elif value % 5 == 0:
         print("Buzz")
    else:
         print(value)
    #End If
         
    value = value + 1
    
    #Selection
    if value > 50:
       Continue = False
    #End If
#End While
       
    
