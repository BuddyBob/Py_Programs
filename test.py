Cliimport turtle as trtl
import random 

yorn = input("would you like to play? type Y or N. ")

global timer
if yorn == "Y":
  userrounds = int(input("how many rounds?(1-7)  "))
#timer = int(input("how many seconds?   "))
colorwords = ["red", "orange", "green", "blue", "purple", "white", "black"]
colorchoices = ["red", "orange", "yellow", "green", "blue", "purple", "black"]
writer = trtl.Turtle()
writer.penup()
font_setup = ("Arial", 20, "normal")
timer = 5
global counter_interval
counter_interval = 1000  
global timer_up
timer_up = False
counter =  trtl.Turtle()
writr = trtl.Turtle()
writr.penup()
writr.goto(0, -120)
wn = trtl.Screen()

def countdown():
  global timer, timer_up, counterinterval
  writr.clear()
  if timer == 0:
    timer_up = True
  if timer > 0:
    writr.write("Timer: " + str(timer), font=font_setup)
    timer -= 1
    writr.getscreen().ontimer(countdown, counter_interval)
  else:
    timer_up == True
    writr.write("times up", font = font_setup)

def play(userrounds):
  rounds = 0 
  global score
  score = 0
  print("type the color of the word, be careful and dont type the word!")
  #wn.ontimer(timecountdown, secondlength)
  while userrounds > 7 or userrounds < 1:
    print("the number of rounds can not be greater then 7 or less then 1, please choose a different number")
    userrounds = int(input("how many rounds?(1-7)  "))
  while rounds != userrounds:
    textcolor = random.choice(colorchoices)
    wordcolor = random.choice(colorwords)
    writer.pencolor(textcolor)
    writer.write(wordcolor, font = "Arial")
    attempt = input("guess:  ")
    #print(attempt)
    if attempt == textcolor:
      score += 1
    writer.clear()
    rounds = rounds + 1
  print("your score was: " + str(score) + " out of " + str(userrounds))
  return score

def calcscore():
  global score
  quotient = int(score) / int(userrounds)
  percent = quotient *100
  print("Your percentage correct is " + str(percent) + "%")

wn.ontimer(countdown, counter_interval) 

def go():
  if yorn == "Y":
    play(userrounds)
    calcscore()
    print("thanks for playing, reload the program to play again!  ")
  if yorn == "N":
    print("alright, goodbye!")

go()
wn.update()
wn.mainloop()