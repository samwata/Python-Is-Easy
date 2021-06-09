#We are now going to incooperate the function into our while loop

def drawfield(field):
    for row in range(5):
        if row %2 == 0: #0,2,4
            #Since we need values 0,1,2 according to our list
            #We will divide the values that are divisible by 2 to get 0,1,2
            PracticalRow = int(row/2) #0,1,2
            #print vertical lines
            for column in range(5):
                if column %2 == 0 : # 0,2,4 that pass here
                    #Since we need values 0,1,2 according to our list
                    #We will divide the values that are divisible by 2 to get 0,1,2
                    PracticalColumn = int(column/2) #0,1,2
                    if column != 4:
                        print(field[PracticalColumn][PracticalRow], end="")
                    else:
                        print(field[PracticalColumn][PracticalRow])    
                else:
                    print("|", end="")    
        else:
            print("-----")


#Let us extend it a little using while loop

Player = 1
#Create a list that has all elemnts 
#Eache element in a list has 3 elemnts inside it
CurrentField = [[" "," "," ",], [" "," "," ",], [" "," "," ",]]

drawfield(CurrentField)
while(True):
    print("Player turn: ",Player)
    MoveRow = int(input("Please enter the row\n"))
    MoveColumn = int(input("Please enter column\n"))
    if Player == 1:
        #Make move for Player 1
        if CurrentField[MoveColumn][MoveRow] == " " :
            CurrentField[MoveColumn][MoveRow] = "X"
            Player = 2
        

    else:
        #Make move for Player 2
        if CurrentField[MoveColumn][MoveRow] == " ":
            CurrentField[MoveColumn][MoveRow] = "O"
            Player = 1
    drawfield(CurrentField)
