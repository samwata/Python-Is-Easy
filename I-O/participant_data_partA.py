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
    print(tempPartData)
    ParticipantData.append(tempPartData) #[[name,country,age]]
    print(ParticipantData)
    registeredParticipant += 1

for participant in ParticipantData:
    for data in participant:
        outputFile.write(str(data)) #str formats int to float i.e 25 to "25"
        outputFile.write(" ") #Sam kenya 25

    outputFile.write("\n")    #Adding new line in the file for every participant                
outputFile.close()  #Closing the file
