import random
pokemon_number = random.randint(1, 152)
import requests
import response
import json

# Introduce Game
print("⭐                                   ⭐")
print("⭐                                   ⭐")
print("⭐       ♡ Kiana, Temi & Nadja ♡     ⭐")
print("⭐                                   ⭐")
print("⭐             Welcome To:           ⭐")
print("⭐        POKEMON TOP TRUMPS         ⭐")
print("⭐                                   ⭐")
print("⭐                                   ⭐")
player_name = input("Player, please enter your name: ")
print("Welcome " + player_name + ", to Top Trumps")

def random_pokemon():
    pokemon_number = random.randint(1, 151)
    url = 'https://pokeapi.co/api/v2/pokemon/{}/'.format(pokemon_number)
    response = requests.get(url)
    pokemon = response.json()

    # Create a dictionary that has the Pokémon name, id, height and weight
    return {
        'name': pokemon['name'],
        'id': pokemon['id'],
        'height': pokemon['height'],
        'weight': pokemon['weight']
    }

# The players get 10 random Pokemon to choose from
def chosen_pokemon():
    for i in range(10):
        get_pokemon = random_pokemon()
        print(get_pokemon['name'].title())
    pokemon = input("What Pokemon would you like to pick?")
    return pokemon


def get_pokemon_info(pokemon_name):
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_name.lower()}/"
    response = requests.get(url)

    if response.status_code == 200:
        pokemon_info = response.json()
        return pokemon_info
    else:
        return None


# Get chosen Pokemon
chosen_pokemon_name = chosen_pokemon()
my_pokemon = get_pokemon_info(chosen_pokemon_name)

if my_pokemon:
    print('Your Pokemon stats are: {} with id: {}, height: {} decimetres, weight: {} hectograms.'.format(my_pokemon['name'].title(),
                                                                                   my_pokemon['id'],
                                                                                   my_pokemon['height'],
                                                                                   my_pokemon['weight']))
else:
    my_pokemon = random_pokemon()


# Random Pokemon for the computer
computer_pokemon = random_pokemon()
print("The computer's Pokemon is: {}".format(computer_pokemon['name'].title()))

# Ask the player which stat they want to use
chosen_stat = input("What stat would you like to choose (id, height, or weight)? ")

# Opponent chooses a stat
def opponent_choose_stat():
    stats = ['id', 'height', 'weight']
    print("Opponent, please choose a stat (id, height, or weight):")
    chosen_stat = input("> ")

    # Validate the chosen stat
    while chosen_stat not in stats:
        print("Invalid stat. Please choose a stat (id, height, or weight):")
        chosen_stat = input("> ")

    return chosen_stat


opponent_pokemon = random_pokemon()
print('The opponent got {}'.format(opponent_pokemon['name']))

def get():
    # Simulate scores for the player and computer
    my_score = 0
    computer_score = 0

    if my_pokemon[chosen_stat] > computer_pokemon[chosen_stat]:
        my_score = 1
        print('You won this round')
    elif my_pokemon[chosen_stat] == computer_pokemon[chosen_stat]:
        print('You drew this round')
    elif my_pokemon[chosen_stat] < computer_pokemon[chosen_stat]:
        computer_score = 1
        print('You lost this round')

    return my_score, computer_score


my_total_score = 0
computer_total_score = 0
my_score, computer_score = get()
my_total_score += my_score
computer_total_score += computer_score
print('Your current score is {}, compared to the computer\'s score of {}.'.format(my_total_score, computer_total_score))

play_again = input('Play again? (Y/N): ')
if play_again.upper() != 'Y':
    choice = False
    print('No Worries! Have a good day.')
else:
    chosen_pokemon_name = chosen_pokemon()
    my_pokemon = get_pokemon_info(chosen_pokemon_name)

    opponent_pokemon = random_pokemon()
    print('The opponent got {}'.format(opponent_pokemon['name']))

    chosen_stat = opponent_choose_stat()

    my_score, computer_score = get()
    my_total_score += my_score
    computer_total_score += computer_score
    print('Your Pokemon stats are: {} with id: {}, height: {} decimetres, weight: {} hectograms.'.format(my_pokemon['name'].title(),
                                                                                   my_pokemon['id'],
                                                                                   my_pokemon['height'],
                                                                                   my_pokemon['weight']))
    print('Your current score is {}, compared to the computer\'s score of {}.'.format(my_total_score,
                                                                                      computer_total_score))

play_again = input('Play again? (Y/N): ')
if play_again.upper() != 'Y':
    choice = False
    print('No Worries! Have a good day.')

def pokemon_file():
    import csv
    field_names = ['My score', 'Computer score']
    data = [{'My score': my_total_score, 'Computer score': computer_total_score}]
    path = './scores.csv'

    with open(path, 'a', newline='') as csv_file:
        spreadsheet = csv.DictWriter(csv_file, fieldnames=field_names)
        if csv_file.tell() == 0:
            spreadsheet.writeheader()
        spreadsheet.writerows(data)


pokemon_file()

