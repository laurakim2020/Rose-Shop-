print ("Welcome to Le Fleur De Rose") 
def numflower(num):
    if num == 0:
        return "Rose Eden"
    elif num == 1:
        return "Golden Celebration"
    elif num == 2:
        return "Damask Rose"
    elif num == 3:
        return "Beach Rose"
    elif num == 4:
        return "Dog-Rose"
    else:
        return "Please enter the rose you would like according to its number"
print(numflower(int(input("Please enter the rose you would like according to its number"))))

items = int(input("How many roses do you want?"))
if items >= 12:
    print("No one needs that many flowers")
else:
    print("Nice and Simple")

question = input("Would you like to change the color")
if question == "yes":
    print ("Great")
    Color = input("What color would you like your roses to be: Lavender, Maroon, Gold, Yellow")
else:
    print("Nice")
    
Box = input("Choose a box color: Black, White, Grey")

