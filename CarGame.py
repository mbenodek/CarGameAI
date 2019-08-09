import pyttsx3 ## install this saying pip install pyttsx3

engine = pyttsx3.init()

userInput= ""
isCarStarted = False

engine.say(
    "Welcome to Biri you out of work good for nothing,disturbed and well something to every nothing person,I did not want you here but here we are,Well let's begin the horror that you are now....ho ho ho ")
engine.runAndWait()

while True:

    userInput= input(">").lower()
    if userInput == "start":
        if isCarStarted:
            carStarted = "Car is already started you imbecile...why would you start it again"
            engine.say(carStarted)
            engine.runAndWait()
            ##print("Car is already started you imbecile...why would you start it again")

        else :
            isCarStarted = True
            carStarted = "Car started dude lets go for a ride....I know you are all alone and this is the only joy you will ever have"
            engine.say(carStarted)
            engine.runAndWait()
            #print(f'Car started dude lets go for a ride ')


    elif userInput == "stop":
        if not isCarStarted :
            carStarted = "You are worstest driver i have ever seen....The car is stopped and you are  still trying to stop it...Bro use your brain.... sorry i forgot you don't have one...My Bad"
            engine.say(carStarted)
            engine.runAndWait()

            #print("You are worst driver i have ever seen the car is stopped and you are trying still stopping it")

        else :
            isCarStarted = False
            carStarted = "Car is stopped... why would you stop the car.....Man you need to get a life. You stay at home all day and do this shit anyways.GET OUT............ and start the car"
            engine.say(carStarted)
            engine.runAndWait()
            #engine.say(print("Car is stopped... why would you stop the car "))
           # engine.runAndWait()



    elif userInput =="help":
        carStarted = """You seem to me like someone who will always need help. Here are your options and stop bothering me you f***k**in beautiful person.. 
First option is quit - because you are a quitter you can use this option.
Second option is start - This option will let you start the car but a stupid person like you may not even understand what i am saying here.
last option is stop - I think you should stop you worthless piece of .... well let it be just stoppppppp,I am  disappointed but i guess your use to it by now. ... So stop mate"""
        engine.say(carStarted)
        engine.runAndWait()

       ## print("""
##You seem to me like someone who will always need help. Here are your options and stop bothering me you f***k**in i mean freaking  person
##it - because you are a quitter you can use this option
##start - Yaay !! Lets go for a long drive
##stop - I am  disappointed but i guess you are use to it by now
 ##       """)

    elif userInput == "quit":
        carStarted = " Well i knew you are quitter and quitting is all you do,Get Lost"
        engine.say(carStarted)
        engine.runAndWait()
        break

    else:
        carStarted = "Check what you are typing you moron , It's not Westros where everything goes if you don't know anything you Breaking bad idiot  John Snow just type help and yes leave me alone"
        engine.say(carStarted)
        engine.runAndWait()
        ##print("Check what you are typing you moron , if you don't know anything like John Snow just type help ")

