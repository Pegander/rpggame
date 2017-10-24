class Character():

    """ Create a character """
    def __init__(self, char_name, char_description):
        self.name = char_name
        self.description = char_description
        self.conversation = None

    """ Describe this character """
    def describe(self):
        print( self.name + " is here!" )
        print( self.description )

    """ Set what this character will say when talked to """
    def set_conversation(self, conversation):
        self.conversation = conversation

    """ Talk to this character """
    def talk(self):
        if self.conversation is not None:
            print("[" + self.name + " says]: " + self.conversation)
        else:
            print(self.name + " doesn't want to talk to you")

    """ Fight with this character """
    def fight(self, combat_item):
        print(self.name + " doesn't want to fight with you")
        return True

    """ Hug this character """
    def hug(self):
        print(self.name + "says 'why on earth would i?'")
        return True
    
    
class Enemy(Character):
    def __init__(self, char_name, char_description):
      
      super().__init__(char_name, char_description)
      self.weakness = None

      """ Create a fight method """
    def fight(self, combat_item):
        if combat_item == self.weakness:
            print("You fend " + self.name + " off with the " + combat_item)
            return True
        else:
            print(self.name + " crushes you, puny adventurer!")
            return False
    
    def set_weakness(self, item_weakness):
        self.weakness = item_weakness

    def get_weakness(self):
        return self.weakness

    """ Create a friend class """
class Friend(Character):
    def __init__(self, char_name, char_description):

      super().__init__(char_name, char_description)

    def set_inventory(self, inventory):
        self.inventory = inventory
        return True
    
    def get_inventory(self):
        print(self.inventory)
    
    def give_item(self, inventory):
        if self.inventory is not None:
            print(self.name + " gave you a " + inventory)
        else:
            print(self.name + " has nothing for you")
            
    """ Hug this character """
    def hug(self):
        print(self.name + " Hugs you right back")
        return True

