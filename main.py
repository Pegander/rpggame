import rpggame

kitchen = rpggame.Room("Kitchen")

kitchen.set_description("A dark and dirty room buzzing with flies.")

dining_hall = rpggame.Room("Dining Hall")
dining_hall.set_description("A large room with ornate golden decorations on each wall")

ballroom = rpggame.Room("Ballroom")
ballroom.set_description("A big room with chairs along the walls")

kitchen.link_room(dining_hall, "south")
dining_hall.link_room(kitchen, "north")
ballroom.link_room(dining_hall, "east")
dining_hall.link_room(ballroom, "west")

dave = rpggame.Enemy("Dave", "A smelly zombie")
dave.set_conversation("I will kill you and eat your braaaaiin!!")
dave.set_weakness("sword")
dining_hall.set_character(dave)

ben = rpggame.Friend("Ben", "An old friend with a thing for swords")
ben.set_conversation("Well hello old friend, you look like you could use a hug")
ben.set_inventory("sword")
kitchen.set_character(ben)

sword = rpggame.Item("sword")
sword.set_description("A nice big shiny sword")
ballroom.set_item(sword)

current_room = kitchen
backpack = []

life = 3

while life > 0:
    print("\n")
    current_room.get_details()
    inhabitant = current_room.get_character()
    
    if inhabitant is not None:
        inhabitant.describe()
    item = current_room.get_item()
    
    if item is not None:
        item.describe()
    command = input("> ")
    
    if command in ("north", "south", "east", "west"):
        current_room = current_room.move(command)
    elif command == "hug":
        if isinstance(inhabitant, rpggame.Friend) == True:
            inhabitant.hug()         
        else:
            print(inhabitant.name + " kicks you away!")
            
    elif command == "talk":
        print(inhabitant.conversation)
        
    elif command == "fight":
       if inhabitant is None:
            print("No one here to fight")
       elif isinstance(inhabitant, rpggame.Friend):
           print(inhabitant.name + " doesn't want to fight you")
       elif inhabitant is not None and isinstance(inhabitant, rpggame.Enemy):
            print("With what?")
            fight_with = input("> ")
            if fight_with in backpack:
                if inhabitant.fight(fight_with) == True:
                    print("You won the fight!!")
                    current_room.character = None
                else:
                    print(inhabitant.name + " takes advantage of the situation and kills you")
                    print("You loose your life and the game")
            else:
                print("You don't have " + fight_with)
                print(inhabitant.name + " takes advantage of the situation and bites you")
                print("You loose a life")
                life = life - 1
               ### print ("You now have " + life + " lives left")
                if life == 0:
                    print("You are killed")
                
    elif command == "take":
        if item is not None:
            print ("You take " + item.get_name())
            backpack.append(item.get_name())
            current_room.item = None
        else:
            print("Nothing here to take")
    elif command == "backpack":
        print(backpack)
    elif command == "life":
        print(life)
    elif command == "help":
        print("You can use the following commands to interact with the game; life, talk, fight, hug, take, backpack and various directions")
        
