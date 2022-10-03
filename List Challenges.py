#List Challenges - 03/10/2022
#Declare Lists
stringList = ["Jake", "Willow", "Alfie", "Zoey", "Elliot"]
integerList = [1, 2, 3, 4, 5]

#Print Orignals
print(stringList)
print(integerList)
print()

#Challenge 1 - Reverse One of the Lists
stringList.reverse()
print(stringList)
print()

#Challenge 2 - Concatenate the Lists
print(stringList + integerList)
print()

#Challenge 3 - Square Every Value of the Int List
squaredNumbers = [number ** 2 for number in integerList]
print(squaredNumbers)
print()



