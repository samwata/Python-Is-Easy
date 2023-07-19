#Songs dictionary
Songs = {"Laugh Now, Cry Later":"Drake","Dark Lane Demo Tapes":"Drake",
"Sounds from the Other Side":"Wizkid","Joro":"Wizkid","jeje":"Diamond Platnumz","A Boy from Tandale":"Diamond Platnumz",
"Tambarare":"Eunice Njeri"}

#Function to check if the Song exists in Songs dictionary
while (True):
    SongName = input("Please enter the song title and artist seperated by colon i.e song_name:artist :")
    List=SongName.split(":")
    if List[0] in Songs and List[1] in Songs.values():
        print("True")
    else:
        print("False")

