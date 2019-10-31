# a122_catch_a_turtle.py
#-----import statements-----
import turtle as turtle
import random
import time
import leaderboard as lb
#-----game configuration----
color = "white"
shape = "turtle"
speed = 0
size = 2
score = 0
font = ("Arial", 70, "normal")
timer = 5
counter_interval = 1000   #1000 represents 1 second
color_list = ["red", "green", "blue", "brown", "black"]
wn = turtle.Screen()
#-----leaderboard variables-----
leaderboard_file_name = "a122_leaderboard.txt"
leader_names_list = []
leader_scores_list = []
player_name = input("Relinquish your birth name")
#-----initialize turtle-----
dead = turtle.Turtle(shape = shape)
dead.turtlesize(size)
dead.speed(speed)
dead.left(90)
dead.color(random.choice(color_list))

scoreman = turtle.Turtle()
scoreman.ht()
scoreman.pu()
scoreman.goto(-370, 270)
scoreman.pencolor("black")

counter =  turtle.Turtle()
counter.ht()
counter.pu()
counter.goto(200, 270)
#-----game functions--------
def dead_clicked(x,y):
    score_change()
    dead.dot(25)
    change_loc()

def change_loc():
    dead.ht()
    dead.pu()
    randx = random.randint(-400, 400)
    randy = random.randint(-300, 300)
    dead.goto(randx, randy)
    dead.pd()
    dead.st()

def score_change():
    global score
    score += 1
    scoreman.clear()
    scoreman.write(score, align="center", font=font)
    #print(score)

def countdown():
  global timer
  counter.clear()
  if timer <= 0:
    counter.goto(0,0)
    counter.write("Time's Up", align="center", font=font)
    manage_leaderboard()
    game_over()
  else:
    counter.write("Timer: " + str(timer), align="center", font=font)
    timer -= 1
    counter.getscreen().ontimer(countdown, counter_interval)

def game_over():
    dead.ht()
    dead.pu()
    dead.clear()
    dead.goto(0, 9000)

    #while True:
    #  wn.bgcolor("red")
    #  time.sleep(1/60)
    #  wn.bgcolor("green")
    #  time.sleep(1/60)
    #  wn.bgcolor("blue")
    #  time.sleep(1/60)

# manages the leaderboard for top 5 scorers
def manage_leaderboard():
  
  global leader_scores_list
  global leader_names_list
  global score
  global scoreman

  # load all the leaderboard records into the lists
  lb.load_leaderboard(leaderboard_file_name, leader_names_list, leader_scores_list)

  # TODO
  if (len(leader_scores_list) < 5 or score > leader_scores_list[4]):
    lb.update_leaderboard(leaderboard_file_name, leader_names_list, leader_scores_list, player_name, score)
    lb.draw_leaderboard(leader_names_list, leader_scores_list, True, scoreman, score)

  else:
    lb.draw_leaderboard(leader_names_list, leader_scores_list, False, scoreman, score)

#-----events----------------
dead.onclick(dead_clicked)

wn.ontimer(countdown, counter_interval) 
wn.mainloop()