#Homework Assignment #8: Input and Output (I/O)
from os import close

def assignment():
    FileList =["ParticipantData"]
    client_file=input("Please enter the file name: ")
    if client_file not in FileList:
        print("The file does not exist")
        description=input("Please enter the text you want to save to file")
        FileList.append(client_file)
        file_add= open("client_file.txt", "w")
        str_description = repr(description)
        file_add.write("description= "+str_description)
        file_add.close()
    else:
        response=input("Enter \n A If you want to Read the file \n B If you want to delete the file and start over \n C If you want to append the file \n D If you want to replace a line \n")
        # Read data in my file
        if response == "A":
            with open('ParticipantData.txt') as f:
                lines = f.readlines()
                print(lines)
                f.close()
                #Overwrite my file with new data
        elif response== "B":
            with open('ParticipantData.txt', "w") as myfile:
                newData = input("Input data you want to overwrite the file with: ")
                myfile.write(newData)
                myfile.close()
                #appending new data to my file
        elif response == "C":
            file_object = open('ParticipantData.txt', 'a')
            file_object.close()
            #Replacing a line
        elif response == "C":
            line_no= int(input("Enter the line number you want to replace"))
            newline = input("The text you want to replace that line with")
            with open("ParticipantData","w") as myfile:
                line = myfile.readline().splitlines()
                line[line_no] = newline

assignment()




