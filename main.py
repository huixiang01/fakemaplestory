import random
import time
from libdw import sm
import sys

# Dedicated to the millenials and pioneer generation Z out there who wants to feel young again.
# This is fake maplestory version back when grinding is the thing.(like when I was in primary 2? year 2006?) --with a twist of singapore-ness and pokemon memes -- Hope you like it.
# This is built with simple state machine and class with public attribute in python.
# Due to assignment criteria, we need to write codes in single file. I wish that we can seperate into different files. 1000 lines of codes is so confusing.

class Player():
    def __init__(self, name):
        self.maxhealth = 100
        self.health = 70
        self.level = 1
        self.potion = 0
        self.monstercount = 0
        self.levellimit = 5
        self.mesos = 100
        self.name = name
        self.skills = ["Attack"]
        self.job = "Beginner"
    
    def attack(self, monster):
        damage = random.randint(self.level * 10, self.level * 20)
        monster.health -= damage
        reply = random.randint(1,5) # varied replies for entertainment
        if reply == 1:
            print("HAI YAH! {} has attacked {}.".format(self.name, monster.name))
            time.sleep(1)
            print("{} gratefully recieves {} damage.".format(monster.name, damage))
        elif reply == 2:
            print("PIAK! {} auntie slapped {} with his hand. Wait wut?".format(self.name, monster.name))
            time.sleep(1)
            print("{} is ashamed of himself and absorbed {} damage.".format(monster.name, damage))
        elif reply == 3:
            print("{} has farted on {}.".format(self.name, monster.name))
            time.sleep(1)
            print("{} cannot tahan so he has to smell it. Bobian lo. {} takes in {} damage.".format(monster.name, monster.name, damage))
        elif reply == 4:
            print("{} skillfully sliced {}".format(self.name, monster.name))
            time.sleep(1)
            print("ORH HOR, you made {} cry. But who cares? {} kenna {} damage.".format(monster.name, monster.name, damage))
        elif reply == 5:
            print("{} uses normal attack.".format(self.name)) # pokemon quotes.
            time.sleep(1)
            if damage < self.level * 14:
                print("It is not effective... {} sustains {} damage.".format(monster.name, damage))
            elif damage >= self.level * 14:
                print("It is effective! {} sustains {} damage.".format(monster.name, damage))
            elif damage >= self.level * 18:
                print("It is super effective! {} sustains {} damage.".format(monster.name, damage))
        time.sleep(1)

    def dpotion(self):
        if self.potion > 0:
            self.health += 50
            if self.maxhealth <= self.health:
                recovered_health = 50 - (self.health - self.maxhealth)
                self.health = self.maxhealth
            else:
                recovered_health = 50
            self.potion -= 1
            print("{} has drunk 1 health potion and recovered {} health.".format(self.name, recovered_health))
        else:
            print("GOD DANG IT. No potions left.")

    def kill(self, monster):
        self.monstercount += 1
        mesos = random.randint(self.level * 10, self.level * 15)
        self.mesos += mesos
        print("You have slayed {}!".format(monster.name))
        print("You have earned {} mesos".format(mesos))
        print("Experience: {}%".format(min(100, round(round(self.monstercount/self.levellimit, 2) * 100, 1))))
        if self.levellimit <= self.monstercount: # level up
            self.level += 1
            self.levellimit += 2 # level up difficulty rises, TIME FOR GRINDING!!!!
            if self.job == "Warrior":
                mult = 1.5
            elif self.job == "Magician":
                mult = 1.1
            elif self.job == "Bowman":
                mult = 1.3
            elif self.job == "Thief":
                mult = 1.4
            elif self.job == "Beginner":
                mult = 1
            self.maxhealth += 20 * mult
            self.health = self.maxhealth
            print("{} has leveled up to {}! Congratz!!!\nYour health is {}.".format(self.name, self.level, self.health))
            self.monstercount = 0

    def bpotion(self):
        if self.mesos >= 20:
            self.mesos -= 20
            self.potion += 1
            print("You now have {} potion(s)! You have {} mesos left.".format(self.potion, self.mesos))
        else:
            print("Dun play play! You no mesos right? tsk.")
    
    def spotion(self):
        if self.potion >= 1:
            self.mesos += 15
            self.potion -= 1
            print("You now have {} potion(s)! You have {} mesos left.".format(self.potion, self.mesos))
        else:
            print("Ops! You don't have potions to sell.")
    
    def death(self):
        self.monstercount -= self.levellimit/10
        print("Ohhhh noooo... {} has died. Play again?".format(self.name))
        print("You have lost 10% experience.")

    # I am not using super class since the data that player has will be lost. Hence, I am defining the class functions here.
    def jobadvancement(self):
        jobs = ["Warrior", "Magician", "Bowman", "Thief"]
        print("""
        Inside the shop, there are four lengendary job instructors that you have been seeking for:
        What jobs do you want to choose:
        1. Warrior
        2. Magician
        3. Bowman
        4. Thief
        """)
        inp = input()
        while ((inp.isdigit()) + (inp in jobs) != 1):
            if inp == "exit":
                print(exit_message)
                time.sleep(20)
                sys.exit()
            print("Choose a job by typing the number beside")
            inp = input()
        if inp.isdigit():
            self.job = jobs[int(inp) - 1]
        if inp in jobs:
            self.job = inp
        
        # job advancement
        if self.job == "Warrior":
            self.advwarrior()
        elif self.job == "Magician":
            self.advmagician()
        elif self.job == "Thief":
            self.advthief()
        elif self.job == "Bowman":
            self.advbowman()

        print("            \n{} has advanced to {}. More Adventure awaits!\n".format(self.name, self.job))

        return True
    # warrior
    def advwarrior(self):
        self.skills.extend(["DoubleSlash", "SlashBlast"])
        self.maxhealth *= 2
        self.health = self.maxhealth
    
    def doubleslash(self, monster):
        damage = random.randint(self.level * 10, self.level * 20)
        monster.health -= damage
        print("{} slashes {}. Monster gets {} damage.".format(self.name, monster.name, damage))
        time.sleep(0.2)
        damage = random.randint(self.level * 10, self.level * 20)
        monster.health -= damage
        print("{} slashes {} again. Monster gets {} damage.".format(self.name, monster.name, damage))

    def slashblast(self, monster):
        damage = random.randint(self.level * 10, self.level * 30)
        monster.health -= damage
        print("{} blasts on {}. Monster gets {} damage".format(self.name, monster.name, damage))

    # magician
    def advmagician(self):
        self.skills.extend(["EnergyBolt", "MagicCross"])
        self.health *= 1.2
        self.health = self.maxhealth

    def energybolt(self, monster):
        damage = random.randint(self.level * 15, self.level * 25)
        monster.health -= damage
        print("{} blasts on {}. Monster gets {} damage".format(self.name, monster.name, damage))

    def magiccross(self, monster):
        damage = random.randint(self.level * 15, self.level * 25)
        monster.health -= damage
        print("{} crosses {}. Monster gets {} damage.".format(self.name, monster.name, damage))
        time.sleep(0.2)
        damage = random.randint(self.level * 10, self.level * 15)
        monster.health -= damage
        print("{} crosses {} again. Monster gets {} damage.".format(self.name, monster.name, damage))

    # thief
    def advthief(self):
        self.skills.extend(["BanditSlash", "LuckySeven"])
        self.health *= 1.5
        self.health = self.maxhealth

    def banditslash(self, monster):
        damage = random.randint(self.level * 15, self.level * 35)
        monster.health -= damage
        print("{} slashes at {}. Monster gets {} damage".format(self.name, monster.name, damage))

    def luckyseven(self, monster):
        damage = random.randint(self.level * 15, self.level * 30)
        monster.health -= damage
        print("{} threw steely at {}. Monster gets {} damage.".format(self.name, monster.name, damage))
        time.sleep(0.2)
        damage = random.randint(self.level * 15, self.level * 30)
        monster.health -= damage
        print("{} threw steely at {} again. Monster gets {} damage.".format(self.name, monster.name, damage))

    # bowman
    def advbowman(self):
        self.skills.extend(["DoubleArrow", "ArrowBlow"])
        self.health *= 1.8
        self.health = self.maxhealth

    def arrowblow(self, monster):
        damage = random.randint(self.level * 25, self.level * 30)
        monster.health -= damage
        print("{} shoots at {}. Monster gets {} damage".format(self.name, monster.name, damage))

    def doublearrow(self, monster):
        damage = random.randint(self.level * 15, self.level * 25)
        monster.health -= damage
        print("{} shoots at {}. Monster gets {} damage.".format(self.name, monster.name, damage))
        time.sleep(0.2)
        damage = random.randint(self.level * 20, self.level * 25)
        monster.health -= damage
        print("{} shoots at {} again. Monster gets {} damage.".format(self.name, monster.name, damage))
    

class Monster():
    def __init__(self, name, player):
        self.level = random.randint(max(1, player.level - 3), player.level) # can't have negative number
        self.health = 40 + self.level * 15
        self.name = name

    def attack(self, player):
        damage = random.randint(self.level * 8, self.level * 16)
        player.health -= damage
        reply = random.randint(1,5) # varied replies for entertainment
        if reply == 1:
            print("{} kisses {}.".format(self.name, player.name))
            time.sleep(1)
            print("Ewwwww. Disgusting. {} gets {} damage.".format(player.name, damage))
        elif reply == 2:
            print("{} unleashes its innermost anger on {}.".format(self.name, player.name))
            time.sleep(1)
            print("Okay {} diam diam and guai guai takes {} damage.".format(player.name, damage))
        elif reply == 3:
            print("{} touches {}.".format(self.name, player.name))
            time.sleep(1)
            print("Wa touch cute {} so painful. Cannot siah. {} takes {} damage.".format(player.name, player.name, damage))
        elif reply == 4:
            print("{} poke {}".format(self.name, player.name))
            time.sleep(1)
            print("{} cannot ignore the intense cuteness. Argh. Heart pain. {} kenna {} damage.".format(player.name, player.name, damage))
        elif reply == 5:
            print("{} uses normal attack.".format(self.name)) # pokemon quotes.
            time.sleep(1)
            if damage <= player.level * 10:
                print("It is not effective... {} sustains {} damage.".format(player.name, damage))
            elif damage > player.level * 10:
                print("It is effective! {} sustains {} damage.".format(player.name, damage))
            elif damage >= player.level * 14:
                print("It is super effective! {} sustains {} damage.".format(player.name, damage))
        time.sleep(1)
        player.health = max(player.health, 0) # no negative health
        self.health = max(self.health, 0)
        print('{}\'s health : {}'.format(player.name, player.health))
        print('{}\'s health : {}'.format(self.name, self.health))

    def death(self):
        print("{} has died.".format(self.name))

class Shop():
    def dpotion(self):
        print("Each potion heals 50 health!")
        print("We sell potions for 30 bucks and buy potions for 20. Ya! Auntie want ya mesos, cannot izit? ($ v $)")

    def talkdifferent(self):
        print("""
        Now Auntie has seen you differently. But just like any other auntie in MapleStory, she has higher expectations.
        But Auntie remains the same in the shop, selling and buying stuffs for money.
        You can do the following in the shop. You have {} mesos. Type the number beside:
        1. Buy potion X 1
        2. Sell potion X 1
        3. Potion Description
        4. Fight monster at dungeon
        """)
    
    def talk(self, player):
        print("You arrived at the town. You heard an typical Singaporean auntie saying...")
        reply = random.randint(1,5)
        if reply == 1:
            print("\"You need something? Come Come. Auntie takes to the shop\"")
        elif reply == 2:
            print("\"Looking for a potion?\"")
        elif reply == 3:
            print("\"Lelong. lelong. But no buy 1 get 1 free hor\"")
        elif reply == 4:
            print("\"Come buy chicken essence potion. Fight hard hard hor.\"")
        elif reply == 5:
            print("\"Sales are hard to come by these days...\"")
        print("""
        You can do the following in the shop. You have {} mesos. Type the number beside:
        1. Buy potion X 1
        2. Sell potion X 1
        3. Potion Description
        4. Fight monster at dungeon
        """.format(player.mesos))

    def talkagain(self, player):
        print("""
        You can do the following in the shop. You have {} mesos. Type the number beside:
        1. Buy potion X 1
        2. Sell potion X 1
        3. Potion Description
        4. Fight monster at dungeon
        """.format(player.mesos))

class Dungeon():
    def talk(self, player, monster):
        print("""
        You enter the blue portal that is luminating.
        Somehow, you arrived the map after hovering over the dungeon's portal for quite some time.
        A wild level {} {} appeared.
        What do you want to do?
        1. Fight
        2. Run away
        """.format(monster.level, monster.name))

    def monsterappear(self, monster):
        print("""
        A wild level {} {} appeared.
        What do you want to do?
        1. Fight
        2. Run away
        """.format(monster.level, monster.name))

    def fighting(self, player, monster):
        print("        What do you want to do?")
        while True:
            for i in range(len(player.skills)):
                print('        {}. {}'.format(i + 1, player.skills[i]))
                if i == len(player.skills) - 1:
                    print("        {}. Drink Potion".format(i + 2))
                    print("        {}. Run Away\n".format(i + 3))
            inp = input()
            if inp == "exit":
                print(exit_message)
                time.sleep(20)
                sys.exit()
            if (inp.isdigit() and int(inp) == len(player.skills) + 1) or inp == "Drink Potion":
                player.dpotion()
            if (inp.isdigit() and int(inp) == len(player.skills) + 2) or inp == "Run Away":
                return (False, "Shop")
            if inp in player.skills:
                inp = inp.lower()
                attack_type = getattr(player, inp)
                break
            if inp.isdigit():
                if int(inp) in range(1, len(player.skills) + 1):
                    skills  = list(map(lambda x : x.lower(), player.skills))
                    attack_type = getattr(player, skills[int(inp) - 1]) # with string, call method
                    break
        attack_type(monster)
        monster.attack(player)
        if monster.health == 0:
            monster.death()
            time.sleep(0.5)
            player.kill(monster)
            return (True, "monster_death")
        if player.health == 0:
            player.death()
            return (False, "player_death")
        return (True, "Dungeon")
    
        
#state machine for the locations
class Location(sm.SM):
    start_state = 'Welcome'

    def get_next_values(self, state, inp):
        if state == 'Welcome':
            if inp == 'exit':
                print(exit_message)
                time.sleep(20)
                sys.exit() # exit command prompt
                return ('exit', None)
            elif inp == "Yes" or inp == "yes":
                return("Shop", None)
            else:
                return("Welcome", None)
        if state == "Shop":
            if inp == "Dungeon" or inp == "4":
                return("Dungeon", None)
            elif inp == "exit":
                print(exit_message)
                time.sleep(20)
                sys.exit()
            else:
                return("Shop", None)
        if state == "Dungeon":
            if inp == "Shop":
                return ("Shop", None)
            elif inp == "exit":
                print(exit_message)
                time.sleep(20)
                sys.exit()
            else:
                return("Dungeon", None)           

monster_names = ["Orange Mushroom", "Green Mushroom", "Ribbon Pig", "Slime", "Stump", "Horny Mushroom", "Wild Boar", "Wooden Mask", "snail", "red snail", "Yeti", "jr. Neckie"]

def start():
    print(welcome_string)
    print("Orange Mushroom greets you.")
    print("Welcome to FakeMapleStory")
    print("Loading-in-progress")
    time.sleep(2)

    location = Location()
    shop = Shop()
    dungeon = Dungeon()
    location.start()

    print("If you want to exit the game anytime, type \'exit\' to exit the game \n ***Caution***: The game will not be saved. ")
    time.sleep(1)

    player_name = input("Alright! What should you name yourself?\n")
    if player_name == "exit":
        print(exit_message)
        time.sleep(20)
        sys.exit()
    player = Player(player_name)
    inp = input("Start Adventure? Type \'Yes\' to start!\n")
    location.step(inp)
    if inp == "exit":
        print(exit_message)
        time.sleep(20)
        sys.exit()

    while location.state == "Welcome":
        print("\nI will wait for you! When you are ready...")
        inp = input("Type \'Yes\' to start!\n")
        if inp == "exit":
            print(exit_message)
            time.sleep(20)
            sys.exit()
        location.step(inp)
    print("Adventure awaits for you!\n")
    while True and inp != "exit":
        if location.state == "Shop":
            if player.level == 10  and player.job == "Beginner":
                inp = player.jobadvancement()
                shop.talkdifferent()
            else:
                shop.talk(player) # small introduction in every location
            inp = input()
            while inp in ["1", "2", "3"]:
                if inp == "1":
                    player.bpotion()
                elif inp == "2":
                    player.spotion()
                elif inp == "3":
                    shop.dpotion()
                shop.talkagain(player)
                inp = input()
            location.step(inp)
        if location.state == "Dungeon":
            monster_name = monster_names[random.randint(0,len(monster_names)-1)]
            monster = Monster(monster_name, player)
            dungeon.talk(player, monster) # small introduction in every location
            inp = input()
            counter = True
            if inp == "1":
                inp = True
                while inp == True and inp != "exit":
                    if counter == True:
                        inp, results = dungeon.fighting(player, monster)
                        counter = False
                    elif counter == False and results == "Dungeon":
                        inp, results = dungeon.fighting(player, monster)
                    elif counter == False and results == "monster_death":
                        # new monster
                        monster_name = monster_names[random.randint(0,len(monster_names)-1)]
                        monster = Monster(monster_name, player)
                        dungeon.monsterappear(monster)
                        inp = input()
                        if inp == "exit":
                            print(exit_message)
                            time.sleep(20)
                            sys.exit()
                        if inp == "2" or inp == "Run Away":
                            location.state = "Shop"
                            break
                        inp, results = dungeon.fighting(player, monster)
                    if inp == False:
                        if results == "Shop" or "player_death":
                            location.state = "Shop"
                            break
                        
                
            location.step(inp)


welcome_string ="""
@@@@@@@@&&&&&&&&&&&&&&&&&&&&@@@@@@@@&&&&&&&&@@@@&@@&@@@@@@@@@@@@@@@@@@@@&&&&&&&&@@@@&&&&&&&&@@@@&&&&
@@@@@@@@&&&&&&&&&&&&&&&&&&&&@@@@@@@@&&&&&&&&@@@@&&&&@@@@@@@@@@@@@@@@@@@@&&&&&&&&@@@@&&&&&&&&@@@@&&&&
@@@@&&&&@@@@@@@@@@@@@@@@@@@@@@@@&&&&&&&&@&&&@&&@@@@&@&&&@&&&@@&&@&&&@@@@@@@@@@@@@@@@&&&&@@@@@@@@&&&&
@@@@&&&&@@@@@@@@@@@@@@@@@@@@@@@@@&@@@@&&@&@/.   .,/((((//*,.    /&@@@@@@@@@@@@@@@@@@&&&&@@@@@@@@&&&&
&&&&@@@@@@@@@@@@&&&&@@@@@@@@&&&&@@&@@#  ,####%%%%%%%%##((((((((/(/(*  ,&&&@&@@@&@&&&@@@@@@@@&&&&@@@@
&&&&&&&&&&&&&&&&&&&&&&&&@@&&&@@&@# ./((#%%%%%%%%%%%#(((((((((((((///((((  (&@&&@@&&&&&&&&&&&&&&&&&&&
&&&&&&&&&&&&&&&&&&&&&&&&@@&&@&# ,(/#((#%%%%%%%%%####(((((((((((((//(((((##%. %@&@&&&&&&&&&&&&&&&&&&&
@@&&&&&&&&&&&&&&@@@&@@@&@&@&, /(((((#################((((((((((((((((((/(((((* (&&&@&&&&@&&&&&&&&&&&
&&&&&&&&&&&&&&&&@@&@&&@@@, *((########################(((((((#%%#########(((((#, @&&&&&&&&&&&&&&@@@@
&&&&&&&&&&&&&&&&@&&&@%  /#(###########################((((((#%%%########(#((((#(/ &&&&&&&&&&&&&&@@@@
@@@@@@@@&@@&@&@&@%  *%%%%%%%###########################(((((((#%%######(((##(((((( (@&&&&&&&@@@@@@@@
@@@@@@@@&&&&%.  (&%&%%%%%%%%###############################(#(((((((##(((((#(((((##. &&&&&&&@@@@&&&&
@@@@@&&(  ,#%%%%%%%%%%%%%#####################################((((((((////////((((((( *@&&&&&&&&&&&&
@&&@( ,####((((((((#((###########################%%%%%%%%#######(((((((////////(((((##/ /&@&&&&&&&&&
@@% *(/(//////////////////(((((((((############%%%&%%%%%%%%####(((((((((////////((((###%( .&&&&&&&&&
&& ////*****//**//////((///////////((((((((##%%%%%%%%%%%%%%%%#(((((((((////////////(((###%%, (&&&&&&
@# ///****/*,       .*(((((*//////////////(((%#%%%%%%%%%%%%%%%(((((((((///////////////((((((## *@@@@
&# ///**/.*//***//*,***.#(. /(////////////////((((###########(//(/////////////****//////((((((#. &&@
@&  (((/( /,.*****///**/#((((##/. *(/////////**//((((((((((/////////////*******//(///////((((((#. &&
&&&  ((((( */(*,/////*/##(((((((((((((*  ,/((//////////*********////*********////(/(//////(((((#( #&
&&&&&  //**/*./(//(/ ###/ ,/#(((((((((((((((##/, .,((((/////////*/********//*(((((##/,*///((((((# #&
&&&&&&&#  .***/***.%##/ .    &&&&&&%%%##((((((((((((##(#(/*.   ,*//(((((/((/*.  ***///////((((((( &&
&&&&&&&&&&&&#,  %&@&&&&     ,@&&@@@@@@&&&&&&%%###((((/ %    (#(((((#(((####%##%%.//////(####%#%# #@@
&&&&&&&&&&%&  @&%##%%%&@&@@&@@@@.@&&@&&&@&@@&&&&&%#((/      (((((((((((######%%%%,/(((####%%%&, &&&@
&&&&&&&&&&. &&&&&###%%%%%%@@@@@@@%(&@,,%*,@&&&&&&&&&&%#((((((((((((((((#######%%#(/((#%%%%&(  &&&&&&
&&&&&&&&& ,&&&&&&&&&&&%%%&@@@@@@&&@&@@@&@&&&&&&&&&&&&&%&%#((((((((((((#######%%%%% *.    *%%&&&&&&&&
&&&&&&&& *&&&&&&&&&&&&&&&&@@@@@@&&&&&&&&&&&&&&&&&&&%%%%#####((#((((((########%%%%%/ %&%&&&&&&&&&&&&&
&&&&&&&. &&%&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&%%%#%%%%%##((##########%%%%%%% %%&&&&&&&&&&&&&&
&&&&&&& *&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&%###########%%%%%%%# %%%%%&&&&&&&&&&&
&&&&&&& .&&&&&%%%%&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&%%######%%%%%%%%%%* %%%%%%%%&&&&&&&&
&&&&&&&# #&&&&%%%%%%%%%%&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&%%%%%%%###%%%%%%%%%%%% (%%%%%%%%&&&&&&&&
&&&&&&&&( (&&&%%%%%%%%%%%%%%&&&&&&&&&&&&&&&&&&&%%%%%%%%%%%%%%%%%%%%##%%%%%%%%%&%& *%%%%%%%%%&&&&&&&&
&&&&&&&%%%. &&%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%########%%%%%%%%%&&&% (%&%%%%%%%%&&&&&&&&
&&&&&&&%&&%%. (%%%%%%%%%%%%###%%%%%%%%%%%%%%%%%%##################%%%%%%%%&&&&  &&%&&&&&%%&&&&&&&&&&
&&&&&&&&%%%%%&#  /&%%%%%%%%%%##################################%%%%%%%%&&&&#  &&&&&&&&&&&&&&&&&&&&&&
&&&&&&&&&&%%%%%%%%*  *%%%%%%%%%%%%%%#######################%%%%%%%%%&&&&%  /%&&&&&&&&&&&&&&&&&&&&&&&
&&&&&&&&&&&&%%%%%%%%%&#*  .(%&&%&%%%%%%%%%%%%%%%%%%%%%%%%%%%%%&&%@&&#   %@&&&&&&&&&&&&&&&&&&&&&&&&&&
&&&&&&&&&&&&&&&%%%%%%%%%%%%%##,    *%%&&%&&&&%&&&&&&&&&&&&&&&#,    (%&%%%%%%&&&&%%&&&&&&&&&&&&&&&&&&
&&&&&&&&&&&&&&&&%%%%%%%%%%%%#%%%#%%#%%%%#(*,.          ..*(#%%%&%%%%%%%%%%%%%%%%%%%%%%&&&&&&&&&&&&&&
&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
"""

exit_message = """
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&#,.,(#%%&&&&&%%%##(/,..,(%&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&(.(&@@@@@@@@@&%#(///((##%&&&@@@@@@@@@&(./%&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@% ..*%@@@@@@@@(/#@@@@@@@@@@@@&%((/*****/((###%%%%%##/*(/#&@@@@@%//#&@%(%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&,,,.....,%@,#@@@@@@@@&/,(%&@@@@@@@@@@@@@@@@@@@@@&&%#*.(%%%##/*/@%*,,.,,.%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@(,,.,........*&@@%,/@&%(. ,*((#%%%#((,.   ./(%&@@@@@@@@@@@&,,, .,,,,,,,,./*%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&(,,,*,,...,,,,,*..*(%&%%&%&&%%&&%&&&%%%&&&&%#####(/,,...*/.,,*****,.,,....*&#/@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&*,%@&*,**,,,.,.. ,#&&%&&&&@@@&&&%&&&&&&&&&&&&&&&&%%%###(,,,****,.,,*,,.,...,,,.&&&*%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@*(@@@#*,,,,,**, *&%%&&&&@@@@@@&&&&%%&&&&&&&&&&&&&&%&%%%%#*,,.,*,**,,*,,,,,,,,.,,.####/&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%,@@@@/(#..***,.#&&&%%%%&&&@@&&&&&%%&&&%&&&&&&&&&&&&&&%&&%%%,,**,,,**,.,.,,,...,*, (%##/#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%(@@@@(#&/.*,,.#&&&&&&&&%%%%%%%%&&&&&&&&&&&&&&&&&&&&&&&&&&&%&%,.**,**,.,.,,.....,(##(*,**(@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@,@@@@(((.&,,,*%&&&&&&&&&&&&&&%%%%%%&&&&&&&&&&&&&&&&&&&&&&&&%&%&#.,,,,,,,....,###%/*##%###%&&#,,%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@*%@@@#(.#%/..*%&%&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&%&&%&%&&%&&%*.,.....*&&%#/#####(/,,///*./# &@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&.@@@&/&&&&&*(&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&%&@@@&&%%%&&%#(*.,.#&&%&&&&&%*#&&@@@@@@@&/.&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%(@@@%/,*%&/(&%%&%&&&%%%&&%%%%%%%%%%%%%%&&&&&&%%&%&&@@@@@@@@@&%&&&%&&%,., &&@/&&&&&,&@@@@@@@@@@@@@&*@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%(@@%%*,,,.#%&%&#       .,/&%%%%%%%%%%%%%%%%%%%%%&@@@@@@@@@@@@@@&%%%%*,,.%&(/&&&&((@@@@@@@@@@@@@%%@#(@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&.&%%%/./########%%%&&&&&&&%%%%%%%%%%%%%%%%%%%%&&@@@@@@@@@@@@@@@@&&%/...(#*(*(&&#(@@@@@@@@@@@@&%%%%&/@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@#.../%%%*,.########%%%&&&&&&&%&%&&&%%%%%%%%%%%%%%%@@@@,,(@@@@@@@@@@@&%.,,,%&//(&@%*@@@@%&&@@@@@&%%%%%%,@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ ...(%%/.%&%&%%%%%%%&&&&&&&&&&&&%%%&&&&&&&%%%%%%%&@@@@@@@(.   &@@@@&(.,./&&&&&&& @@@@@&%%%%%%%%%%%%%#*@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@/**,.,/*%&&%&%&&&&&&&&&&&&&&&&&&&%,*,&&&&&&&&&&&&&&@@@@@@@@@@@@@@@&&*.,,,,.#%%%%&@@@@@@&%%%%%%%%%%%%(/@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#. *#%&%%&%&&%&&&&&&&&&&&&&&&&&&&%,.(&&&&&&&&&&&&&&&&@@@@@@@&%#%%%%&,.,,,,.#%%%%%@@@@@@@&%%%%%%%%%%%*#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@,*&&&&%%#%&&%&%&&&&&&&&&&&&&&&&&&&%%&&&&&&&&&&&&&&&&%%@@@@&%%##########*.,,.#%%%%%&@@@@@@&%%%%%%%%%%%,&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@**&&&&%%%%(%%%&&&&&&&&&&%%&&&&&&&&%&&%%%&&&&&&&&&&&&&&&%&&&&&&&%%########*.,,,*%%%%%%&@@@@&%%%%%%%%%%# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@& (#%%%%&&%/,/(((#&&&&&%%%#####(((#%&&&&&&&&&&&&&&&&&&&%&&%&&&%&&%&&&&&&%#(,,,,.,/%%%%%%%@@&%%%%%%%%%%(,@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@*/###%%&%&&(#@@@@@@@@@@@@@@@@@@@@@@@@@@&#/%&&%%&&%%%%&%&&&&&&&&&&&&&&%%/......,,,,.(%%%%%%##%@@@@@@&%(*@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@% /##%&&%&%((@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#/#&&&&%%%&&&&&&&&&&&&%&&%%/.,,,,..,,,,. /#%%%%%%%%%%#(.&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@(,&@@@@@@@*/#(,,(%&%&&/%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&(/%&%&%&&&%%&&&&&&%%###/,*/,,,...,,..,,....... ...#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@,,. #@@@@/,&%.%@@&%#*(&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%*#&&&%&&&&&&&%&###(#..........................*&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@&,,,.../@@*(%*#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&.#%&&&&&%%%##((%*..,,,,,,,,,,,,,,,.....(,..,,//&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@,,,,,...//(%.&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@/(%%&%%%##(*&&#,.,,,,,,,**(////,,..,###....,&@*&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@/.,,,,....*#/@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@*(%%###/(%%&&/....(*/(**,,,,,,,..(####,.,,.#@/&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@.,,,,,....#/&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#.###*(&%%%&%,..,,,,,,,,,,,,,,.*######*,.,,*@%,@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@&.,,,,,,. ///%&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&%%%%%.*,&&&%&%%%( ..,,,,,,,,,,,,,./#####%@@*,,..#&*%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@&.,,,,,,,.(.%%%%&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&%%%%%%%%%*/%&&&%&%%%#*.,,,,,,,,,,,,,../#####%@@@#.,,,,(@/(@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@&.,,,,,,,./*%%%%%%%%&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%%%%%%%%%%%%%%# #&%&&&&&&&#(/ ,,,,,,,,,,,....,######%@@@@%*.,,,,%&*/@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@.,,,,,,,.*/%%%%%%%%%%%%%&&@@@@@@@@@@@@@@@@@@@@@@@@@@@@&%%%%%%%%%%%%%%%%%%%%%#.%&&&&&&&&&%##/..,,,,,,,,,,,,,,.*#######%&@@@@*,,,,,./%@//%@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@(.,,,,,,,.*%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%#..#%%%%%%%%%%%%%%%%#,%%%%%&%%%####, .,,,,,,,,,,,,,...,###%@@&%%##%&@#,,,,..,,/#&%//%@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@,,,,,,,,..%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%#,.,,./%%%%%%%%%%%%%%%%#.#%&%&%#/,,(##..,,,,,,,,,,,,....,.(##&@@@@@@@@@@@@# ,,.,,.,,..(/#@@@@@@@@@@@@@@@@@@
@@@@@@@@@@&,,,,,,,,.#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%#.,.,,,,,,%%%%%%%%%%%%%%%%%#*###########,.,,,,,,,,,,,,....,,..#%@@@@@@@@@@@@@@@&,,,,.,.... ./%@@@@@@@@@@@@@@@
@@@@@@@@@@@&,,,,,,,,,#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%/ .....,,,,.,%%%%%%%%%%%%%%%,(##########(*..,.,,,,,,,,...,,,,,,.,%@@@@@@@@@@@@@@@@@@&(*....,,,.....,/&@@@@@@@@
@@@@@@@@@@@@@# ....,..*%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%#.........,,,,,,.%%%%%%%%%%%%,/###########((..,,,,,,,,,.,,,,,,,,,,,,.#@@@@@@@@@@@@@@@@@%#/..,,,,.,,,..,&@@@@@@@@
@@@@@@@@@@@@@@@#  ..... (%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%#............,,,,,.*%%%%%%%%%,/%###########((/..,,,,,,,,,,,,,,,,,,,......%@@@@@@@@@@@@&##/..,,,...,,.. &@@@@@@@@@
@@@@@@@@@@@@@%%#%##/*,... *%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%...............,,,,.,%%%%%%*.(############(#(*..,,,,,,,,,,,,,,,,,..,,,,,,.. ,#&@@@@@@&##(..,,,,..,,.. %@@@@@@@@@@
@@@@@@@@@@@&%###############,,(%%%%%%%%%%%%%%%%%%%%%%%%%( ...............,,,,..%%#.,(#############((((( ..,,,,,,,,,,,,,,,,,,,,,.,,,,,,....*%%####,..,,,..,,,..(@@@@@@@@@@@
@@@@@@@@@@@@&%#################(..(%%%%%%%%%%%%%%%%%%%%%/ ................,,,,...(###############((((((( ..,,,,,,,,,,,,,,,,,,,,.,,...**** ,,../#/..,,,..,,,,.,@@@@@@@@@@@@
@@@@@@@@@@@@@@@@&&&%%%#############/, ,/#%%%%%%%%%%%%%%%( ................,,,,,./###############(((((((((,..,,,,,,,,,,,,,,,,,,,,,,,,,,.,,,,,,.....,*/*,.,,,..*@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@&&&%%%%%#####(/,.,**,**(((##### ................,,,,,.*##############((##(##(........,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,..........,,*,.,%@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&%%%###(, .*#######*.. .............,,,,,.*#############(((((#/ .............,,,,,,,,,,,,,,,,,,,,,,,,,,,,.......,..,.(@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&&&%#/, .,//................,,,,,.*##########(((#((,........................,,,,,,,,,,,,,,,,,,,,,....,..,,..%@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&&&#(...............,,,,,.(########((/*,*(###############((((//***,,.. ...,,,,,..,...,,,,,,.,,,,(&@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@/............,,,,, ,..,**/(((########(########%%%%%%&&&&&&&&&&&&&&&&&%#/,.,**,...,,..*%@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#.. .  .,,..,(################%%%%&&&&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&#(#&@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&&&&&&&&&&&&&&&&&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

Pink bean can now go to sleep. See you soon!
"""

start()