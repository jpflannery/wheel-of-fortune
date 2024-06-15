# Let's import the random module
import random

# Let's make two lists of letters, one for consonants and one for vowels, and an empty list for letters used during a round.
consonants = ['B','C','D','F','G','H','J','K','L','M','N','P','Q','R','S','T','V','W','X','Y','Z']
vowels = ['A','E','I','O','U']
used_letters = []

# Let's also create a list of wedges of dollar values or other values on the wheel.
wheel = [5000, 500, 900, 700, 600, 650, 500, 700, 500, 600, 550, 500, 600,
        'Bankrupt', 650, 850, 700, 'Lose a Turn', 800, 500, 650, 500, 900, 'Bankrupt']

# Let's define a default contestant number of zero.
contestant_number = 0

# Let's define who the current contestant is throughout the game.
current_contestant = None

# Let's create some classes, one class for contestants and another for puzzles
class Contestant:
    # Initialization of the class
    def __init__(self, name, turn=False, grand_total=0, round_total=0):
        self.name = name
        self.grand_total = grand_total
        self.round_total = round_total
    
    # Contestant spins the wheel
    def spin_the_wheel(self):
        print("{} spins the wheel.".format(self.name))
        i = random.randint(0, len(wheel)-1)
        amount = wheel[i]
        print(amount)
        if amount == 'Bankrupt':
            self.round_total = 0
            print("Oh no! You've hit a Bankrupt, {}.".format(self.name))
            switch_contestant(self)
        elif amount == 'Lose a Turn':
            print("You've lost your turn, {}.".format(self.name))
            switch_contestant(self)
        else:
            letter = input("Please enter a consonant: ")
            letter = letter.upper()
            if letter in used_letters:
                print(display_letters(used_letters, current_puzzle))
                print("Oops! That letter has been called already. You lose your turn. I'm sorry.")
                switch_contestant(self)
            elif (letter in consonants) and (letter in current_puzzle):
                self.round_total += (current_puzzle.count(letter) * amount)
                used_letters.append(letter)
                print(display_letters(used_letters, current_puzzle))
                if current_puzzle.count(letter) == 1:
                    print("There is {} {} in the puzzle, {}. Your total is ${}.".format(current_puzzle.count(letter), letter, self.name, self.round_total))
                elif current_puzzle.count(letter) > 1:
                    print("There are {} {}'s in the puzzle, {}. Your total is ${}.".format(current_puzzle.count(letter), letter, self.name, self.round_total))
                self.contestant_play()
            elif letter not in consonants:
                letter= input("Please enter a consonant:")
                letter = letter.upper()
                if letter in used_letters:
                    print(display_letters(used_letters, current_puzzle))
                    print("Oops! That letter has been called already. You lose your turn. I'm sorry.")
                    switch_contestant(self)
                elif (letter in consonants) and (letter in current_puzzle):
                    self.round_total += (current_puzzle.count(letter) * amount)
                    used_letters.append(letter)
                    print(display_letters(used_letters, current_puzzle))
                    if current_puzzle.count(letter) == 1:
                        print("There is {} {} in the puzzle, {}. Your total is ${}.".format(current_puzzle.count(letter), letter, self.name, self.round_total))
                    elif current_puzzle.count(letter) > 1:
                        print("There are {} {}'s in the puzzle, {}. Your total is ${}.".format(current_puzzle.count(letter), letter, self.name, self.round_total))
                    self.contestant_play()
                else:
                    print(display_letters(used_letters, current_puzzle))
                    print("There is no {} in the puzzle, {}.".format(letter, self.name))
                    switch_contestant(self)
            else:
                print(display_letters(used_letters, current_puzzle))
                print("There is no {} in the puzzle, {}.".format(letter, self.name))
                switch_contestant(self)
        
    # Contestant buys a vowel
    def buy_a_vowel(self):
        if self.round_total >= 250:
            letter = input("Please enter a vowel: ")
            letter = letter.upper()
            if letter in used_letters:
                print(display_letters(used_letters, current_puzzle))
                print("Oops! That letter has been called already. You lose your turn. I'm sorry.")
                switch_contestant(self)
            elif (letter in vowels) and (letter in current_puzzle):
                self.round_total -= 250
                used_letters.append(letter)
                print(display_letters(used_letters, current_puzzle))
                if current_puzzle.count(letter) == 1:
                    print("There is {} {} in the puzzle, {}. Your total is ${}".format(current_puzzle.count(letter), letter, self.name, self.round_total))
                elif current_puzzle.count(letter) > 1:
                    print("There are {} {}'s in the puzzle, {}. Your total is ${}".format(current_puzzle.count(letter), letter, self.name, self.round_total))
                self.contestant_play()
            elif letter not in vowels:
                print("Please enter letter A, E, I, O, or U:")
                self.buy_a_vowel()
            else:
                print(display_letters(used_letters, current_puzzle))
                print("There is no {} in the puzzle, {}.".format(letter, self.name))
                switch_contestant(self)
        else:
            print("You don't have enough money to buy a vowel. Please spin or solve.")
            self.contestant_play()
            
    # Contestant tries to solve the puzzle
    def solve_the_puzzle(self):
        solve = input("What is the puzzle? ")
        if solve.upper() == current_puzzle:
            if self.round_total < 1000:
                self.round_total = 1000
                self.grand_total += self.round_total
                print(current_puzzle + ". That's it! Well done, {}! You've won ${} this round since that is our house minimum for a round. The grand totals now are: {}: ${}, {}: ${}, {}: ${}.".format(self.name, 
                                                                                                                                               self.round_total, 
                                                                                                                                               contestant_1.name, 
                                                                                                                                               contestant_1.grand_total,
                                                                                                                                               contestant_2.name, 
                                                                                                                                               contestant_2.grand_total,
                                                                                                                                               contestant_3.name, 
                                                                                                                                               contestant_3.grand_total))
            elif self.round_total >= 1000:
                self.grand_total += self.round_total
                print(current_puzzle + ". That's it! Well done, {}! You've won ${} this round. The grand totals now are: {}: ${}, {}: ${}, {}: ${}.".format(self.name, 
                                                                                                                                               self.round_total, 
                                                                                                                                               contestant_1.name, 
                                                                                                                                               contestant_1.grand_total,
                                                                                                                                               contestant_2.name, 
                                                                                                                                               contestant_2.grand_total,
                                                                                                                                               contestant_3.name, 
                                                                                                                                               contestant_3.grand_total))
            self.round_total = 0
        else:
            print(display_letters(used_letters, current_puzzle))
            print("I'm sorry, that is not correct.")
            contestant_number = switch_contestant(self)
            
    # Contestant is given the choice of spinning the wheel, buying a vowel, or solving the puzzle.
    def contestant_play(self):
        choice = input("{}, would you like to (S)pin the wheel, (B)uy a vowel, or S(o)lve the Puzzle?".format(self.name))
        choice = choice.upper()
        if choice == 'S':
            self.spin_the_wheel()
        elif choice == 'B':
            self.buy_a_vowel()
        elif choice == 'O':
            self.solve_the_puzzle()
        else:
            self.contestant_play()

class Puzzle:
    # Initialization
    def __init__(self, puzzle, category, round_num):
        self.puzzle = puzzle
        self.category = category
        self.round_num = round_num
    
    # Here a new puzzle is created.
    def create_new_puzzle(self):
        unsolved_puzzle = ""
        contestant_1.round_total = 0
        contestant_2.round_total = 0
        contestant_3.round_total = 0
        for i in range(0, len(self.puzzle)):
            if (self.puzzle[i] in consonants) or (self.puzzle[i] in vowels):
                unsolved_puzzle += "_"
            else:
                unsolved_puzzle += self.puzzle[i]
        current_contestant = contestant_list[(self.round_num-1)%3]
        print("The category is {}. ".format(self.category) + "Here is the puzzle: " + unsolved_puzzle + ". {}, it's your turn to start this round.".format(current_contestant.name))
        return unsolved_puzzle
        

# Let's define our three contestants and make an empty contestant list.
contestant_1 = Contestant('George')
contestant_2 = Contestant('Penelope')
contestant_3 = Contestant('Jim Bob')
contestant_list = []

#Let's define our puzzles for the game
puzzle_1 = Puzzle("WHEEL OF FORTUNE", "Show Biz", 1)
puzzle_2 = Puzzle("HAPPY RETIREMENT PAT SAJAK", "Phrase", 2)
puzzle_3 = Puzzle("I WOULD LIKE TO SOLVE THE PUZZLE", "Phrase", 3)
puzzle_4 = Puzzle("SUMMERTIME SUMMERTIME SUM SUM SUMMERTIME", "Song Lyrics", 4)
puzzle_5 = Puzzle("FIXING A FLAT TIRE", "What Are You Doing?", 5)
puzzle_6 = Puzzle("ATLANTA BRAVES WIN THE WORLD SERIES", "Headline", 6)

# Let's create some functions

# Let's make a list of contestants for our upcoming game
def make_contestant_list(contestant_1, contestant_2, contestant_3):
    contestant_list.append(contestant_1)
    contestant_list.append(contestant_2)
    contestant_list.append(contestant_3)
    return contestant_list

# Let's start a brand new game
def start_new_game(contestant_1, contestant_2, contestant_3):
    # Let's also define the starting current contestant, which will have a default index of 0 for the first player from the contestant list.
    print("It's the show where the wheel keeps on spinning, spinning, spinning, and the the contestants keep on winning, winning, winning! It's Wheel of Fortune!")
    print("Contestant 1 is {}, contestant 2 is {}, and contestant 3 is {}.".format(contestant_1.name, contestant_2.name, contestant_3.name))
  

# Here the contestant is switched due to landing on a "Bankrupt" or "Lose a Turn", calling a letter not in the puzzle or 
# a used letter, or unsuccessfully attempting to solve the puzzle.
def switch_contestant(current_contestant):
    if current_contestant == contestant_1:
        current_contestant = contestant_2
    elif current_contestant == contestant_2:
        current_contestant = contestant_3
    elif current_contestant == contestant_3:
        current_contestant = contestant_1
    print("Now, it's your turn, {}. Your total is ${}.".format(current_contestant.name, current_contestant.round_total))
    current_contestant.contestant_play()
    
#This function will display the unsolved puzzle after each turn.
def display_letters(used_letters, current_puzzle):
    unsolved_puzzle = ""
    vowel_count = 0
    consonant_count = 0
    for i in range(len(current_puzzle)):
        if (current_puzzle[i] in consonants) or (current_puzzle[i] in vowels):
            if current_puzzle[i] in used_letters:
                unsolved_puzzle += current_puzzle[i]
            else:
                unsolved_puzzle += "_"
        else:
            unsolved_puzzle += current_puzzle[i]
    for i in range(len(current_puzzle)):
        if current_puzzle[i] in vowels:
            vowel_count += 1
    for i in range(len(unsolved_puzzle)):
        if unsolved_puzzle[i] in vowels:
            vowel_count -= 1
    for i in range(len(current_puzzle)):
        if current_puzzle[i] in consonants:
            consonant_count += 1
    for i in range(len(unsolved_puzzle)):
        if unsolved_puzzle[i] in consonants:
            consonant_count -= 1
    if vowel_count == 0:
        print("***NO MORE VOWELS!***")
    if consonant_count == 0:
        print("***ONLY VOWELS LEFT!***")
    return unsolved_puzzle

# This function declares the winner at the end of the game.
def declare_winner(contestant_list):
    winning_total = 0
    winning_contestant = None
    for contestant in contestant_list:
        if contestant.grand_total > winning_total:
            winning_total = contestant.grand_total
            winning_contestant = contestant
    return "Congratulations, {}! You have won the game with a grand total of ${}!".format(winning_contestant.name, winning_total)

# Here we begin playing our game using the functions we've created.
make_contestant_list(contestant_1, contestant_2, contestant_3)
start_new_game(contestant_1, contestant_2, contestant_3)

# Round 1
current_puzzle = puzzle_1.puzzle
puzzle = puzzle_1.create_new_puzzle()
contestant_1.contestant_play()

used_letters = []

# Round 2
current_puzzle = puzzle_2.puzzle
puzzle = puzzle_2.create_new_puzzle()
contestant_2.contestant_play()

used_letters = []

# Round 3
current_puzzle = puzzle_3.puzzle
puzzle = puzzle_3.create_new_puzzle()
contestant_3.contestant_play()

used_letters = []

# Round 4
current_puzzle = puzzle_4.puzzle
puzzle = puzzle_4.create_new_puzzle()
contestant_1.contestant_play()

used_letters = []

# Round 5
current_puzzle = puzzle_5.puzzle
puzzle = puzzle_5.create_new_puzzle()
contestant_2.contestant_play()

used_letters = []

# Round 6
current_puzzle = puzzle_6.puzzle
puzzle = puzzle_6.create_new_puzzle()
contestant_3.contestant_play()

# The game is over. Let's see who won.
declare_winner(contestant_list)