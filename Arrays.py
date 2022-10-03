#Array Tasks - 26/09/2022
#Declare Array
arr = [2, 5, 7, 3, 19, 5]

#Task 1 - First 3 Items
print(arr[0],arr[1],arr[2])

#Task 2 - Reverse Order
res = arr[::-1]
print(res)

#Task 3 - Duplicate Number
userInput = input("Enter a value you would like to test the number of ocurences. ")
total = 0
for i in arr:
    if i == userInput:
       total = total + 1
    #End If
#Next i



