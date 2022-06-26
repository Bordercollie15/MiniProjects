import turtle                        # Gets a turtle
from datetime import datetime
import pytz
from pytz import country_timezones   #Useful if you want to switch out values for different time zones around the world
from pytz import timezone, utc
#print(' '.join(country_timezones('US'))) #Use this if you want to see what time zones you can choose
date = datetime.now(tz=pytz.utc)
now = datetime.now()
local_now = now.astimezone()
local_tz = local_now.tzinfo
local_tzname = local_tz.tzname(local_now)#Get your local timezone's abbreviation

wn = turtle.Screen()                 # Gets window for turtle
wn.bgcolor("white")                  # Sets background color to white
t = turtle.Turtle()                  # Names the turtle "t"
t.pensize(2)
t.turtlesize(0.5)
t.shape("circle")                   # Turtle shape
t.color("pink")                     # Makes the turtle pink
t.pencolor("black")                 # Makes the lines drawn black
t.right(45)
turtle.write(local_tzname, move=True, align='left', font=('Monaco', 50, 'normal'))

year = now.year 
month = now.month 
day = now.day
hour = now.hour
minute = now.minute

def write_time_standardly(hour,minute):    #Function for writing the time
    '''writes time in standard form ex. 9:30 PM'''
    outstring = ''
    addition = 'AM'
    if hour >12 and hour != 24:
        outstring+=str(hour-12)
        addition = 'PM'
    elif hour ==12:
        outstring+='12'
        addition = 'PM'
    else:
        outstring+=str(hour)
    outstring+=':'
    if minute<10:
        outstring+=str(0)
    outstring+=str(minute)
    outstring+=' '
    outstring+=addition
    return outstring

second = now.second
t.penup()                            # lifts pen so the marks are not connected
t.right(90)
t.forward(40)
t.left(90)
size = 40
t.speed(10)
for i in range(12):                  # Makes the tick marks on the clock
    t.stamp()             
    t.forward(size)      
    t.right(30)           
t.right(75)
t.forward(80)
t.right(150)
h = 30 * hour                        # Finds the angle of the clock hour hand
m = 6 * minute                       # Finds the angle of the minute hand

t.pendown()                          # Lowers the pen so we can draw the hands of the clock
t.stamp()                            #Stamps a circle in the center of the clock
t.shape("classic")                   #An arrow shape for the hands of the clock.            

t.right(m)                           # Drawing the minute hand
t.forward(65)
t.turtlesize(1)
t.stamp()
t.forward(-65)
t.right(360-m)
t.right(h+m/12)                      # Drawing the hour hand
t.forward(40)
t.stamp()
t.backward(40)

t.hideturtle()                       # Makes the turtle invisible
t.penup()
t.setpos(-50,70)
t.pendown()
t.write("The time is "+write_time_standardly(hour,minute), move=True, align='left', font=('Monaco', 15, 'normal'))
t.penup()
t.setpos(-50,110)
t.pendown()
t.write("Today is "+str(month)+"/"+str(day)+"/"+str(year), move=True, align='center', font=('Courier', 15, 'normal'))

t.penup()
t.showturtle()
t.setheading(90)
t.forward(80)
t.setheading(0)
t.forward(180)
t.pendown()

for i in range(0,4): #Draws box
    t.right(90)
    t.forward(400)
t.hideturtle()
t.setheading(180)
t.forward(100)
t.setheading(0)
subtractthis=90
subtractthat=0

for tizn in ['US/Pacific','US/Central','US/Eastern']: #Add more time zones if needed, or exchange for different zones
    if date.astimezone(timezone(tizn)).hour != hour:       #Shows what the time is in different time zones
        local_now = date.astimezone(timezone(tizn))
        local_tz = local_now.tzinfo
        local_tzname = local_tz.tzname(local_now)
        t.penup()
        t.setpos(-20-subtractthat,-subtractthis)
        t.forward(50)
        t.pendown()
        subtractthis+=50
        subtractthat+=10
        tzhour = date.astimezone(timezone(tizn)).hour
        tzminute = date.astimezone(timezone(tizn)).minute
        t.write("In "+str(local_tzname)+" it is "+write_time_standardly(tzhour,tzminute), move=True, align='left', font=('Monaco', 12, 'normal'))
wn.mainloop()

