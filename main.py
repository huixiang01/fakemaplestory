import random
import time
from libdw import sm
import sys
import numpy
import math
# import winsound

# Dedicated to the millenials and pioneer generation Z out there who wants to feel young again.
# This is fake maplestory version back when grinding is the thing.(like when I was in primary 2? year 2006?) -- with a twist of singapore-ness and pokemon memes -- I hope you like it.
# This is built with simple state machines and classes with public attributes in python.
# Due to assignment criteria, we need to write codes in single file. I wish that we can seperate into different files. Writing 800 lines of codes is so confusing.
# I did not realise that prof oka has a sample code with similiar format. Dang, there goes my marks...

class Player():
    def __init__(self, name):
        self.maxhealth = 100
        self.health = 80
        self.level = 1
        self.potion = 0
        self.experience = 0
        self.explimit = 3
        self.mesos = 100
        self.name = name
        self.skills = ["Attack"]
        self.job = "Beginner"
        self.weapon = 1 # use as a multiplier
        self.firstblood = True  # beginner's luck factor
        self.wep_eqp = None
    
    def attack(self, monster):
        damage = random.randint(15, 25)
        damage = (1 + (self.level - 1)/3) * damage 
        critical = random.randint(1, 10) 
        if critical <= 2:
            damage *= 1.5 # critical to increase damage variance
        damage *= self.weapon
        damage = int(round(damage, 0)) # rounding returns a float. Hence, int to make it nice
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
            if damage < self.level * 20:
                print("It is not effective... {} sustains {} damage.".format(monster.name, damage))
            elif damage >= self.level * 20:
                print("It is effective! {} sustains {} damage.".format(monster.name, damage))
            elif damage >= self.level * 40:
                print("It is super effective! {} sustains {} damage.".format(monster.name, damage))
        if critical <= 2:
            print("It is a critical hit!")
        print("")
        time.sleep(1)

    def dpotion(self):
        if self.potion > 0:
            self.health += 50
            if self.maxhealth <= self.health:
                recovered_health = 50 - (self.health - self.maxhealth) # ensure player does not exceed max health
                self.health = self.maxhealth
            else:
                recovered_health = 50
            self.potion -= 1
            print("{} has drunk 1 health potion and recovered {} health.".format(self.name, recovered_health))
        else:
            print("GOD DANG IT. No potions left.")

    def kill(self, monster):
        if monster.type == "Monster":
            self.experience += 1.1 ** monster.level
            mesos = random.randint(monster.level * 15, monster.level * 20)
            self.mesos += mesos # meso is based monster level
        if monster.type == "Boss":
            self.experience += 30
            mesos = 300
            self.mesos += mesos 
        print("You have slayed {}!".format(monster.name))
        print("You have earned {} mesos. You now have {} mesos".format(mesos, self.mesos))
        print("Experience: {}% ({}/{})".format(min(100, round(self.experience/self.explimit * 100, 1)),
        int(min(self.experience * 100, self.explimit * 100)), int(self.explimit * 100) )) # experience not to exceed 100%
        if self.explimit <= self.experience: # level up
            self.level += 1
            self.explimit *= 1.3 # level up difficulty rises exponentially, TIME FOR GRINDING!!!!
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
            self.maxhealth = int(round(self.maxhealth * 1.25 * mult, -1)) # to nearest tens # health increase exponetially too
            self.health = self.maxhealth
            print("{} has leveled up to {}! Congratz!!!\nYour health is {}/{}.".format(self.name, self.level, self.health, self.maxhealth))
            self.experience = 0

    def bpotion(self):
        if self.mesos >= 45:
            self.mesos -= 45
            self.potion += 1
            print("You now have {} potion(s)! You have {} mesos left.".format(self.potion, self.mesos))
        else:
            print("Dun play play! You no mesos right? tsk.") 
    
    def spotion(self):
        if self.potion >= 1:
            self.mesos += 30
            self.potion -= 1
            print("You now have {} potion(s)! You have {} mesos left.".format(self.potion, self.mesos))
        else:
            print("Ops! You don't have potions to sell.")
    
    def death(self):
        self.experience -= self.explimit/10
        self.experience = max(self.experience, 0)
        print("\nOhhhh noooo... {} has died.".format(self.name))
        time.sleep(5)
        print("You have lost 10% experience.\n")

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
            print("Choose a job!")
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
        
        self.weapon = 1 # weapon is not the same anymore
        print("            \n{} has advanced to {}. More Adventure awaits!\n".format(self.name, self.job))

        return True
    # warrior
    def advwarrior(self):
        self.skills.extend(["DoubleSlash", "SlashBlast"])
        self.maxhealth *= 2
        self.maxhealth = int(self.maxhealth)
        self.health = self.maxhealth
    
    def doubleslash(self, monster):
        damage = random.randint(self.level * 15, self.level * 25)
        monster.health -= damage
        print("{} slashes {}. Monster gets {} damage.".format(self.name, monster.name, damage))
        time.sleep(0.2)
        damage = random.randint(self.level * 15, self.level * 25)
        monster.health -= damage
        print("{} slashes {} again. Monster gets {} damage.".format(self.name, monster.name, damage))

    def slashblast(self, monster):
        damage = random.randint(self.level * 20, self.level * 35)
        monster.health -= damage
        print("{} blasts on {}. Monster gets {} damage".format(self.name, monster.name, damage))

    # magician
    def advmagician(self):
        self.skills.extend(["EnergyBolt", "MagicCross"])
        self.maxhealth *= 1.2
        self.maxhealth = int(self.maxhealth)
        self.health = self.maxhealth

    def energybolt(self, monster):
        damage = random.randint(self.level * 20, self.level * 30)
        monster.health -= damage
        print("{} blasts on {}. Monster gets {} damage".format(self.name, monster.name, damage))

    def magiccross(self, monster):
        damage = random.randint(self.level * 20, self.level * 30)
        monster.health -= damage
        print("{} crosses {}. Monster gets {} damage.".format(self.name, monster.name, damage))
        time.sleep(0.2)
        damage = random.randint(self.level * 15, self.level * 25)
        monster.health -= damage
        print("{} crosses {} again. Monster gets {} damage.".format(self.name, monster.name, damage))

    # thief
    def advthief(self):
        self.skills.extend(["ShurikunBlast", "LuckySeven"])
        self.maxhealth *= 1.5
        self.maxhealth = int(self.maxhealth)
        self.health = self.maxhealth

    def shurikunblast(self, monster):
        damage = random.randint(self.level * 25, self.level * 45)
        monster.health -= damage
        print("{} blasts at {}. Monster gets {} damage".format(self.name, monster.name, damage))

    def luckyseven(self, monster):
        damage = random.randint(self.level * 20, self.level * 40)
        monster.health -= damage
        print("{} throws steely at {}. Monster gets {} damage.".format(self.name, monster.name, damage))
        time.sleep(0.2)
        damage = random.randint(self.level * 20, self.level * 35)
        monster.health -= damage
        print("{} throws steely at {} again. Monster gets {} damage.".format(self.name, monster.name, damage))

    # bowman
    def advbowman(self):
        self.skills.extend(["DoubleArrow", "ArrowBlow"])
        self.maxhealth *= 1.8
        self.maxhealth = int(self.maxhealth)
        self.health = self.maxhealth

    def arrowblow(self, monster):
        damage = random.randint(self.level * 30, self.level * 40)
        monster.health -= damage
        print("{} shoots at {}. Monster gets {} damage".format(self.name, monster.name, damage))

    def doublearrow(self, monster):
        damage = random.randint(self.level * 20, self.level * 30)
        monster.health -= damage
        print("{} shoots at {}. Monster gets {} damage.".format(self.name, monster.name, damage))
        time.sleep(0.2)
        damage = random.randint(self.level * 20, self.level * 30)
        monster.health -= damage
        print("{} shoots at {} again. Monster gets {} damage.".format(self.name, monster.name, damage))

class Monster():
    def __init__(self, name, player):
        if player.firstblood:
            self.level = 1
            player.firstblood = False
        else:
            distribution = numpy.random.normal(player.level, 1, 100)
            self.level = int(max(1, round(random.choice(distribution), 0))) # can't have negative number, distribution to give a chance of having higher level monster with small chance
        self.health = 30 + (self.level - 1) * 25
        self.maxhealth = self.health
        self.name = name
        self.type = "Monster"

    def attack(self, player):
        damage = random.randint(45, 95)
        damage = (1 + (self.level - 1)/2.2) * damage/10
        critical = random.randint(1, 15)
        if critical == 1:
            damage *= 1.5 # critical to increase damage variance
        damage = int(round(damage, 0))
        player.health -= damage # returns int
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
            print("{} pokes {}".format(self.name, player.name))
            time.sleep(1)
            print("The cuteness is too intense to be ignored. Argh. Heart pain. {} kenna {} damage.".format(player.name, damage))
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
        if critical <= 1:
            print("It is a critical hit!")
        player.health = int(max(player.health, 0)) # no negative health, int to standardise
        self.health = max(self.health, 0)
        print('{}\'s health : {}/{}'.format(player.name, player.health, player.maxhealth))
        print('{}\'s health : {}/{}\n'.format(self.name, self.health, self.maxhealth))
        time.sleep(1)

    def death(self, player):
        print("{} has died.".format(self.name))
        drops = random.randint(1, 1000)
        drop = False

        if drops > 980 and player.weapon <= 1.8:
            weapons ={"Warrior": "Maple Sword", "Magician": "Maple Wand", "Thief": "Maple Claw", "Bowman": "Maple Bow", "Beginner": "Maple Flag"}
            weapon = weapons[player.job]
            player.weapon = 2.3
            drop = True
        elif drops > 950 and player.weapon <= 1.3:
            weapons ={"Warrior": "Pico-Pico Hammer", "Magician": "Mithril Wand", "Thief": "Steel Guards", "Bowman": "Hunter's Bow", "Beginner": "Broomstick"}
            weapon = weapons[player.job]
            player.weapon = 1.8
            drop = True
        elif drops > 900 and player.weapon <= 1.1:
            weapons ={"Warrior": "Newspaper Sword", "Magician": "Magic Wand", "Thief": "Garnier", "Bowman": "War Bow", "Beginner": "Wooden Club"}
            weapon = weapons[player.job]
            player.weapon = 1.3
            drop = True
        elif drops > 500 and player.weapon == 1: # let them have some beginner's luck
            weapons ={"Warrior": "Training Sword", "Magician": "Training Wand", "Thief": "Training Claw", "Bowman": "Training Bow", "Beginner": "Tree Branch"}
            weapon = weapons[player.job]
            player.weapon = 1.1
            drop = True

        if drop:
            player.wep_eqp = weapon
            print("{} dropped a {}".format(self.name, weapon))
            print("You are now equipped {} as a weapon\n".format(weapon))
            time.sleep(1)

class Boss():
    def __init__(self, name, player):
        if player.level <= 15:
            self.level = 10
        else:
            self.level = int((math.ceil(player.level / 10.0)) * 10) 
        self.health = 10000 * 2 ** (0.2 * (self.level - 10))
        self.maxhealth = self.health
        self.name = name
        self.type = "Boss"

    def attack(self, player):
        damage = random.randint(self.level * 0.5, self.level * 2)
        damage = ((self.level) * damage)
        critical = random.randint(1, 15)
        if critical <= 2:
            damage *= 1.5 # critical to increase damage variance
        damage = int(round(damage, 0))
        player.health -= damage # returns int
        reply = random.randint(1,5) # varied replies for entertainment
        if reply == 1:
            print("{} bear hugs {}.".format(self.name, player.name))
            time.sleep(1)
            print("Ewwwww. Disgusting. {} gets {} damage.".format(player.name, damage))
        elif reply == 2:
            print("{} jumps on {}.".format(self.name, player.name))
            time.sleep(1)
            print("{} is being crushed on. {} takes {} damage.".format(player.name, player.name, damage))
        elif reply == 3:
            print("{} makes an earthquake.".format(self.name))
            time.sleep(1)
            print("{} cannot stand up and looks at {} with his teary eyes. So embarrassing. {} takes {} damage.".format(player.name, self.name, player.name, damage))
        elif reply == 4:
            print("WARNING: {} hp1/mp1 on {}".format(self.name, player.name))
            player.health = 1
            time.sleep(1)
            print("What a shock of your life!")
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
        if critical <= 1:
            print("It is a critical hit!")
        player.health = int(max(player.health, 0)) # no negative health, int to standardise
        self.health = max(self.health, 0)
        print('{}\'s health : {}/{}'.format(player.name, player.health, player.maxhealth))
        print('{}\'s health : {}/{}\n'.format(self.name, self.health, self.maxhealth))
        time.sleep(1)

    def death(self, player):
        print("Finaly, {} has sucummubed to its injury.".format(self.name))
        drops = random.randint(1, 1000)
        drop = False

        if drops > 950 and player.weapon <= 2.3:
            weapons ={"Warrior": "Maple Soul Singer", "Magician": "Maple Staff", "Thief": "Maple Kandayo", "Bowman": "Maple Soul Searcher"}
            weapon = weapons[player.job]
            player.weapon = 3
            drop = True
        elif drops > 900 and player.weapon <= 1.8:
            weapons ={"Warrior": "Maple Sword", "Magician": "Maple Wand", "Thief": "Maple Claw", "Bowman": "Maple Bow", "Beginner": "Maple Flag"}
            weapon = weapons[player.job]
            player.weapon = 2.3
            drop = True
        elif drops > 750 and player.weapon <= 1.3:
            weapons ={"Warrior": "Pico-Pico Hammer", "Magician": "Mithril Wand", "Thief": "Steel Guards", "Bowman": "Hunter's Bow", "Beginner": "Broomstick"}
            weapon = weapons[player.job]
            player.weapon = 1.8
            drop = True

        if drop:
            player.wep_eqp = weapon
            print("{} dropped a {}".format(self.name, weapon))
            print("You are now equipped {} as a weapon\n".format(weapon))
            time.sleep(1)

class Shop():
    def dpotion(self):
        print("Each potion heals 50 health!")
        print("We sell potions for 45 bucks and buy potions for 30. Ya! Auntie want ya mesos, cannot izit? ($ v $)")

    def talkdifferent(self):
        print("""
        Now Auntie has seen you differently. But just like any other auntie in MapleStory, she still has higher expectations.
        But Auntie remains the same in the shop, selling and buying stuffs for money.
        You can do the following in the shop. You have {} mesos.
        Choose your options:
        1. Buy potion X 1
        2. Sell potion X 1
        3. Potion Description
        4. Fight monster at dungeon
        """)
    
    def talk(self, player):
        print("You arrived at the town. You heard an typical Singaporean auntie saying...")
        reply = random.randint(1,5)
        if reply == 1:
            print("\"You need something? Come Come. Auntie takes to the shop.\"")
        elif reply == 2:
            print("\"Looking for a potion?\"")
        elif reply == 3:
            print("\"Lelong. lelong. But no buy 1 get 1 free hor!\"")
        elif reply == 4:
            print("\"Come buy chicken essence potion. Fight hard hard hor.\"")
        elif reply == 5:
            print("\"Sales are hard to come by these days...\"")
        print("""
        You can do the following in the shop. You have {} mesos.
        Choose your options:
        1. Buy potion X 1
        2. Sell potion X 1
        3. Potion Description
        4. Fight monster at dungeon
        """.format(player.mesos))

    def talkagain(self, player):
        print("""
        You can do the following in the shop. You have {} mesos.
        Choose your options:
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
        if monster.type == "Monster":
            print("""\n
        A wild level {} {} appeared.
        What do you want to do?
        1. Fight
        2. Run away
            """.format(monster.level, monster.name))
        else:
            print("""\n
        After fighting for so long, a rare boss monster, {}, appeared.
        What do you want to do?
        1. Fight
        2. Run away
            """.format(monster.name))

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
        trap_random = random.randint(1, 12)
        results = "normal"

        # check traps and effects
        if trap_random == 12:
            time.sleep(1)
            results = self.trap(player, monster, attack_type)
        # if results == normal, check whether there is damage reflection and do monster attacks
        if results == "normal":
            attack_type(monster)
            isDamageReflect = random.randint(1,40) 
            if isDamageReflect == 50 and player.level != 1: # let them have some beginner's luck
                player.health -= player.maxhealth/2
                player.health = max(player.health, 0)
                print("You did not realise there is damage reflect. !@!%#^#!@%@@!")
                if player.health == 0:
                    player.death()
                    return (False, "player_death")
            monster.attack(player)
        # check deaths
        if player.health == 0:
            player.death()
            return (False, "player_death")
        elif monster.health == 0:
            monster.death(player)
            time.sleep(1)
            player.kill(monster)
            return (True, "monster_death")
        return (True, "Dungeon")
    
    # traps are used for element of surprise that hinders players.
    def trap(self, player, monster, attack_type):
        
        reply = random.randint(1,25)
        if reply <= 5:
            damage = random.randint(15, 20)
            print("Alamak! {} accidentally stepped on a dog's poop. Ew~ Xiao Chou Chou!".format(player.name)) # status: random damage trap
        elif reply <= 10:
            damage = random.randint(5, 15)
            print("Argh. There is a thorn on {}'s feet".format(player.name)) # status: random damage trap
        elif reply == 11:
            player.health = 0
            print("A wild hacker appears. He did some hacking magic. You died. !@!%#^#!@%@@!") # status: !@!@%@!@$!
            # add some drastic element of surprise. chance of getting this is 1/250
            time.sleep(5) # Make them stare at it for a while.
            return "status"
        elif reply <= 14:
            print("You kenna hit by a random ball from nowhere and you tio stunned.\n") # status: stunned
            time.sleep(1)
            monster.attack(player)
            return "status"
        elif reply <= 18:
            print("{} chatters to itself and somehow you cannot attack.\n".format(monster.name)) # status: seal
            time.sleep(1)
            monster.attack(player)
            return "status"
        elif reply <= 21:
            print("{} casted darkness on {}.".format(monster.name, player.name)) # status: blind
            print("{} can't see anything.\n".format(player.name))
            isHit = random.randint(1,2)
            if isHit == 1:
                attack_type(monster)
                print("Welp... You manage that cause damage.") 
            time.sleep(1)
            monster.attack(player)
            return "status"
        elif reply <= 25:
            print("{} casted confusion on {}.".format(monster.name, player.name)) # status: confusion
            print("You tripped and injured yourself.")
            damage = random.randint(player.level * 10, player.level * 20)

        # Those without player damage due to traps is being returned.
        time.sleep(1)
        player.health -= damage
        player.health = int(max(0, player.health))
        time.sleep(1)
        print("Player's health: {}/{}\n".format(player.health, player.maxhealth))
        return "normal"

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
            if inp == "Shop" or inp == "2":
                return ("Shop", None)
            elif inp == "exit":
                print(exit_message)
                time.sleep(20)
                sys.exit()
            else:
                return("Dungeon", None)           

monster_names = ["Orange Mushroom", "Green Mushroom", "Ribbon Pig", "Slime", "Stump", "Horny Mushroom", "Wild Boar", "Wooden Mask", "snail", "red snail", "Yeti", "jr. Neckie", "Pig", "Pepe"]
boss_names = ["Mushmom", "Stumpy", "King Slime", "Mano", "Deli", "King Clam"]

def start():
    # winsound.PlaySound(r'./BGM/MapleStory_BGM_Title.wav', winsound.SND_ASYNC | winsound.SND_LOOP)
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

    # Introduction done
    while True and inp != "exit":
        if location.state == "Shop":
            # winsound.PlaySound(None, winsound.SND_ASYNC)
            # winsound.PlaySound(r'./BGM/Henesys Music.wav', winsound.SND_ASYNC | winsound.SND_LOOP)
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
            # winsound.PlaySound(None, winsound.SND_ASYNC)
            # winsound.PlaySound(r'./BGM/MapleStory Music - Henesys Hunting Grounds.wav', winsound.SND_ASYNC | winsound.SND_LOOP)
            monster_name = monster_names[random.randint(0,len(monster_names)-1)]
            monster = Monster(monster_name, player)
            dungeon.talk(player, monster) # small introduction in every location, # describe location
            inp = input()
            counter = True
            if inp == "1":
                inp = True
                while inp == True and inp != "exit":
                    if counter == True:
                        inp, results = dungeon.fighting(player, monster) #
                        counter = False
                    elif counter == False and results == "Dungeon": #
                        inp, results = dungeon.fighting(player, monster)
                    elif counter == False and results == "monster_death": 
                        # new monster
                        is_boss = random.randint(1, 100) # code is here so that player must at least kill one monster first
                        if is_boss == 1:
                            # winsound.PlaySound(None, winsound.SND_ASYNC)
                            # winsound.PlaySound(r'./BGM/[MapleStory 2 BGM] Boss 01.wav', winsound.SND_ASYNC | winsound.SND_LOOP)
                            boss_name = boss_names[random.randint(0,len(boss_names)-1)]
                            monster = Boss(boss_name, player)
                            dungeon.monsterappear(monster) # combine variable with boss. 
                        else:
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
                            player.health = player.maxhealth
                            location.state = "Shop"
                            break
                        
                
            location.step(inp)


welcome_string ="""
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
%%%%%%%%%%%%%%%%%%%%%%%%%%%%* /%%%%%..*%%%%%%%%%%%%%%%%%%%%%%%%%%%%,  (%%%#  %%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%* /%%%@@@&%#  #%%%%%%%%%%%%%%%%%%%%%%#  ,%%@@&%%%..#%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%* *%%%@@@@@@@%%/ *%%%%%%%%%%%%%%%%%%/  #%&@@@@@%%%%* #%%%%%%%%%%%%%%%%%%%%
%%%&&&&%&&%%&%%&&&%&%%%%%* ,%%%&@@@@@@@@@@%# ./,       .,(((* .%%@@@@@@@@@%%%#* %&&%%%%%&&&&&%%%%%%%
%%%%&&&%&&&%&%%&&&%%%%%%/  (%%%@@@@@@%/.,//(((((%#((((((%((((/*...,(&@@@@@&%%%(, &&&&&&&%&&&&%%%%%%%
%%%%%%%%%%&&&%%&%%%%%%%#  /#%%&&,,.#%%%%%%#(((((%#((((((%((((((%%%%%%,..(@@&%%#( *%%&&&%%%%%%%%%%%%%
%%%%%%%%%%%&%%%%%%%%%%%. ,((*.(%%%%%%%%%%%#(((((%#((((((%((((((%%%%%%%%%%(..(%#(*.%%%&%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%(  ,,#%%%%%%%%%%%%%%#(((((%#((((((%((((((%%%%%%%%%%%%%%,.*(.(%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%. ,%%%%%%%%%%%%%%%%%#(((((%#((((((%((((((%%%%%%%%%%%%%%%%( .*%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%# .%%%%%%%%%%%%%%%%%%%#(((((%(((((((%((((((%%%%%%%%%%%%%%%%%%* /%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%* /%%%%%%%%%%%%%%%%%%%%%((((#%(((((((%#(/((%%%%%%%%%%%%%%%%%%%%%..%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%, #%%%%%%%%%%%%%%%%%%%%%%%##%%%#(((((#%%%##%%%%%%%%%%%%%%%%%%%%%%% ,%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%, (%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%(((((%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% *%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%, *%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%((#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%( (%%%%%%%%%%%%
&%%%%%%%%%%%%%%/ .%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%, %%%%%%%%&&&&
%%%%%%%%%%%%%%#  %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%..%%%%%%%%%&&
%%%%%%%%%%%%%#  &%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%&@@@@&%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%#.,%%&%%%%%%%
%%%%%%%%%%%%% .#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%@@@@@@@@@@&%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%( *%%%%%%%%%
%%%%%%%%%%%# .#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%@@@@@@@@@@@@@@&%%%%%%%%%%%%%%%%%%%%%%%%%%%%%( *%%%%%%%%
%%%%%%%%%%(  %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%@@@@@@@@@@@@@@@@@@&%%%%%%%%%%%%%%%%%%%%%%%%%%%%(.*%%%%%%%
%%%%%%%%%( .%%%%%%%%%%%%%%%%%%%%%%%%%%%%&@@@@@@@@@@@@@@@@@@@@@@&%%%%%%%%%%%%%%%%%%%%%%%%%%%#..%%%%%%
%%%%%%%%# .#%%%****************************@@@@@@@@@@@@@@@@@@*****************************%%%.,%%%%%
%%%%%%%% .*%%% /@@@@@@@@@@@@@**@@@@@@@@@@@*@@@@@@&&&&&&&@@@@@.@&@@@@@@@@@&**@@@@@@@@@@@# #%%* #%%%%%
%%%%%%%%  ((%%% @@@@@@@@@@@@@**@@@@@@@@@@  @@@@(((#%%#(((@@@@  @@@@@@@@@@&**@@@@@@@@@@@ (%%(( *%%%%%
%%%%%%%% ./((#%% #@@@@@@@@@@@**@@@@@@@@@ %@@@@@@@#*((/#@@@@@@@( @@@@@@@@@&**@@@@@@@@@@ %%#((* #%%%%%
%%%%%%%%( .%###%#% /@@@@@@@@@**@@@@@@@/ @@@@@@@@@@@%@@@@@@@@@@@@. @@@@@@@&**@@@@@@@@ .#%%#%# ,%%%%%%
%%%%%%%%&* .######%/. ./&@@@@@@@@@%*/ @@@@@@@@@@@@/  (@@@@@@@@@@@@# #@@@@#@@@@@@@// .*******.&%%%%%%
%%%%&&&&&%% .*###########%@@@@@@@@@@@@@@@@@@@&#........&./&@@@@@@@@@@@@@&&&&@%####/  @%%@%@&  %%%%%%
%%%%%%&%%&&%%. .(######%@@@@@@@@@@@@@@@@@@@@@@@*........(@@@@@@@@@@@@@@@@@@@@@@( ,#@%###@@@@% /%%%%%
%%%%%%%%%%%&&%%%.. ,(&@@@@@@@@@@@@@@@@@@@@@@@@@@,,,,,,,*@@@@@@@@@@@@@@@@@@@&, /#%%%&@@@@@@@& .%%%%%%
%%%%%%%%%%%%%%%%%%%%#*.  ./%@@@@@@@@@@@@@@@@@@@@@@#//#@@@@@@@@@@@@@@@@@#..(%%%%%%%%%%%&%.  (%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%#/*...    .*/(%%&&@@@@@@@@@@@@@&&%#/,,*(%%%%%%%%%%%%%%%/  ,(%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%#  *.*////*,,///,.,/////* #%%%%%%%%%%%%%#, ..(%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%(,*(%%* .%%#*.*,,. /&&&&&#..,,*,.*%%%%%%%#/,. ./#%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%(. ./##.  ,*///  .(%%%%#(#(&@@@@@@@@@@@@@&%(,...,**(%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%  @@&#@@/.,/////./%%%%%%#.#%%@@@@@@@@@@@@@@@%%# .%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%#*.    */*..,*//////./(#%%%#.  #%%@@@@@@@@@@@@@@@%%%, %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%*  ,,,,...,,,,//////// /((((/..*  %%&@@@@@@@@@@@@@@@&%%(.*%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%  ,,  .. .. ...,,*////./((, .(%%* ,%%@@@@@@@@@@@@@@@@@%%#. %%%%%%%%%%#((((#%%%%%%%%%%%%%%%%%%%
%%%%%* ,,.   ..........,,//. *(%%%%%%%. (%%@@@@@@@@@@@@@@@@@%%%. %%%%%%. *%%%@@@@@( %%%%%%%%%%%%%%%%

Kinky the cat waves you good bye! C u back soon!
"""

start()