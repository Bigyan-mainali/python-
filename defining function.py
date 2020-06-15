def take(k):#defining function
    if (k==1):#1=roshan making the condition to meet to be roshan
        req=int(input('enter your interest, 0 for food and 1 for exercise:'))#entering for food or exercise
        if (req==1):          #if 1,1=exercise
            value=input('type here:\n')#giving instruction
            with open("Roshan_ex.txt","a") as op:#opening folder
                op.write(str([str(getdate())]) + ": " + value + "\n")#appending on file
                print("The item has added to the table.")#printing information to user.
        elif (req==0):#if request =0 , 0=food
            value=input('type here:\n')#asking about food
            with open("Roshan_food.txt","a") as op:#opening file
                op.write(str([str(getdate())]) + ": " + value + "\n")#appending on the file
                print('The item has added to the table.')
    elif (k==2):#2=harry making condition to be harry
        req=int(input('enter your interest, 0 for food and 1 for exercise:'))#entering for food or exercise
        if (req==1):#if 1,1=exerciseype1 =
            value=input('type here:\n') # giving instruction
            with open("Harry_ex.txt", "a") as op:  # opening folder
                op.write(str([str(getdate())]) + ": " + value + "\n") # appending on file
                print("The item has added on the table.")# printing information to user.
        elif (req==0):  # if request =0 , 0=food
            value = input('type here:\n') # asking about food
            with open("Harry_food.txt", "a") as op:  # opening file
                op.write(str([str(getdate())]) + ": " + value + "\n")# appending on the file
                print("The item has added to the table.")
    elif (k==3):
        req=int(input('enter your interest, 0 for food and 1 for exercise:'))#entering for food or exercise
        if (req==1):#if 1,1=exercise
            value=input('type here:\n')#giving instruction
            with open("Bigyan_ex.txt","a") as op:#opening folder
                op.write(str([str(getdate())]) + ": " + value + "\n")#appending on file
                print("The item has added to the table.")#printing information to user.
        elif req==0:#if request =0 , 0=food
            value=input('type here:\n')#asking about fooa
            with open("Bigyan_food.txt","a") as op:#opening file
                op.write(str([str(getdate())]) + ": " + value + "\n")#appending on the file
                print("The item has added to the table.")

def rev(k):
    if k == 1:
        req = int(input("enter 1 for excersise and 2 for food"))
        if (req == 1):
            with open("Harry_ex.txt") as op:
                for i in op:
                    print(i, end="")
        elif (req == 2):
            with open("Harry_food.txt") as op:
                for i in op:
                    print(i, end="")
    elif (k == 2):
        req = int(input("enter 1 for excersise and 2 for food"))
        if (req == 1):
            with open("Roshan_ex.txt") as op:
                for i in op:
                    print(i, end="")
        elif (req == 2):
            with open("Roshan_food.txt") as op:
                for i in op:
                    print(i, end="")
    elif (k == 3):
        req = int(input("enter 1 for excersise and 2 for food"))
        if (req == 1):
            with open("Bigyan_ex.txt") as op:
                for i in op:
                    print(i, end="")
        elif (req == 2):
            with open("Bigyan_food.txt") as op:
                for i in op:
                    print(i, end="")
    else:
        print("You are not resistered in our club. Thank You.")
def getdate():
    import datetime
    return datetime.datetime.now()
print("********Health Management System**********")
job = int(input('what do you want to do? retrieve, type-0: log, type-1: '))
if (job==1):
    k=int(input('what is your name? Roshan-1, Harry-2 and Bigyan-3'))
    take(k)
elif (job==0):
    k=int(input('what is your name? Roshan-1, Harry-2 and Bigyan-3:'))
    rev(k)
#changing datetime into string from gatedate function.