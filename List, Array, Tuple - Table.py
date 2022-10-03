#Table: Lists, Arrays, Tuples - 03/10/2022
#Prettytable
from prettytable import PrettyTable

#Declare Headers
columns = ["Question", "List", "Array", "Tuple"]

#Declare Table
myTable = PrettyTable()

#Declare Column Data
myTable.add_column(columns[0], ["Is it mutable?", "Can we change the size after creation?", "Can items in the list be changed?", "How many different types of data can be stored?"])
myTable.add_column(columns[1], ["Yes", "Yes", "Yes", "All"])
myTable.add_column(columns[2], ["Yes", "No","Yes", "All"])
myTable.add_column(columns[3], ["No", "No", "No", "All"])

#Print Table
print(myTable)
                   
