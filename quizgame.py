print("welcome to the quiz game")
print("every answer must be lower case letters")
playing=input("do you want to paly a game?")
if(playing!="yes"):
    quit()
print("okay! lets play a game:)")
points=0
answer=input("who is the indian have most instagram followers?")
if(answer=="virat kohli"):
    print("yes! its correct")
    points+=1
else:
    print("incorrect")
    points=0
answer=input("what is the capital of australia?")
if(answer=="canberra"):
    print("yes! its correct")
    points+=1
else:
    print("incorrect")
    points=0
answer=input("what is uno stands for?")
if(answer=="united nation organisation"):
    print("yes! its correct")
    points+=1
else:
    print("incorrect")
    points=0
answer=input("who is the president of uk?")
if(answer=="rishi sunak"):
    print("yes! its correct")
    points+=1
else:
    print("incorrect")
    points=0
answer=input("what is the director of titanic?")
if(answer=="james cameron"):
    print("yes! its correct")
    points+=1
else:
    print("incorrect")
    points=0
print("thank you playing game")
if(points==1 or points==2):
    print(f"you got {points} :""pora poyyi chaduvuko")
elif(points==3 or points==4):
    print(f"you got {points} :""good man keep going")
else:
    print(f"you got {points} :""a aa aaa topper bolthey")


