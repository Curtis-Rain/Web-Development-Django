class StudentFighter(object):

    def __init__(self, strength, health, name):
        self.strength = strength
        self.name = name
        self.health = health


    # now let's create an attack method
    # It will take self as an arugment (like all methods)
    # as well as the opponent we are attacking.
    def attack(self, opponent):

        # for now we will simply subtract
        # the opponent's health with our
        # strength

        # we must use opponent.health
        # to refer to opponent's health
        # and self.strength to refer to our strength
        opponent.health -= self.strength

        # then return a message stating
        # how many attack points the opponent has 
        message = "{} has {} health points remaining".format(opponent.name, opponent.health)
        print(message)


kalu = StudentFighter(strength=3, health=100, name="Kalu")
david = StudentFighter(strength=5, health=100, name="David")

# Now let's make an attack
kalu.attack(david)