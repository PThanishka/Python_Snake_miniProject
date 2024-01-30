import pygame
import time
import random

pygame.init()

violet=(130, 89, 113)#back-ground for game
red=(218, 15, 25)#food
green=(133, 233, 67)#snake
blue=(37,50,235)#score
rose=(99,9,104)#message
purple=(185,155,224)#back-ground for game over

# display size
dis_width=600
dis_height=400

dis=pygame.display.set_mode((dis_width,dis_height))
pygame.display.set_caption('Python Snake Game')
clock=pygame.time.Clock()

#sixe of snake
snake_block=10
#speed of snake
snake_speed=15

font_style=pygame.font.SysFont('impact',25)
score_font=pygame.font.SysFont('impact',20)

def Your_score(score):
    value=score_font.render("Score : "+str(score),True,blue)
    dis.blit(value,[0,0]) #used to draw or create the changes

def our_snake(snake_block,snake_list):
    for x in snake_list:
        pygame.draw.circle(dis,green, (x[0] + snake_block //2, x[1] + snake_block //2),snake_block //2)

def message(msg,color):
    mesg=font_style.render(msg,True,color)
    dis.blit(mesg,[dis_width/6,dis_height/3])

def gameLoop():
    game_over=False
    game_close=False

    x1=dis_width/2
    y1=dis_height/2

    x1_change=0
    y1_change=0

    snake_List=[]
    Length_of_snake=1

#this statement will generate food random
    foodx=round(random.randrange(0,dis_width-snake_block)/10.0)*10.0
    foody=round(random.randrange(0,dis_height-snake_block)/10.0)*10.0

    while not game_over:
        while game_close==True:
            dis.fill(purple)
            lost="You lost press C to play again or Q to quit"
            message(lost,rose)
            Your_score(Length_of_snake-1)
            pygame.display.update()
#conditions for either to run or to quit
            for event in pygame.event.get():
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_q:
                        game_over=True
                        game_close=False
                    if event.key==pygame.K_c:
                        gameLoop()

        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                game_over=True
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_LEFT:
                    x1_change= -snake_block
                    y1_change=0
                elif event.key==pygame.K_RIGHT:
                    x1_change=snake_block
                    y1_change=0
                elif event.key==pygame.K_UP:
                    y1_change= -snake_block
                    x1_change=0
                elif event.key==pygame.K_DOWN:
                    y1_change=snake_block
                    x1_change=0

        if x1>=dis_width or x1 <0 or y1>=dis_height or y1<0:
            game_close=True
        x1 += x1_change
        y1 += y1_change
        dis.fill(violet)
        pygame.draw.rect(dis,red,[foodx,foody,snake_block,snake_block])
        snake_Head=[]
        snake_Head.append(x1) #increasing snake on x-axis
        snake_Head.append(y1) #increasing snake on y-axis
        snake_List.append(snake_Head)
        if len(snake_List)>Length_of_snake:
            del snake_List[0]

        for x in snake_List[:-1]: # one is removed
            if x==snake_Head:
                game_close=True

        our_snake(snake_block,snake_List)
        Your_score(Length_of_snake-1)

        pygame.display.update()

        if x1 == foodx and y1 == foody:
            foodx=round(random.randrange(0,dis_width-snake_block)/10.0)*10.0
            foody=round(random.randrange(0,dis_height-snake_block)/10.0)*10.0
            Length_of_snake +=1

        clock.tick(snake_speed)

    pygame.quit()
    quit()
gameLoop()