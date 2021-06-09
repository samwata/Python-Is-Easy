#Create three variables Users, Issues and workers 

Users = "5"               
Issues = 3             
WorkersNeeded = True            
#Comparing Users and issues by first converting the strings into integers
if int(Users) >= 2 and Issues >2:   
    WorkersNeeded = True                      
print(WorkersNeeded)  