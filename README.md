# FakeMapleStory

This is a DW assignment in replace of the finals exam

- Dedicated to the millennials and pioneer generation Z out there who wants to feel young again.

- This is fake MapleStory version back when grinding is the thing.(like when I was in primary 2? year 2006?) --with a twist of Singapore-ness and Pokemon memes -- Hope you like it.
- This is built with simple state machine and class with public attribute in python.
- Due to assignment criteria, we need to write codes in single file. I wish that we can separate into different files. 1000 lines of codes is so confusing.

<h2> Installation</h2>

Install libdw, a library by our SUTD course lead Oka Kurniawan. Downloading this package would allow us to use state machine.

```python
pip install libdw
```

---

<h2>How it works a.k.a. GM's tips</h2>

This program uses state machine, classes and a lot of if else statement to run. 

- Players are first asked to jot down their names and starts the adventure. All classes except monster are initiated.
- I used state machine to change location when needed. Below is the state diagram. I put an exit code as a secondary measure in get_next_values() on top of exiting right after the input just in case.
- I have four public classes: Shop, Dungeon, Player and Monster. All classes have their distinct methods and they interact with one another. Hence, this is why I use public class instead.
- To keep players entertained, I uses varied and random conversation by using if else statement and  random.randint().
- Also, the damage inflicted, monster names and mesoes earned are obtained using random.randint() function.
- Attacks are triggered when players chooses the attack type and the program would find the correct method using getattr() function.
- Experience is gained by the amount of monster killed in that level/ levellimit(i.e. the number of monster for that level to level up) for each level
- After each level up, experience would become zero and the number of monster to level up would be increased by 2, starting from 5.
- A health system is used to keep track both players and monster health. This is done by using class states
- When the player dies, experience would decrease by 10% of the levellimit and returns to town.
- When job advancement, player gains new skills by triggering player.jobadvancement()

<h2>How to Play FakeMapleStory</h2>

FakeMapleStory is a primitive PvE game, where player plays on command prompt. Instructions in command prompt are quite fool-proof, as player just has to type in the numbers to proceed to the next steps. This game is grinding for the level, and reliving millennials' childhood. 

To start the game, run main.py under fakemaplestory folder on command prompt. A new command prompt window at full screen would be good.

```python
./fakemaplestory>main.py
```

Player starts off as beginners.

Shop/Town: Players can buy/sell potion at shops. When player reaches level 10, player would proceed to job advancement(Warrior, Magician, Thief, Bowman). Players can earn mesos to buy potions in the shop by fighting monsters.

Jobs

Each jobs have specific skills and different health. Warriors have highest health while  Thieves have the highest attacks. Their stats vary from one to another.

Dungeon: This is the place that players fight monster. Monster chosen are random and difficulty is based on player's level.

At any point that players want to quit, type "exit" or press crt-c for windows and command-c for mac

Happy Mapling~



