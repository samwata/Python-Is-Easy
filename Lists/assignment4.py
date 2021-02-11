#Define my list variable
myUniqueList =[]
print(myUniqueList)

#Create a function that checks if the value is my list
def AddToList(Value):
    if Value in myUniqueList:
        print("True")
    else:
        myUniqueList.append(Value)
        print("False")
        
    return Value

#Add a Value to my list using the function
AddToList(30)
print(myUniqueList)

#Add another Value to the list
AddToList(33)
print(myUniqueList)

#Add the same Value to the list to test if the function will still add existing value
AddToList(33)
print(myUniqueList)

#Add another Value to the list
AddToList(45)
print(myUniqueList)


#Adding another function for leftovers
myUniqueList =[]
myLeftOvers =[]
def AddListValue(Value):
    if Value in myUniqueList:
        print("True")
        myLeftOvers.append(Value)
    else:
        myUniqueList.append(Value)
        print("False")
        
    return Value

#Testing the function by adding a value
AddListValue(60)
print(myUniqueList)
print(myLeftOvers)
#Add a second Value
AddListValue(70)
print(myUniqueList)
print(myLeftOvers)
#Add a third value
AddListValue(80)
print(myUniqueList)
print(myLeftOvers)
#Add the third value(80) again
AddListValue(80)
print(myUniqueList)
print(myLeftOvers)
#Add the first value(60) again
AddListValue(60)
print(myUniqueList)
print(myLeftOvers)

