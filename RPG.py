import random


import pickle


def save_object(obj, filename):
    with open(filename, 'wb') as output:  # Overwrites any existing file.
        pickle.dump(obj, output, pickle.HIGHEST_PROTOCOL)


def load_object(filename):
    try:
        with open(filename, 'rb') as myinput:
            myobject = pickle.load(myinput)
    except:
        myobject = []
    return myobject

def createrandom():
    names = ["Gary", "Belinda", "Clive", "Oswald", "Mandeep", "Jan"]
    characterclasses = ["Fighter", "Archer", "Wizard"]
    newname = random.choice(names)
    newclass = random.choice(characterclasses)
    if newclass == "Fighter":
        maxstrength = 20
        maxagility = 15
        maxwisdom = 10
    elif newclass == "Archer":
        maxstrength = 15
        maxagility = 20
        maxwisdom = 10
    else:
        maxstrength = 12
        maxagility = 12
        maxwisdom = 20
    newstrength = random.randint(3, maxstrength)
    newagility = random.randint(3,maxagility)
    newwisdom = random.randint(3, maxwisdom)
    newcharacter = [newname, newclass, newstrength, newagility, newwisdom]
    viewcharacter(newcharacter)
    return newcharacter

def viewcharacter(character):
    print("\n\n **************\n")
    print("CURRENT CHARACTER\n\n")
    attributes = ["Name: ", "Class: ", "Strength: ", "Agility: ", "Wisdom: "]
    for i in range(len(character)):
        print(attributes[i], character[i])



def workout(oldstrength, characterclass):
    print("\n\nYou enter the workout yard")
    print("That is a random blue potion on the ground, will you drink it?")
    drink = input("--> ")
    print("Before the workout your strength was", oldstrength)
    if drink.lower() in ["yes", "y"]:
        potioneffect = random.randint(-1,2)
    else:
        potioneffect = 1
    if potioneffect < 1:
        print("You start to feel weak...potion was a bad choice")
    elif potioneffect == 1 and drink.lower() in ["yes", "y"]:
        print("The 'potion' is blueberry juice. Yummy!")
    elif drink.lower() in ["yes", "y"]:
        print("The strength of Zeus flows through you. Time to PUMP SOME IRON!")
    
    if characterclass == "Fighter":
        classeffect = 3
    elif characterclass == "Archer":
        classeffect = 2
    else:
        classeffect = 1
    newstrength = oldstrength + (potioneffect * classeffect)
    print("Your new strength is", newstrength)
    return newstrength




def calculatehitpoints(strength, agility):
    randombonus = random.randint(1,5)
    hitpoints = strength + agility // 2 + randombonus
    return hitpoints

def strikeopponent(attacker, defender, aggressor):
    classbonus = 3
    if aggressor:
        print("\n\n Pick your mode of attack")
        print("1. Sword")
        print("2. Arrow")
        print("3. Fireball")
        mode = input("--> ")
    else:
        print("\n\nDefend yourself!")
        if defender[1] == "Fighter":
            choices = ["1", "2", "2", "3", "3"]
        elif defender[1] == "Archer":
            choices = ["1", "1", "2", "3", "3"]
        else:
            choices = ["1", "1", "2", "2", "3"]
        mode = random.choice(choices)
    if mode == "1":
        print("Sword attack")
        if attacker[1] == "Fighter":
            maxstrike = attacker[2] + classbonus
        else:
            maxstrike = attacker[2]
        if defender[1] == "Fighter":
            maxdefend = defender[2] + classbonus
        else:
            maxdefend = defender[2]
        damage = random.randint(1,maxstrike) - random.randint(1,maxdefend)
        damage = 0
    elif mode == "2":
        print("Arrow attack")
        if attacker[1] == "Archer":
            maxstrike = attacker[3] + classbonus
        else:
            maxstrike = attacker[3]
        if defender[1] == "Archer":
            maxdefend = defender[3] + classbonus
        else:
            maxdefend = defender[3]
        damage = random.randint(1,maxstrike) - random.randint(1,maxdefend)
    elif mode == "3":
        print("Haoduken!")
        if attacker[1] == "Wizard":
            maxstrike = attacker[4] + classbonus * 2
        else:
            maxstrike = attacker[4]
        if defender[1] == "Wizard":
            maxdefend = defender[4] + classbonus * 2
        else:
            maxdefend = defender[4]
        damage = random.randint(1,maxstrike) - random.randint(1,maxdefend)
    else:
        print("You miss, fool")
        damage = 0
    if damage < 0:
        print("Attack highly ineffective")
        return 0
    else:
        return damage


def battle_in_the_arena(player):
    print("\n\n#######ENEMY#########")
    enemy = createrandom()
    enemyhp = calculatehitpoints(enemy[2], enemy[3])
    print("ENEMY STARTS WITH", enemyhp, "HIT POINTS")
    print("\n\n#######PLAYER########")
    viewcharacter(player)
    playerhp = calculatehitpoints(player[2], player[3])
    print("PLAYER STARTS WITH", playerhp, "HIT POINTS")

    
    playerwon = False
    enemywon = False
    
    while not playerwon and not enemywon:
        enemyhp -= strikeopponent(player, enemy, True)
        print("Enemy hit points now", enemyhp)
        if enemyhp <= 0:
            playerwon = True
        else:
            playerhp -= strikeopponent(enemy, player, False)
            print("Player hit points now", playerhp)
            if playerhp <= 0:
                enemywon = True
    return playerwon
        
    


def run_assault_course(oldagility, characterclass):
    print("\n\nYou enter the assault course")
    print("It's raining - that might help your workout or you may get injured. Do you continue? ")
    continueworkout = input("--> ")
    print("Before the workout your agility was", oldagility)
    if continueworkout.lower() in ["yes", "y"]:
        raineffect = random.randint(-1,2)
    else:
        raineffect = 0
    if raineffect < 1:
        print("The slippy slidey conditions cause you to sprain your ankle. Ouchy!")
    elif raineffect == 1 and continueworkout.lower() in ["yes", "y"]:
        print("Just as your start the assault course the rain stops and the sun comes out. Result!")
    else:
        print("Battling through the rain, you feel like Aragon at Helm's Deep. Except you can't read so you don't know who that is")
    
    if characterclass == "Archer":
        classeffect = 3
    elif characterclass == "Fight":
        classeffect = 2
    else:
        classeffect = 1
    newagility = oldagility + (raineffect * classeffect)
    print("Your new agility is", newagility)
    return newagility


def read_a_book(oldwisdom, characterclass):
    print("\n\nYou enter the library")
    print("Mrs Scott tells you about the accelerated reader program - will you join it?")
    acceleratedreader = input("--> ")
    print("Before the reading the book your wisdom was", oldwisdom)
    if acceleratedreader.lower() in ["yes", "y"]:
        acceleratedreadereffect = random.randint(2,5)
        print("You feel your brain swelling inside your skull, great choice")
    else:
        acceleratedreadereffect = 0
        print("Y tho?")
   
    
    if characterclass == "Wizard":
        classeffect = 3
    elif characterclass == "Archer":
        classeffect = 2
    else:
        classeffect = 1
    newwisdom = oldwisdom + (acceleratedreadereffect * classeffect)
    print("After reading a random book your new wisdom is", newwisdom)
    print(newwisdom)
    return newwisdom

def levelup(character):
    print("\n\n Please select an attribute to increase")
    print("1. Strength")
    print("2. Agility")
    print("3. Wisdom")
    option = input("--> ")
    if option == "1":
        character[2] += 1
    elif option == "2":
        character[3] += 1
    elif option == "3":
        character[4] += 1
    else:
        print("Level up failed")
    viewcharacter(character)
    return character
    

def menu():
    keepgoing = True
    print("\n\n*** Welcome to the World's finest role playing game ***")

    
    print("Would you like to load in your data from your last game?")
    doload = input("--> ")
    if doload.lower() in ["y", "yes"]:
        character = load_object("current_character.pkl")
        character_record = load_object("character_record.pkl")
        if character == []:
            print("Sorry, we could not find any previous data for you")
            character = createrandom()
    else:
        character = createrandom()
        character_record = []


        
    while keepgoing:
        print("\n\n *********************************\n\n")
        print("Please choose your option")
        print("1. Create a new random character and store old character")
        print("2. View the current character")
        print("3. Work out (increase strength)")
        print("4. Run assault course (increase agility)")
        print("5. Read a book (increase wisdom)")
        print("6. Battle in the arena")
        print("7. View past characters")
        print("Q. Quit")
        option = input("--> ")
        if option == "1":
            character_record.append(character)
            character = createrandom()
        elif option == "Q":
            keepgoing = False
            save_object(character, "current_character.pkl")
            save_object(character_record, "character_record.pkl")
        elif character[0] != "Default":
            if option == "2":
                viewcharacter(character)
            elif option == "3" and character[0]:
                character[2] = workout(character[2], character[1])
            elif option == "4" and character[0]:
                character[3] = run_assault_course(character[3], character[1]) 
            elif option == "5" and character[0]:
                character[4] = read_a_book(character[4], character[1])
            elif option == "6":
                if battle_in_the_arena(character):
                    character = levelup(character)
                else:
                    print("Better luck next time")
                    character_record.append(character)
                    character = createrandom()

            elif option == "7":
                print("\n\n**** PAST CHARACTERS ****\n")
                for oldcharacter in character_record:
                    viewcharacter(oldcharacter)

                

            else:
                print("Sorry, that option is not available at this time")
            
                
        else:
            print("Please create a character to procede")

menu()
    
    
