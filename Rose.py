import pygame
from pygame.locals import *

display_width = 900
display_height = 750

rose_width = 150

# Display = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Welcome to the RoseShop')

# roseImg = pygame.image.load("Rose_Eden.JPG")
WinSize = [1024, 768]
screen = pygame.display.set_mode(WinSize)


mylist = ["Rose_Eden.JPG", "Beach_rose.jpg", "Damask_rose.jpg", "golden_celebration.jpg", "Rosa_peace.jpg"]
for (i, v) in enumerate(mylist):
    roseImg = pygame.image.load(v)
    x = 200 * i + 50
    screen.blit(pygame.transform.scale(roseImg, (rose_width, rose_width)), (x, 200))


def rose(x, y):
    screen.blit(pygame.transform.scale(roseImg, (rose_width, rose_width)), (x, y))


def button(msg,x,y,w,h,ic,ac,action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    print(click)
    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        pygame.draw.rect(gameDisplay, ac, (x, y, w, h))
        if click[0] == 1 and action != None:
            action()
    else:
        pygame.draw.rect(gameDisplay, ic, (x, y, w, h))

    smallText = pygame.font.Font("freesansbold.ttf", 20)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ((x + (w / 2)), (y + (h / 2)))
    gameDisplay.blit(textSurf, textRect)


def main():
    pygame.init()
    pygame.display.set_caption('')
    intro = True
    introimg = pygame.image.load('TheRoseShop.png')

    while True:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                return

        if intro:
            screen = pygame.display.set_mode(WinSize)
            screen.blit(introimg, (125, 125))

        if intro == False:
            for i in mylist:
                roseImg = pygame.image.load(i)
                x = i * 10
                # screen.blit(pygame.transform.scale(roseImg, (rose_width, rose_width)), (x, 200))
        pygame.display.update()
if __name__ == '__main__':
    main()


def numflower(num):
    if num == 1:
        return "Rose Eden"
    elif num == 2:
        return "Golden Celebration"
    elif num == 3:
        return "Damask Rose"
    elif num == 4:
        return "Beach Rose"
    elif num == 5:
        return "Rosa Peace"
    else:
        return "Please enter the rose you would like according to its number"
print(numflower(int(input("Please enter the rose you would like according to its number"))))



items = int(input("How many roses do you want?"))
if items >= 12:
    print("No one needs that many flowers")
else:
    print("Nice and Simple")



style = input("Press enter an arrangement style (Click enter to see the style options)")
arrangement = input("arrangement: Solid, Checked, Vertical Rows, Horizontal Rows")



question = input("Would you like to change the color of your rose")
if question == "yes":
    print("Great")
    Color = input(
        "What color would you like your roses to be: Lilac, Baby Blue, Gold, Rose Gold, White, Black, Dark Green")
else:
    print("Keeping orginial color")



question = input("Do you want the roses in a glass box?")
if question == "yes":
    print("Ok")
else:
    print("Ok")
    Box = input("Would box material would you like: classic, suede, velvet, leather, marble print")
    Box = input("What shape do you want the box to be: round, square, heart")



compose = input("Would you like to compose a greeting card?")
if compose == "yes":
    print("Greeting card message must be 100 characters maximum")
    card = input("Enter your message")
    while len(card) >= 150:
        print("Your message is ", len(card), " characters long. Please revise ")
        card = input("Enter your message")
else:
    print("Checkout")



information = input("Enter your first and last name")
information = input("Street Address")
information = input("Email Address")



information = input("Select type of payment: Amex, Visa, Mastercard, Chase, Citibank ")
information = input("Card Number")



statement = input("Press Enter to Finalize Order")
statement = input("Thank you for shopping at the RoseShop")



question = input("Would you like to order another box of roses?")
if question == "yes":
    print("Excellent")
else:
    print("Exit")

pygame.quit()
quit()