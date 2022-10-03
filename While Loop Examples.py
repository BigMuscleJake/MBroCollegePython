#While Loops - 26/09/2022
#First Example
n = 0

while n < 5:
    print(n)
    n = n + 1
#End While
print()

#Second Example
m = 1
while m != 0:
      m = int(input("Please enter any value. Enter 0 to kill the program. "))
      print(m)
#End While
print()

#Using While Loops and If Statements Together
answer = "n"
while answer != "0":
      answer = input("This statement is false. True or False? Enter 0 to kill the program ")
      if answer == "True":
         print("True? I'm not sure. ")
      elif answer == "False":
           print("False? I don't know. ")
      elif answer == "0":
           print()
      else:
           print("Answer Invalid, Try Again. ")
      #End If
#End While
