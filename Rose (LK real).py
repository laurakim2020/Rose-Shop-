print("Welcome to the La Fleur")
def flowerchoice(): 
    list = ["Rosa Eden'", "Golden Celebration", "Damask rose", "Beach rose"]
    list = input("pick a rose")
    if list == "Golden Celebration":
        print ("good choice")
    elif list == "Rosa Eden":
        print ("great")
    elif list == "Damask rose":
        print ("awesome choice")
    elif list == "Beach rose":
        print ("awesome")
    else:
        print (list, "choose rose from list please")
    

