from enum import Enum  

class PokemonType(Enum):
    grass = 1
    water = 2
    fire = 3

def calculateDamage(damage, atackerType, defenderType):
    if(atackerType == PokemonType.fire.name):
        if(defenderType == PokemonType.fire.name):
            damage /= 2
        if(defenderType == PokemonType.water.name):
            damage /= 2
        if(defenderType == PokemonType.grass.name):    
            damage *= 2
    elif(atackerType == PokemonType.water.name ):
        if(defenderType == PokemonType.fire.name):
            damage *= 2
        if(defenderType == PokemonType.water.name):
            damage /= 2
        if(defenderType == PokemonType.grass.name):    
            damage /= 2
    elif(atackerType == PokemonType.grass.name ):
        if(defenderType == PokemonType.fire.name):
            damage /= 2
        if(defenderType == PokemonType.water.name):
            damage *= 2
        if(defenderType == PokemonType.grass.name):    
            damage /= 2
    return damage

class Pokemon:
    def __init__(self, name, level, type):
        self.name = name
        self.level = level
        self.type = type
        self.maxHealth = level * 5
        self.health = self.maxHealth
        self.isKnockedOut = False
        self.experience = 0
        print('created new pokemon name={}, level={}, type={}, maxHealth={}, health={}, isKnockedOut={}'
        .format(self.name, self.level, self.type, self.maxHealth, self.health, self.isKnockedOut))
    
    def __repr__(self):
        return self.name
    
    def loseHealth(self, damage):
        if(damage > self.health):
            self.health = 0
            self.knockOut()
        else:
            self.health -= damage
        self.printHealth()

    def gainHealth(self, heal):
        self.health += heal
        if(self.health > self.maxHealth):
            self.health = self.maxHealth
        self.printHealth()

    def printHealth(self):
        print('{} has now {} health'.format(self.name, self.health))

    def knockOut(self):
        self.isKnockedOut = True
    
    def revive(self, health):
        self.isKnockedOut = False
        self.health = health
        print("{name} was revived!".format(name = self.name))

    def increaseXP(self):
        self.experience += 10
        if(self.experience == 50):
            print('{} gained 1 level and is now level {}'.format(self.name, self.level))
            self.experience = 0
            self.level += 1

    def attack(self, otherPokemon):
        damage = self.level
        damage = calculateDamage(damage, self.type, otherPokemon.type)
        print('{} attacks {} for {} damage'.format(self.name, otherPokemon.name, damage))
        otherPokemon.loseHealth(damage)
    

class Charmander(Pokemon):
    def __init__(self, level = 5):
        super().__init__("Charmander", level, PokemonType.fire)

    def attack(self, otherPokemon):
        self.flamethrower(otherPokemon)

    def flamethrower(self, otherPokemon):
        damage = self.level * 2
        damage = calculateDamage(damage, self.type, otherPokemon.type)
        print('{} attacks {} with flamethrower for {} damage'.format(self.name, otherPokemon.name, damage))
        otherPokemon.loseHealth(damage)

