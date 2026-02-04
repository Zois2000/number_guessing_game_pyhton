from player.player import Player
from opponent.opponent import Opponent

def guessing_evulation():
    player = Player()
    guessing_range = player.player_range_input()
    opponent = Opponent(guessing_range)

    while True:
        player_input = player.player_input_guess()
        return_value = opponent.guess_number_check(player_input, opponent.random_picked_number)
        
        if return_value == 1:
            print("Too high")
        elif return_value == -1:
            print("Too low")
        elif return_value == 0:
            print("Correct!")
            break
    print(f"Total Guesses: {opponent.guess_counter}")