#First assignment to create a board


for row in range(40): #0,1,2,3,4
    if row%2 == 0:
        for column in range(1,21):
            if column%2 == 0:
                if column !=20:
                    print(" ", end=" ")
                else:
                    print(" ")
            else:
                print("|", end=" ")
        #print(" | | ")
             #  12345
    else:
        print("-------------------------------------------------")  
        if row ==39:
            print("True", end=" ")
        elif row > 39:
                print("False", end=" ")    
        else:
            print(" ")    
        
