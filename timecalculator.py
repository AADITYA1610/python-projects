from time import *
import random as rm

def error(par,us):
    er = 0
    for i in range(len(par)):
        try:
            if par[i] != us[i]:
                er += 1
        except :
            er += 1
    return er
def type_speed(ts,te,ui):
    delay = round(te - ts,2)
    speed = len(ui)/delay
    return round(speed)

sample = ["Education is the most powerful weapon you can use to change the world.","You must be the change you wish to see in the world.","Success is the sum of all efforts, repeated day-in & day out.","Failure will never overtake me if my determination to succeed is strong enough.","In the end, it's not the years in your life that count. It's the life in your years."]
test_line = rm.choice(sample)
print()
print("\t ","*"*30)
print("\twelcome to typing speed calculator!!\t")
name  = input("enter your name: ")
fname = f"{name}tsp.txt"
choice = input("want to know your previous speeds? yes/no : ")
if choice.lower() == "yes":
    try:
        f = open(fname,"r")
        data = f.read()
        print(data)
    except FileNotFoundError:
        print("this is your first attempt")
else:
    print("ok")
print()
while True:
    ck = input("Start the test : yes / no : ")
    if ck.lower()== "yes":
        print("here's the line to test your typing speed:")
        print()
        print(test_line)
        print()
        print()
        t1 = time()
        user = input("start typing!\n-->")
        t2 = time()
        print()
        speed = type_speed(t1,t2,user)
        mistakes = error(test_line,user)

        print(f"your typing speed is : {speed} w/s")
        print(f"total no. of errors : {mistakes}")
        
        f = open(fname,"a")
        f.write(f"your typing speed is : {speed}w/s,")
        f.write(f"with {mistakes} errors")
        f.write("\n")
        f.close()
    
    
    elif ck.lower() == "no":
        print("thank you")
        break
    else:
        print("wrong input")

print("\t ","*"*30)




    

