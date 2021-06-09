# We are going to write a program that registers a participant list
ParticipantNumber = 5
ParticipantData = []
outputFile = open("ParticipantData.txt", "w")

registeredParticipant = 0

while(registeredParticipant < ParticipantNumber):
    tempPartData = []
    name = input("Please enter your name: ")
    tempPartData.append(name)
    country = input("Please enter your country of origin: ")
    tempPartData.append(country)
    age = int(input("Please enter your age: "))
    tempPartData.append(age) #[name,country,age]
    #print(tempPartData)
    ParticipantData.append(tempPartData) #[[name,country,age]]
    #print(ParticipantData)
    registeredParticipant += 1

for participant in ParticipantData:
    for data in participant:
        outputFile.write(str(data)) #str formats int to float i.e 25 to "25"
        outputFile.write(" ") #Sam kenya 25

    outputFile.write("\n")    #Adding new line in the file for every participant                
outputFile.close()  #Closing the file

#Reading data from the file
inputFile = open("ParticipantData.txt", "r")

inputList = []

#Reading data line by line
for line in inputFile:
    tempParticipant = line.strip("\n").split()
    #Sam kenya 25 /n .strip("\n") --> Sam Kenya 25
    # Sam Kenya 25 .split()
    inputList.append(tempParticipant)
    #print(inputList)

#Save Age data to a dictionary
Age = {}
for part in inputList:
    tempAge = int(part[-1]) #int('21') --> 21
    if tempAge in Age:
        Age[tempAge] += 1
    else:
        Age[tempAge] = 1

print(Age)

inputFile.close()
