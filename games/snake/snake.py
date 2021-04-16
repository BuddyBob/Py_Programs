import pygame
from pygame import mixer
from pygame.locals import *
import sqlite3,time,random
pygame.init()
mixer.init()
song = 'music/music1.mp3'
volume = 0
mixer.music.load(song) 
mixer.music.set_volume(volume) 
pygame.mixer.music.play(100) # repeat 5 times
pygame.mixer.music.queue(song)
#set up screen
screen = pygame.display.set_mode((600,600))
pygame.display.set_caption("Snake Game")
screen.fill((74, 66, 66))
#import a restart btn
colorWheel = pygame.image.load('colorWheel.png')
colorWheel = pygame.transform.scale(colorWheel,(150,150))
restart = pygame.image.load('restart.png')
restart = pygame.transform.scale(restart,(400,100))
musicMenue = pygame.image.load('musicMenue.png')
musicMenue = pygame.transform.scale(musicMenue,(60,60))
leaderBoardButton = pygame.image.load('leaderBoard.png')
leaderBoardButton = pygame.transform.scale(leaderBoardButton,(60,60))
#variables
sqx = 0
sqy = 100
speedx = 0
speedy = 0
color1 = (31, 29, 29)
color2 = (69, 52, 52)
bps = 10
score = 0
snakeList = []
#snake pos
x = (random.randint(10,580) // 20) * 20
y = (random.randint(100,400) // 20) * 20

#food pos
foodx = (random.randint(10,580) // 20) * 20
foody = (random.randint(100,400) // 20) * 20

#*checkerboard
def funtext():
    font = pygame.font.Font("arial.ttf", 50)
    # 33, 32, 28
    text = font.render("Score: "+str(score), True, (26, 25, 24))
def checkerboard(sqx,sqy,color1,color2):
    pygame.draw.rect(screen,(207, 204, 204),(0,100, 600,400),5)
    for i in range(1,600+1):
        pygame.draw.rect(screen,(color1),(sqx,sqy,20,20),0)
        color1,color2 = color2,color1
        sqx += 20
        if i % 30 == 0:
            color1,color2 = color2,color1
            sqy += 20
            sqx = 0
    sqx = 0
    sqy = 100











def get_key(backUp,AvailKeys):
    while 1:
        event = pygame.event.poll()
        if event.type == KEYDOWN:
            if event.key in AvailKeys:
                return event.key
            if event.key == K_ESCAPE:
                return backUp
        else:
            pass

def display_box(screen, message,backUp,innerBoxX,innerBoxY,outterBoxX,outterBoxY,textX,textY):
    "Print a message in a box in the middle of the screen"
    fontobject = pygame.font.Font('arial.ttf',20)
    pygame.draw.rect(screen, (0,0,0),
                    ((screen.get_width() / 2) - innerBoxX,
                    (screen.get_height() / 2) + innerBoxY,
                    201,30), 0)
    backUup = backUp
    backUp = backUp.split(',')
    try:
        backUp = [int(i) for i in backUp]
        if backUp[0] != backUup[0]:
            backUp == snakeColor
    except:
        backUp = 245, 47, 83
    backUp = tuple(backUp)
    
    pygame.draw.rect(screen, backUp,
                    ((screen.get_width() / 2) - outterBoxX,
                    (screen.get_height() / 2) + outterBoxY,
                    205,34), 4)
    if len(message) != 0:
        screen.blit(fontobject.render(message, 1, (255,255,255)),((screen.get_width() / 2)-textX, (screen.get_height() / 2) + textY))
    pygame.display.flip()
def ask(screen, question,backUp,innerBoxX,innerBoxY,outterBoxX,outterBoxY,textX,textY,AvailKeys):
    "ask(screen, question) -> answer"
    pygame.font.init()

    current_string = []
    display_box(screen, question + ": " + ''.join(current_string),backUp,innerBoxX,innerBoxY,outterBoxX,outterBoxY,textX,textY)
    while 1:
        inkey = get_key(backUp,AvailKeys)
        if inkey == K_BACKSPACE:
            current_string = current_string[:-1]
            try:
                for x in current_string:
                    current_string.remove('\x08')
                
            except:
                pass
        elif inkey == K_RETURN:
            break
        try:
            if inkey <= 127 and inkey!=8 and len(current_string)<=10:
                current_string.append(chr(inkey))
        except:
            current_string.append(backUp)
            break
        display_box(screen, question + ": " + ''.join(current_string),backUp,innerBoxX,innerBoxY,outterBoxX,outterBoxY,textX,textY)
    return ''.join(current_string)

clock = pygame.time.Clock()
restartBtn = False
scores = []
snakeColor = 245, 47, 83
slider_rect1 = pygame.Rect(600, 300, 210, 10)
slider_rect2 = pygame.Rect(600, 400, 210, 10)
highscore = 0

#* sqlite3 
def highscores(scores):
    scores.sort()
    highscore = scores[-1]
    return highscore
conn = sqlite3.connect('leaderboard.db')
#create cursor
c = conn.cursor()

#CREATE TABLE
try:
    c.execute("""CREATE TABLE leaderBoard(
                username text,
                password text,
                highscore integer
            )""") 

except sqlite3.OperationalError: pass
info = True
#ask for username and password

checkerboard(sqx,sqy,color1,color2)
backUp,innerBoxX,innerBoxY,outterBoxX,outterBoxY,textX,textY,AvailKeys = 'dummy',250,100,254,98,244,108,list(range(1,1000))
username = ask(screen,'username',backUp,innerBoxX,innerBoxY,outterBoxX,outterBoxY,textX,textY,AvailKeys)
AvailKeys = list(range(1,1000))
backUp,innerBoxX,innerBoxY,outterBoxX,outterBoxY,textX,textY,AvailKeys = 'dummyPwd',-50,100,-50,98,-55,108,list(range(1,1000))
password = ask(screen,'password',backUp,innerBoxX,innerBoxY,outterBoxX,outterBoxY,textX,textY,AvailKeys)
#!select every login made from user with said username and password
c.execute("SELECT * FROM leaderBoard WHERE username='{}' AND password='{}'".format(username,password))
#take only one
#!if this username and password combination is not in the table, user  with return none
#!if this username and password combination is in the table, user with return ('username', 'password', UsersHighscore)
user = c.fetchone()
print(user)

#print whole table and every users info
#make sure leaderboard has enoough slots for most peoplepython
with conn:
    c.execute("SELECT * FROM leaderBoard")
    print('Database: '+str(c.fetchall()))
print('username '+username)
print('password '+password)

#if the login info occur in the table
if user != None:
    print('logged in')
    print(user)
    #grab highscore located in the 3 slot of the users info
    highscore = user[2]
    print('user highscore: '+str(highscore))
    #scores list constains low and high numbers. Highscore can be compared to everyscore at the end of eatch game
    scores.append(highscore)

#if user is signing up
if user == None:
    print('new account made')
    #set the highscore to 0 therefore they have to start over
    highscore = 0
    #insert there info given above
    c.execute("INSERT INTO leaderBoard VALUES (:username,:password,:highscore)",{'username':username,'password':password,'highscore':highscore})
    conn.commit()

#after the insert and commit this will show the database now
with conn:
    c.execute("SELECT * FROM leaderBoard")
    print('databaseNow: '+str(c.fetchall()))


count = 0
blocksTraveled = 0
gameover = False
while gameover == False:
    bps += .01

    screen.fill((74, 66, 66))

    font = pygame.font.Font("arial.ttf", 25)
    checkerboard(sqx,sqy,color1,color2)
    # 33, 32, 28

    scoreTxt = font.render("Score: "+str(score), True, (26, 25, 24))
    screen.blit(scoreTxt,(75 - scoreTxt.get_width() // 2, 75 - scoreTxt.get_height() // 2))
    highscoreTxt = font.render("Highscore: "+str(highscore), True, (255, 255, 255))
    screen.blit(highscoreTxt,(470- highscoreTxt.get_width() // 2, 75 - highscoreTxt.get_height() // 2))
    smallfont = pygame.font.Font("arial.ttf", 20)
    bpsTxt = smallfont.render("BPS: "+str("{:.2f}".format(round(bps, 2))), True, (255, 255, 255))
    screen.blit(bpsTxt,(250- bpsTxt.get_width() // 2, 80 - bpsTxt.get_height() // 2))
    bodyHead = [x,y]
    try:
        snakeList.pop(0)
    except:
        pass
    snakeList.append(bodyHead)
    if restartBtn == False:
        checkerboard(sqx,sqy,color1,color2)
        for segments in snakeList:
            try:
                pygame.draw.rect(screen,(snakeColor),([segments[0],segments[1]]+[20,20]),0)
            except:
                snakeColor = 245, 47, 83
        pygame.draw.rect(screen,(230, 223, 223),(foodx,foody,20,20),0)
        x += speedx
        y += speedy

        
        if y+10 == foody+10 and x+10 == foodx+10:
            snakeList.append((x,y))
            
            foodx = (random.randint(10,580) // 20) * 20
            foody = (random.randint(100,400) // 20) * 20
            score += 1

            pygame.draw.rect(screen,(230, 223, 223),(foodx,foody,20,20),0)

    # ! ===GAME RESTART====
    if x < -20 or x >= 610 or y <= 70 or y+20 >= 525:
        count += 1
        screen.fill((74, 66, 66))
        checkerboard(sqx,sqy,color1,color2)
        screen.blit(colorWheel,(100,350))
        screen.blit(restart,(100,258))
        # screen.blit(leaderBoardButton,(200,258))
        #insert the new score into scores also were highscore is located
        scores.append(score)
        #check if the database highscore is higher or lower than the current score
        highscore = highscores(scores)
        scoreTxt = font.render("Score: "+str(score), True, (255,255,255))
        screen.blit(scoreTxt,(180 - scoreTxt.get_width() // 2, 225 - scoreTxt.get_height() // 2))
        highscoreTxt = font.render("Highscore: "+str(highscore), True, (255, 255, 255))
        screen.blit(highscoreTxt,(380- highscoreTxt.get_width() // 2, 225 - highscoreTxt.get_height() // 2))
        if count == 1:
            #if so update leaderBoard and set the highscore to the funtions highscore. 
            c.execute("UPDATE leaderBoard SET highscore = :highscore  WHERE  username = :username AND password =  :password",{'highscore':highscore,'username':username,'password':password})
            conn.commit()
            with conn:
                c.execute("SELECT * FROM leaderBoard")
                print('databaseNowNow: '+str(c.fetchall()))
        restartBtn = True
        
    for segments in snakeList[1:]:
        if snakeList[0] == segments:
            screen.fill((74, 66, 66))
            checkerboard(sqx,sqy,color1,color2)
            screen.blit(restart,(100,258))
            scores.append(score)
            highscore = highscores(scores)
            # c.execute("UPDATE leaderBoard SET username=?, password=?, highscore=?",(username,password,highscore))
            # conn.commit()
            scoreTxt = font.render("Score: "+str(score), True, (255,255,255))
            screen.blit(scoreTxt,(180 - scoreTxt.get_width() // 2, 225 - scoreTxt.get_height() // 2))
            highscoreTxt = font.render("Highscore: "+str(highscore), True, (255, 255, 255))
            screen.blit(highscoreTxt,(380- highscoreTxt.get_width() // 2, 225 - highscoreTxt.get_height() // 2))
            
            if count == 1:
            #if so update leaderBoard and set the highscore to the funtions highscore. 
                c.execute("UPDATE leaderBoard SET highscore = :highscore  WHERE  username = :username AND password =  :password",{'highscore':highscore,'username':username,'password':password})
                conn.commit()
                with conn:
                    c.execute("SELECT * FROM leaderBoard")
                    print('databaseNowNow: '+str(c.fetchall()))
            restartBtn = True
    
    
        


    if restartBtn == True:
        screen.blit(colorWheel,(100,350))
        screen.blit(musicMenue,(500,525))
        speedx,speedy = 0,0
        count = -10000000*10000000000000000000000000
    for events in pygame.event.get():
        if events.type == pygame.KEYDOWN:
            if (events.key == K_RIGHT or events.key == K_d) and speedx != -20:
                speedx = 20
                speedy = 0
            elif (events.key == K_LEFT or events.key == K_a) and speedx != 20:
                speedx = -20
                speedy = 0
            elif(events.key == K_UP or events.key == K_w) and speedy != 20:
                speedy = -20
                speedx = 0
            elif(events.key == K_DOWN or events.key == K_s) and speedy != -20:
                speedy = 20
                speedx = 0
        if events.type == pygame.MOUSEBUTTONDOWN:
            if events.pos[0] in range(100,400) and  events.pos[1] in range(258,358):
                restartBtn = False
                foodx = (random.randint(10,580) // 20) * 20
                foody = (random.randint(100,400) // 20) * 20
                speedx = 0
                speedy = 0
                score = 0
                bps = 11
                snakeList = []
                x = (random.randint(10,580) // 20) * 20
                y = (random.randint(100,400) // 20) * 20
            if events.pos[0] in range(100,250) and events.pos[1] in range(350,500):
    
                while True:
                    try:
                        try:
                            snakeColor = str(snakeColor[0])+','+str(snakeColor[1])+','+str(snakeColor[2])
                        except:
                            snakeColor = '245, 47, 83'
                        backUp,innerBoxX,innerBoxY,outterBoxX,outterBoxY,textX,textY,AvailKeys = snakeColor,62,100,64,98,61,108,[44,13,8,48,49,50,51,52,53,54,55,56,57,58,59]
                        snakeColor = ask(screen,'snake color',backUp,innerBoxX,innerBoxY,outterBoxX,outterBoxY,textX,textY,AvailKeys)
                        try:
                            snakeColor = snakeColor.split(',')
                            snakeColor = tuple(map(int, snakeColor))
                        except:
                            snakeColor = (245, 47, 83)
                        if len(snakeColor) == 3:
                            break
                        else:
                            pass
                    except Exception as e:
                        traceback.print_exc()
                        time.sleep(10)
                        pass
            if events.pos[0] in range(500,560) and events.pos[1] in range(525,585):
                snakeColor = str(snakeColor[0])+','+str(snakeColor[1])+','+str(snakeColor[2])
                backUp,innerBoxX,innerBoxY,outterBoxX,outterBoxY,textX,textY,AvailKeys = snakeColor,20,240,23,238,12,250,[44,13,8,48,49,50,51,52,53,54,55,56,57,58,59]
                volume = ask(screen,'volume',backUp,innerBoxX,innerBoxY,outterBoxX,outterBoxY,textX,textY,AvailKeys)
                try:
                    mixer.music.set_volume(int(volume))
                except:
                    pass
                

                
        if events.type == QUIT:
            with conn:
                c.execute("SELECT * FROM leaderBoard")
                print('databaseNowNowNow: '+str(c.fetchall()))
            gameover = True
            screen = pygame.display.set_mode((1100,600))
            
    pygame.display.update()
    clock.tick(bps)