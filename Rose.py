import pygame
from pygame.locals import *

display_width = 900
display_height = 750

rose_width = 250

Display = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Welcome to Le Fleur de Rose')

#roseImg = pygame.image.load("Rose_Eden.JPG")
WinSize = [1024,768]
screen = pygame.display.set_mode(WinSize)

mylist = ["Rose_Eden.JPG", "Beach_rose.jpg", "Damask_rose.jpg", "golden_celebration.jpg"]
for i in mylist:
    roseImg = pygame.image.load(i)
    x = 10
    screen.blit(pygame.transform.scale(roseImg, (rose_width, rose_width)), (x, 200))

def rose(x, y):
    screen.blit(pygame.transform.scale(roseImg, (rose_width, rose_width)), (x, y))

def main():
    pygame.init()
    pygame.display.set_caption('')

    while True:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                return
        for i in mylist:
            roseImg = pygame.image.load(i)
            x = i*10
            screen.blit(pygame.transform.scale(roseImg, (rose_width, rose_width)), (x, 200))
        pygame.display.update()
if __name__ == '__main__':
    main()

pygame.quit()
quit()

def numflower(num):
    if num == 1:
        return "Rose Eden"
    elif num == 2:
        return "Golden Celebration"
    elif num == 3:
        return "Damask Rose"
    elif num == 4:
        return "Beach Rose"
    else:
        return "Please enter the rose you would like according to its number"
print(numflower(int(input("Please enter the rose you would like according to its number"))))

items = int(input("How many roses do you want?"))
if items >= 12:
    print("No one needs that many flowers")
else:
    print("Nice and Simple")

style = input("Press enter an arrangement style")
arrangement = input("arrangement: Solid, Checked, Vertical Rows, Horizontal Rows")
   
question = input("Would you like to change the color of your rose")
if question == "yes":
    print ("Great")
    Color = input("What color would you like your roses to be: Lilac, Baby Blue, Gold, Rose Gold, White, Black, Dark Green")   
else:
    print("Keeping orginial color")
    
question = input("Do you want the roses in a glass box?")
if question == "yes": 
    print ("Ok" )
else:
    print ("Ok") 
    Box = input("Would box material would you like: classic, suede, velvet, leather, marble print")
    Box = input("What shape do you want the box to be: round, square, heart")
    
compose = input("Would you like to compose a greeting card?")
if compose == "yes": 
    print("Greeting card message must be 150 characters maximum")
    card = input("Enter your message")
    while len(card) >= 150:
        print("Your message is ", len(card), " characters long. Please revise ") 
        card = input("Enter your message")             
else:
    print("Moving on to next step") 
        

question = input("Would you like to order another box of roses?")
