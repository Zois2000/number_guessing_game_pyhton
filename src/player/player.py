class Player:
    def __init__(self):
        self.lower_input = 0
        self.upper_input = 0
        self.input_guess = 0

    def player_range_input(self) -> tuple[int, int]:
        print("Enter the guessing range: ")
        y = True
        
        while y:
            self.lower_range = input("Enter lower input range: ")
            self.upper_input = input("Enter upper input range ")
            try:
                self.lower_range = int(self.lower_range)
                self.upper_input = int(self.upper_input)
                y = False
            except ValueError:
                print("Invalid inputs!")
        print("Valid Inputs!")
        return self.lower_range, self.upper_input
    
    def player_input_guess(self) -> int:
        self.input_guess = input("Enter your guess: ")
        try:
            return int(self.input_guess)
        except ValueError:
            print("Ivalid inputs! Please enter integers.")
        return self.input_guess
