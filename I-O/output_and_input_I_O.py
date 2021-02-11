# Var = input("message to the user")
# age =int(input("Enter your age: "))
# print(age)
# print(str(age)+1)

#Let us create a for loop for scores
scores=[]
for i in range(5):
    CurrentScore = int(input("Enter your Score: "))
    scores.append(CurrentScore)

print(Scores)

for i in range(5):
    CurrentScore = float(input("Enter your Score " +str(i+1)": ")) #str(i) adds a the current loop number we are in
    scores.append(CurrentScore)
    print("The score you entered is:\n"+str(CurrentScore))
print(Scores)

#FILE I\O
# File = open("File name","r") #"r", "w", "a", "r+" ---> read and write
# File.close() #Its good practice to close your file

VacationSpots = ["London","Newyork","Paris","kenya","Zanzibar"]
VacationFile = open("VacationPlaces","w")

for Spots in VacationSpots:
    VacationFile.write(Spots + "\n")
VacationFile.close()
VacationFile = open("VacationPlaces","r")

FirstLine = VacationFile.readline()
print(FirstLine)

SecondLine = VacationFile.readline()
print(SecondLine)

for Line in VacationFile:
    print(Line, end = "")

# ThewholeFile = VacationFile.read()
# print(ThewholeFile)
VacationFile.close()

#Append data to file
FinalSpot="Thailand"
VacationFile = open("VacationPlaces","a")
VacationFile.write(FinalSpot)
VacationFile.close()

VacationFile = open("VacationPlaces","r")
for Line in VacationFile:
    print(Line, end="")

VacationFile.close()

#Another way of reading a file without necessarily closing it
with open("VocationPlaces","r") as VacationPlaces:
    for Line in VacationPlaces:
        print(Line)
#using with statement you can use it to open or access the file multiple times
for i in range(5):
    with open("VocationPlaces","r") as VacationPlaces:
        for Line in VacationPlaces:
            print(Line)

#Tic-Tac_Toe part A
# | |
# ----
# | |
# ----
# | |


