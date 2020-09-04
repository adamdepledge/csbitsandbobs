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


class Character:

    def __init__(self):
        self.possiblenames = ["Gary", "Belinda", "Clive", "Oswald", "Mandeep", "Jan"]
        self.possibleclasses = ["Fighter", "Archer", "Wizard"]
        self.charactername = random.choice(self.possiblenames)
        self.characterclass = random.choice(self.possibleclasses)
        if self.characterclass == "Fighter":
            maxstrength = 20
            maxagility = 15
            maxwisdom = 10
        elif self.characterclass == "Archer":
            maxstrength = 15
            maxagility = 20
            maxwisdom = 10
        else:
            maxstrength = 12
            maxagility = 12
            maxwisdom = 20
        self.strength = random.randint(3, maxstrength)
        self.agility = random.randint(3, maxagility)
        self.wisdom = random.randint(3, maxwisdom)
        self.hitpoints = self.strength + self.agility // 2 + random.randint(1,5)


    def viewcharacter(self):
        print("\n\n **************\n")
        print("CURRENT CHARACTER\n\n")
        print("Name:  ", self.charactername)
        print("Class: ", self.characterclass)
        print("Strength:", self.strength)
        print("Agility :", self.agility)
        print("Wisdom  :", self.wisdom)

    def getname(self):
        return self.charactername

    def getclass(self):
        return self.characterclass

    def getstrength(self):
        return self.strength

    def getagility(self):
        return self.agility

    def getwisdom(self):
        return self.wisdom
    
    def battledamage(self, damage):
        self.hitpoints -= damage
        
    def resethitpoints(self):
        self.hitpoints = self.strength + self.agility // 2 + random.randint(1,5)

    def gethitpoints(self):
        return self.hitpoints
   

    def workout(self):
        print("\n\nYou enter the workout yard")
        print("That is a random blue potion on the ground, will you drink it?")
        drink = input("--> ")
        print("Before the workout your strength was", self.strength)
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
        
        if self.characterclass == "Fighter":
            classeffect = 3
        elif self.characterclass == "Archer":
            classeffect = 2
        else:
            classeffect = 1
        self.strength = self.strength + (potioneffect * classeffect)
        print("Your new strength is", self.strength)
        self.resethitpoints()

    

    def run_assault_course(self):
        print("\n\nYou enter the assault course")
        print("It's raining - that might help your workout or you may get injured. Do you continue? ")
        continueworkout = input("--> ")
        print("Before the workout your agility was", self.agility)
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
        
        if self.characterclass == "Archer":
            classeffect = 3
        elif self.characterclass == "Fight":
            classeffect = 2
        else:
            classeffect = 1
        self.agility = self.agility + (raineffect * classeffect)
        print("Your new agility is", self.agility)
        self.resethitpoints()



    def read_a_book(self):
        print("\n\nYou enter the library")
        print("Mrs Scott tells you about the accelerated reader program - will you join it?")
        acceleratedreader = input("--> ")
        print("Before the reading the book your wisdom was", self.wisdom)
        if acceleratedreader.lower() in ["yes", "y"]:
            acceleratedreadereffect = random.randint(2,5)
            print("You feel your brain swelling inside your skull, great choice")
        else:
            acceleratedreadereffect = 0
            print("Y tho?")
       
        
        if self.characterclass == "Wizard":
            classeffect = 3
        elif self.characterclass == "Archer":
            classeffect = 2
        else:
            classeffect = 1
        self.wisdom = self.wisdom + (acceleratedreadereffect * classeffect)
        print("After reading a random book your new wisdom is", self.wisdom)


    def levelup(self):
        print("\n\n Please select an attribute to increase")
        print("1. Strength")
        print("2. Agility")
        print("3. Wisdom")
        option = input("--> ")
        if option == "1":
            self.strength += 1
        elif option == "2":
            self.agility += 1
        elif option == "3":
            self.wisdom += 1
        else:
            print("Level up failed")
        self.viewcharacter()




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
        if defender.getclass() == "Fighter":
            choices = ["1", "2", "2", "3", "3"]
        elif defender.getclass() == "Archer":
            choices = ["1", "1", "2", "3", "3"]
        else:
            choices = ["1", "1", "2", "2", "3"]
        mode = random.choice(choices)
    if mode == "1":
        print("Sword attack")
        if attacker.getclass() == "Fighter":
            maxstrike = attacker.getstrength() + classbonus
        else:
            maxstrike = attacker.getstrength()
        if defender.getclass() == "Fighter":
            maxdefend = defender.getstrength() + classbonus
        else:
            maxdefend = defender.getstrength()
        damage = random.randint(1,maxstrike) - random.randint(1,maxdefend)
        damage = 0
    elif mode == "2":
        print("Arrow attack")
        if attacker.getclass() == "Archer":
            maxstrike = attacker.getagility() + classbonus
        else:
            maxstrike = attacker.getagility()
        if defender.getclass() == "Archer":
            maxdefend = defender.getagility() + classbonus
        else:
            maxdefend = defender.getagility()
        damage = random.randint(1,maxstrike) - random.randint(1,maxdefend)
    elif mode == "3":
        print("Haoduken!")
        if attacker.getclass() == "Wizard":
            maxstrike = attacker.getwisdom() + classbonus * 2
        else:
            maxstrike = attacker.getwisdom()
        if defender.getclass() == "Wizard":
            maxdefend = defender.getwisdom() + classbonus * 2
        else:
            maxdefend = defender.getwisdom()
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
    enemy = Character()
    print("ENEMY STARTS WITH", enemy.gethitpoints(), "HIT POINTS")
    print("\n\n#######PLAYER########")
    player.viewcharacter()
    print("PLAYER STARTS WITH", player.gethitpoints(), "HIT POINTS")

    
    playerwon = False
    enemywon = False
    
    while not playerwon and not enemywon:
        enemy.battledamage(strikeopponent(player, enemy, True))
        print("Enemy hit points now", enemy.gethitpoints())
        if enemy.gethitpoints() <= 0:
            playerwon = True
        else:
            player.battledamage(strikeopponent(enemy, player, False))
            print("Player hit points now", player.gethitpoints())
            if player.gethitpoints() <= 0:
                enemywon = True
    return playerwon
        
    








    

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
            playercharacter = Character()
    else:
        playercharacter = Character()
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
            character_record.append(playercharacter)
            playercharacter = Character()
        elif option == "Q":
            keepgoing = False
            save_object(playercharacter, "current_character.pkl")
            save_object(character_record, "character_record.pkl")
        elif option == "2":
            playercharacter.viewcharacter()
        elif option == "3":
            playercharacter.workout()
        elif option == "4":
            playercharacter.run_assault_course()
        elif option == "5" :
            playercharacter.read_a_book()
        elif option == "6":
            if battle_in_the_arena(playercharacter):
                playercharacter.levelup()
            else:
                print("Better luck next time")
                character_record.append(playercharacter)
                playercharacter = Character

        elif option == "7":
            print("\n\n**** PAST CHARACTERS ****\n")

            for oldcharacter in character_record:
                oldcharacter.viewcharacter()

                

        else:
            print("Sorry, that option is not available at this time")
            
                
menu()
    
    
