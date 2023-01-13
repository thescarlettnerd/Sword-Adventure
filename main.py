print('''       SWORD ADVENTURE    ''')
print('''⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⢀⣀⣀⣀⠀⣶⣶⠀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⠀⣶⣶⠀⣀⣀⣀⡀⠀
⠀⠘⠛⠛⠛⠀⣿⣿⠀⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠀⣿⣿⠀⠛⠛⠛⠃⠀
⠀⠀⠀⠀⠀⠀⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⣿⣤⣤⣤⣤⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣀⣀⣀⣀⣿⠀⠀⠀⠀
⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⡿⠛⣛⠋⣠⣄⣉⣉⠙⣿⣿⣿⣿⣿⠿⠿⠀⠀⠀⠀
⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⡇⢸⣿⡿⣿⡿⠹⣿⠇⠛⠻⣿⣿⣿⣶⣦⠀⠀⠀⠀
⠀⠀⠀⠀⣀⣤⣭⣿⣿⣿⣿⠄⢠⣤⣈⣁⣤⡄⠠⣶⡀⢹⣿⣿⣿⣿⠀⠀⠀⠀
⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⠀⣿⣿⣿⣿⣿⣿⠀⣿⡇⢸⣿⣿⣿⣿⠀⠀⠀⠀
⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⠀⣿⣿⣿⣿⣿⣿⠀⣿⠀⣼⣿⣿⣉⠉⠀⠀⠀⠀
⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⠐⠛⠛⠛⠛⠛⠛⠂⣠⣴⣿⣿⣿⣿⣷⠀⠀⠀⠀
⠀⠀⠀⠀⠛⠛⠻⢿⣿⣿⣿⠘⠛⠛⠛⠛⠛⠛⠃⣿⣿⣿⡿⠟⠛⠛⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⢿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠛⠿⠿⠿⠿⠛⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀''')
print("Hello Adventurer!\n")
name = input("What is your name?\n")
race = input("Are you an ELF, DWARF, or HUMAN?\n")
if race.lower() == "elf":
  race = "elf"
elif race.lower() == "dwarf":
  race = "dwarf"
else:
  race = "human"

rpg_class = input("Are you a FIGHTER, a CASTER, or a ROGUE?\n")
if rpg_class.lower() == "fighter":
  rpg_class = "fighter"
elif rpg_class.lower() == "caster":
  rpg_class = "caster"
else:
  rpg_class = "rogue"

weapon = input("Do you use a STAFF, a SWORD, or a BOW?\n")
if weapon.lower() == "staff":
  weapon = "staff"
elif weapon.lower() == "sword":
  weapon = "sword"
else:
  weapon = "bow"

print(f"\nYou are {name}, the {race} {rpg_class} who uses a {weapon}!\n")
hp = 2 

print("\nWelcome to the Rusty Pike Inn " + name + ".\n")
print("\n*** you find yourself sitting at a table in a cozy tavern nursing a foaming tankard of ale. you are surrounded by the low buzz of conversation from patrons at surrounding tables. suddenly, an argument breaks out at the table next to yours. two men are arguing about the local mythos - according to legend, there is an enormous treasure cache nearby but it is (apparently hotly) debated whether the treasure is hidden within the castle to the west of town, or within the cave systems beneath the mountains to the east. the men continue to argue as you head off to find the treasure yourself... ***\n \n")

landmark = input("Upon exiting the inn, do you head westward to the CASTLE or eastward toward the mountain CAVES?\n")

if landmark.lower() == "castle":
  landmark = "castle"
  print("You head westward toward the castle on the hill that overlooks the town. \nAfter a while of walking, you find yourself at the base of the castle, standing in front of a moat.\n")
  moat = input("Do you SWIM across the moat, or do you build a RAFT using what materials you can find nearby?\n")
  if moat.lower() == "raft":
    print("Using your unique ingenuity, you manage to scrape together a raft that holds together just long enough to get you across the moat and to the base of the castle. Congratulations!")
    castle_inner = input("You spend a short time wandering enough of the castle to discover a spiral staircase. Do you go UP the staircase towards the tower, or DOWN to check out the lower levels?\n")
    if castle_inner.lower() == "down":
      print("You make your way down the stairs, spiralling lower and lower into the depths of the castle until you come to a hall.")
      bowels = input("The hall leads two directions. Both are clearly marked. Do you head left to the DUNGEON or right towards the castle CRYPT?\n")
      if bowels.lower() == "dungeon":
        print("Within the dungeon, you find mostly empty cells, but one contains a very old man. He tells you that there is no treasure in the castle.")
        old_man = input("Do you believe him and LEAVE, or do you continue to SEARCH the castle on your own?\n")
        if old_man.lower() == "leave":
          print("You decide this old man seems to know what he's talking to. You trace back your steps, leaving the castle, taking your raft back across the moat, and heading eastwards toward the CAVES.\n")
        
        else:
          print("Figuring that this old man is lying and just wants to keep the treasure for himself, you continue to search the dungeons.\nUnfortunately, you find yourself in the bowels of a GELATINOUS CUBE before you can find any evidence of treasure here.\nGAME OVER\nTRY AGAIN\n")
          hp -= 1
      else:
        print("You head right towards the crypt in search of treasure. Perhaps it is buried within one of the graves here.\nUpon reaching the crypt, you begin checking through the various tombs, intently searching each one - which is how a ZOMBIE is able to sneak up and turn you into a meal.\nGAME OVER\nTRY AGAIN\n")
        hp -= 1
    else:
      print("You head up the staircase and find that it leads to the immense spire within the centre of the castle. Exploring this tower, you find your way into what appears to be a pristinely kept library. Who could this belong to?\nIt does not take long to discover as you soon find that you have disturbed the studies of a WIZARD. For your rudeness, he flings you out the tower window, killing you.\nGAME OVER\nTRY AGAIN\n")
      hp -= 1
  else:
    print("You decide to chance swimming across the moat as it really doesn't look terribly deep or far. As you're nearing the other side, a searing pain errupts from your left leg and you look back to find that a CROCODILE is making you its supper.\nGAME OVER\nTRY AGAIN\n")
    hp -= 1
else:
  landmark = "caves"
  print("You head eastward toward the far off mountains.")
  if race == "dwarf":
    print("Naturally, being a dwarf, you know your way to the mountains and arrive in a timely manner.") 
  else:
    print("After a fair while of journeying, you arrive at the edge of a vast expanse of forest.")
    mountain = input("Do you find your way through the WOODS, or do you decide to follow the STREAM nearby in the hopes that it will bring you to the base of the mountains?\n")
    if mountain.lower() == "woods" and race == "elf":
      print("Your heightened senses and long life of experience amongst the trees serve you well here. You easily find your way through the woods.")
    elif mountain.lower() == "woods":
      print("These woods are foreign to you and night falls quickly. You are able to find kindling to create a fire and you build yourself a nice little campsite for the night. However, the scent of your dinner attracts a BEAR, and you meet your untimely demise fighting for both your life and your dinner.\nGAME OVER\nTRY AGAIN\n")
      hp -= 1
    else:
      print("Rather than attempting to find your way through the forest on your own, you follow the stream a ways as it seems to be heading toward the mountains.")
      stream = input("After quite a ways, the stream seems to curve away from the mountains. Do you FOLLOW the stream in the hopes that it will curve back again, or do you CROSS the stream and head in a straight line?\n")
      if stream.lower() == "follow":
        print("You stick with what you know and follow the stream. It adds many hours to your journey, and sometimes you feel like giving up, but you've come too far now and push onwards. Fortunately, your persistence pays off.")
       
      else:
        print("You stick with the straightest path and cross the river.")
        cross = input("Do you risk the current and SWIM across, or do you try to stay dry and walk across a line of river STONES you can see?\n")
        if cross.lower() == "swim":
          print("You're cold and wet and the current seems a little bit concerning at times, but you make it across the river and continue on your way to the mountains.")
         
        else:
          print("The river rocks you've discovered are slick and covered in barely visible moss. Unfortunately, while walking across them, you slip, knocking yourself unconscious and the weight of your gear causes you to DROWN in the river.\nGAME OVER\nTRY AGAIN\n")
          hp -= 1

#arrival at mountains# 
if hp > 1:          
  print("You arrive at the base of the mountains and easily find your way into the network of caves beneath them.")
  fork = input("After wandering the caves for a while, you come to a fork. Do you head LEFT or RIGHT?\n")
  if fork.lower() == "left":
    print("You head left for a ways, wandering the labyrinth of tunnels until finding yourself in a large chamber with two exits.")
    smell = input("You notice that one of the exits has a STENCH emenating from it, while the other seems to smell of NOTHING at all. Which way do you go?\n")
    if smell.lower() == "nothing" and rpg_class == "caster":
      print("You find yourself in a very dark passage, and before you know it, you have fallen off a ledge and are plunging into darkness. Quick thinking and your skills with magic allow you to cast a feather fall enchantment upon yourself, slowing your fall and saving your life. Upon safely reaching the ground, you spend hours finding your way back to the entrance of the caves, deciding to head RIGHT instead.")
      fork = "right"
    elif smell.lower() == "nothing":
      print("You find yourself in a very dark passage, and before you know it, you have fallen off a ledge and are plunging into darkness. Unfortunately, there is nothing you can do to save yourself and you are CRUSHED to death when you hit the ground.\nGAME OVER\nTRY AGAIN\n")
      hp -= 1
    else:
      print("For some reason, you decide to follow the stench in the hopes that it will lead somwhere. It does. It leads to a MANTICORE who eats you.\nGAME OVER\nTRY AGAIN\n")
      hp -= 1
  else:
    print("You make your way into the right-hand tunnel, following it into the depths of the caves. Your ears alert you before any of your other senses that you are happening upon a tribe of goblins.")
    goblins = input("Do you FIGHT the goblin tribe, or do you attemt to SNEAK past them instead?\n")
    if goblins.lower() == "sneak" and rpg_class == "rogue":
      print("You employ your sneaky rogue skills you have been honing for years and manage to sneak past the goblins unnoticed. Nice!")
      
    elif goblins.lower() == "sneak":
      print("You're not sneaky. They catch you and you must fight!")
      goblins = "fight"
    else:
      print("A fight it is - you bravely take on the goblins!")
      if rpg_class == "fighter" or weapon == "sword":
        print("You came prepared, and there really weren't that many goblins anyway... you guess. You fight valiantly and vanquish the goblins!")
        
      elif rpg_class == "caster" and weapon == "staff":
        print("For a battlemage like you, a small tribe of goblins doesn't present much of a challenge. you cast FIREBALL and they all go up in a screaming puff of smoke.")
        
      else:
        print("You didn't really think this one through, did you? The goblin tribe BEHEADS you and uses your remains to ward off other adventurers from invading their territory.\nGAME OVER\nTRY AGAIN\n")
        hp -= 1

#arrival at dragon#
if hp > 1:
  print("You have made it through the caverns beneath the mountains, past the goblins, and here, you have found what you set out to find in the first place. A vast treasure hoard! Unfortunately, this treasure seems to already have an owner - an enormous black dragon is curled up atop the treasure, counting through piles of golden coins.")
  dragon = input("You have come so very far and done so many great deeds. Will you BEFRIEND this dragon, or will you attempt to SLAY the dragon and take its immense treasure hoard and become the wealthiest person in all the lands?\n")
  if dragon.lower() == "befriend":
    print("As it turns out, Herbert the Black Dragon really was just hoping to have a friendly companion all these years. He is happy to share his treasure hoard with you so that you may go buy nice things for you two to share - as long as you promise to always return to spend your time with him after going off on your shopping trips. It's pretty difficult for him to fit in shops after all...")
    print(f"CONGRATULATIONS! {name} you made all the right choices and managed to win not only an absurd amound of treasure, but also a life-long friend!\nTHANK YOU FOR PLAYING\n")
  else:
    print("Well that was silly of you wasn't it? You BURN to death after rudely picking a fight with a dragon.\nGAME OVER\nTRY AGAIN\n")
      