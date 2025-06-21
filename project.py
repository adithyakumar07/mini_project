import random

class HangmanGame:
    HANGMAN_PICS = [
        '''
          +---+
              |
              |
              |
             ===''',
        '''
          +---+
          O   |
              |
              |
             ===''',
        '''
          +---+
          O   |
          |   |
              |
             ===''',
        '''
          +---+
          O   |
         /|   |
              |
             ===''',
        '''
          +---+
          O   |
         /|\  |
              |
             ===''',
        '''
          +---+
          O   |
         /|\  |
         /    |
             ===''',
        '''
          +---+
          O   |
         /|\  |
         / \  |
             ==='''
    ]

    def __init__(self, word_list):  
        self.word_list = word_list
        self.word, self.hint = random.choice(self.word_list)
        self.word = self.word.lower()
        self.guessed_letters = []
        self.attempts_left = len(self.HANGMAN_PICS) - 1

    def display_word(self):
        result = ""
        for letter in self.word:
            if letter in self.guessed_letters:
                result += letter + " "
            else:
                result += "_ "
        return result.strip()

    def guess_letter(self, letter):
        letter = letter.lower()
        if letter in self.guessed_letters:
            print("You already guessed '{}'.".format(letter))
        elif letter in self.word:
            print("Nice! '{}' is correct.".format(letter))
            self.guessed_letters.append(letter)
        else:
            print("Oops! '{}' is wrong.".format(letter))
            self.guessed_letters.append(letter)
            self.attempts_left -= 1

    def display_hangman(self):
        print(self.HANGMAN_PICS[len(self.HANGMAN_PICS) - 1 - self.attempts_left])

    def is_won(self):
        for letter in self.word:
            if letter not in self.guessed_letters:
                return False
        return True

    def is_lost(self):
        return self.attempts_left <= 0

    def play(self):
        print("Welcome to Tollywood Hangman!")
        print("\nHint: {}".format(self.hint))  # ✅ Fixed: self.Hint → self.hint

        while not self.is_won() and not self.is_lost():
            print("\n" + "-" * 40)
            self.display_hangman()
            print("Word:", self.display_word())
            print("Attempts Left:", self.attempts_left)

            guess = input("Guess a letter: ").strip().lower()
            if len(guess) != 1 or not guess.isalpha():
                print("Please enter a single alphabet letter.")
                continue

            self.guess_letter(guess)

        print("\n" + "-" * 40)
        if self.is_won():
            print("Congratulations! You guessed the word:", self.word)
        else:
            self.display_hangman()
            print("Game Over! The word was:", self.word)


# Word list
word_list = [
    ("NTR", "young tiger"),
    ("bhAAi", "iconstar"),
    ("Ramcharan", "globalstar"),
    ("Prabhas", "rebelstar"),
    ("mahesh babu", "super star"),
    ("Balayya", "god of massess"),
    ("Chirangeevi", "megastar"),
]

#final result
game = HangmanGame(word_list)
game.play()
