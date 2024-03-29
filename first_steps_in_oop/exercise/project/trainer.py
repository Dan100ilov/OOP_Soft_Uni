
from OOP.first_steps_in_oop.exercise.project.pokemon import Pokemon


class Trainer:
    def __init__(self, name: str):
        self.name = name
        self.pokemons = []

    def add_pokemon(self, pokemon: Pokemon):
        if pokemon in self.pokemons:
            return "This pokemon is already caught"
        else:
            self.pokemons.append(pokemon)
            return f"Caught {pokemon.pokemon_details()}"

    def release_pokemon(self, pokemon_name: str):
        for pokеmon in self.pokemons:
            if pokеmon.name == pokemon_name:
                self.pokemons.remove(pokеmon)
                return f"You have released {pokemon_name}"
            else:
                return "Pokemon is not caught"

    def trainer_data(self):
        result = ''
        result += f"Pokemon Trainer {self.name}\n"
        result += f"Pokemon count {len(self.pokemons)}\n"

        for pokemon in self.pokemons:
            result += f" - {pokemon.pokemon_details()}\n"
        return result
