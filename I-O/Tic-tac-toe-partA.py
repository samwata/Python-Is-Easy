#Tic-Tac_Toe part A
# | |
# ----
# | |
# ----
# | |

def drawfield(n,m):
    for row in range(n):
        if row %2 == 0:
            #print vertical lines
            for column in range(m):
                if column %2 == 0 :
                    if column != m-1:
                        print(" ", end="")
                    else:
                        print(" ")    
                else:
                    print("|", end="")    
        else:
            print("-----")
drawfield(10,5)

#Let us extend it a little using while loop

Player = 1
#Create a list that has all elemnts 
#Eache element in a list has 3 elemnts inside it
CurrentField = [[" "," "," ",], [" "," "," ",], [" "," "," ",]]
print(CurrentField)
while(True):
    print("Player turn: ",Player)
    MoveRow = int(input("Please enter the row\n"))
    MoveColumn = int(input("Please enter column\n"))
    if Player == 1:
        #Make move for Player 1
        CurrentField[MoveColumn][MoveRow] == "O"
        Player = 2

    else:
        #Make move for Player 2
        CurrentField[MoveColumn][MoveRow] == "X"
        Player = 1
    print(CurrentField)

