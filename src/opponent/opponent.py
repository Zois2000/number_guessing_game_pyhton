import random

class Opponent:
    def __init__(self, guess_range: tuple[int, int]):
        self.random_picked_number = random.randrange(*guess_range)
        self.guess_counter = 0

    def guess_number_check(self, player_input_guess: int, opponent_random_number) -> int:
        self.guess_counter += 1
        
        if player_input_guess > self.random_picked_number:
            return 1
        elif player_input_guess < self.random_picked_number:
            return -1
        elif player_input_guess == self.random_picked_number:
            return 0

