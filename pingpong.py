
from flask_socketio import SocketIO,send
import random
from flask import Flask
from numpy import broadcast
import time
px=[2,-2]
h=[]
app=Flask(__name__)
s = SocketIO(app, cors_allowed_origins="*")
x=0
y=0
a=2
b=2
b1=300
b2=300
dir1=0
dir2=0
score1,score2=0,0
@s.on('connect')
def d(msg):
    global x,a,b,y,b1,b2,score1,score2
    b1=300
    b2=300
    score1=0
    score2=0
    b=random.choice(px)
    a=random.choice(px)
    x=random.randint(1,699)
    y=random.randint(1,699)
    
    print('connected')
@s.on('dir')
def dir(a):
    global dir1
    dir1=a
@s.on('dir2')
def di(b):
    global dir2
    dir2=b  
@s.on('left')
def change():
    global a,b,x,y,b1,b2,score1
    b=random.choice(px)
    a=random.choice(px)
    x=random.randint(400,450)
    y=random.randint(400,450)
    b1,b2=300,300
    score1=score1+1
@s.on('right')
def right():
    global a,b,x,y,b1,b2,score2
    b=random.choice(px)
    a=random.choice(px)
    x=random.randint(400,450)
    y=random.randint(400,450)
    b1,b2=300,300
    score2=score2+1
    print('right')

@s.on('up')
def up():
    global b
    b=-2
    print('up')

@s.on('down')
def right():
    global b
    b=2
    print('down')

@s.on('flipx')
def flip():
    global a
    a=-2
    print('flipfsjdhfsdfsadg')

@s.on('bar1up')
def barup(): 
    global b1
    if (b1<600):
        b1=b1+10   
@s.on('bar2up')
def bar2up(): 
    global b2
    if (b2<600):
        b2=b2+10 
@s.on('bar2down')
def bar2down(): 
    global b2
    if (b2>0):
        b2=b2-10         
@s.on('bar1down')
def bardown(): 
    global b1
    if (b1>0):
       b1=b1-10     

@s.on('message')
def send():
    global x,y,a,b1,b,b2,dir1,dir2,score1,score2
    x=x+a
    y=y+b
    
    if (x==30 or x==31 or x==29) and y in range(b1-30,b1+80):
        a=2
        if(dir1==38)and b>0:
            b=b*-1
        elif(dir1==40)and b<0:
            b=b*-1 
    elif (x==845 or x==837 or x==836) and y in range(b2-30,b2+80):
        a=-2
        if(dir2==87)and b>0:
            b=b*-1
        elif(dir2==83)and b<0:
            b=b*-1 
        print('reverse',b2,x,y)
    #print(x,y,b2)    
    
    s.send({'x':x,'y':y,'b1':b1,'b2':b2,'s1':score1,'s2':score2})




if __name__=='__main__':
    s.run(app)
    