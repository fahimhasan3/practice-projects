from pokemon import Pokemon
from pokemon import PokemonType
from pokemon import Charmander

class Trainer:
    def __init__(self, name, pokemons, potions, activePokemon):
        self.name = name
        self.pokemons = pokemons[:6]
        self.potions = potions
        if(activePokemon > len(self.pokemons) -1):
            activePokemon = 0
        self.activePokemon = activePokemon
        print('\ncreated new trainer name={}, potions={} \npokemons={}, active pokemon={}'
        .format(self.name, self.potions, self.pokemons, self.pokemons[activePokemon]))

    def usePotion(self):
        if(self.potions > 0):
            print('{} is using a potion to heal {}'.format(self.name, self.pokemons[self.activePokemon]))
            self.pokemons[self.activePokemon].gainHealth(50)

    def attack(self, otherTrainer):
        if(self.pokemons[self.activePokemon].isKnockedOut):
            print("{} doesn't have any more pokemon, he cannot attack anymore".format(otherTrainer.name))

        print('{} is attacking {}'.format(self.name, otherTrainer.name))
        enemyPokemon = otherTrainer.pokemons[otherTrainer.activePokemon]
        self.pokemons[self.activePokemon].attack(enemyPokemon)
        if(enemyPokemon.isKnockedOut):
            print('{} is knocked out switching to next pokemon'.format(enemyPokemon))
            switched = False
            for index, pokemon in enumerate(otherTrainer.pokemons):
                if(not pokemon.isKnockedOut):
                    switched = True
                    otherTrainer.switch(index)
                    break
            if(not switched):
                print("{} doesn't have any more pokemon, he lost the duel".format(otherTrainer.name))
    
    def switch(self, newActivePokemon):
        if(newActivePokemon > 0 and newActivePokemon <= len(self.pokemons)):
            newPokemon = self.pokemons[newActivePokemon]
            if(newPokemon.isKnockedOut):
                print('cannot switch to {} he is knocked out'.format(newPokemon))
            else:
                print('{} is switching his active pokemon to {}'.format(self.name, newPokemon))
                self.activePokemon = newActivePokemon
        else:
            print("cannot switch, pokemon doesn't exist")


charmander = Charmander(30)
charizard = Pokemon('charizard ash', 44, PokemonType.fire.name)
squirtle = Pokemon('squirtle ash', 30, PokemonType.water.name)
bulbasaur = Pokemon('bulbasaur ash', 44, PokemonType.grass.name)

squirtle2 = Pokemon('squirtle fh', 30, PokemonType.water.name)
bulbasaur2 = Pokemon('bulbasaur fh', 44, PokemonType.grass.name)
print('\n')

ash = Trainer('ash', [charmander, charizard, squirtle, bulbasaur], 5, 0)
fh = Trainer('fahim', [bulbasaur2,squirtle2], 1, 3)

ash.attack(fh)
fh.usePotion()
fh.attack(ash)
ash.attack(fh)
fh.attack(ash)
ash.attack(fh)
ash.attack(fh)
ash.switch(2)
ash.attack(fh)
ash.attack(fh)
