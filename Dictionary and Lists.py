#Data Structures - Dictionaries - 30/10/2022
#Dictionary Zip Challenge
#Declare Lists
keys = ['Ten', 'Twenty', 'Thrity']
values = [10, 20, 30]

#Show Originals
print("Original Keys List -", keys)
print("Original Values List -", values)
print()

#Convert to Dictionary
final = dict(zip(keys, values))

#Show Dictionary
print("New Dictionary -", final)
print()

#Dictionary Key Challenge
#Declare Dictionary
sampleDict = {
    "class":{
        "student":{
           "name":"Mike",
           "marks":{
              "physics":70,
              "history":80
            }
        }
    }
}
 
#Print Value "80"
print(sampleDict['class']['student']['marks']['history'])
print()

#Dictionary Delete Challenge
sampleDict2 = {
    "name": "Kelly",
    "age":25,
    "salary": 8000,
    "city": "New York"

}
del sampleDict2["name"]
del sampleDict2["salary"]
print (sampleDict2)
print()

#Dictionary Rename Key Challenge
sampleDict3 = {
    "name": "Willow",
    "age":21,
    "salary": 8000,
    "city": "Mbro"

}
sampleDict3['location'] = sampleDict3.pop('city')
print (sampleDict3)






