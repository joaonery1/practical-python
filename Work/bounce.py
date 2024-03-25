# bounce.py
# A rubber ball is dropped from a height of 100 meters
# bounce 3/5 height
#
# Exercise 1.5


height = 100 #meters
quicks = 3/5
height_ball = height * quicks
bounces = 10
i = 0
#print(height_ball)
while i <10 :
    height_ball = round(height_ball,4)
    print(height_ball)
    height_ball = height_ball * quicks
    i = i +1

