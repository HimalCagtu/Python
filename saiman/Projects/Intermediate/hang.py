import random
from hangman import HANGMAN, LOOSER, WINNER

print("*" * 69)
print(HANGMAN)
print("*" * 69)
name = input("Enter your name:  ")
words = {
    'computer': 'an electronic device that manipulates information, or data',
    'programming': ' a technological process for telling a computer which tasks to perform in order to solve problems',
    'inheritance': 'the process by which genetic information is passed on from parent to child',
    'polymorphism': 'a feature of object-oriented programming languages that allows a specific routine to use variables of different types at different times',
    'dictionary': 'a list of comma-separated key-value pairs wrapped around curly braces ({})',
    'comprehension': 'a concise and readable way to create dictionaries in Python.',
    'lambda': 'function can take any number of arguments, but can only have one expression.',
    'iteration': 'Repetitive execution of the same block of code over and over'}
greet = [f'We are so excited to have you on our team, {name}!', f'We are thrilled to have you at our terminal, {name}!',
         f'Welcome {name}!! lets start the exciting game']


def list_to_str(value):
    temp = ""
    for v in value:
        temp += v

    return temp


class Game:
    def __init__(self, name):
        self.name = name
        self.current_word = ''
        self.attempts = 0
        self.guess = 0
        self.lives = 5
        self.crnt_word = ''

    def display_Greeeting(self):
        print(random.choice(greet))
        print("*" * 69)

    def find_indices(self, word, value):
        templist = []
        for count, w in enumerate(word):
            if w == value:
                templist.append(count)
        # return [
        #     index for index in enumerate(word)
        #     if index == value
        #
        # ]
        return templist

    def game(self):

        print("Lets start with the word:")
        key, value = random.choice(list(words.items()))
        key = key.upper()
        self.current_word = list(key)
        rand = random.choice(self.current_word)
        self.rand = random.choice(self.current_word)
        self.indx = self.find_indices(self.current_word, self.rand)
        # print(n_indx)
        # n_indx = self.current_word.index(n_rand)
        indx = self.current_word.index(rand)
        self.disp = '_' * len(key)
        self.lis_disp = list(self.disp)
        self.lis_disp[indx] = rand
        for R_value in self.indx:
            self.lis_disp[R_value] = self.rand

        self.disp = list_to_str(self.lis_disp)
        value = value.upper()
        print("Hint: ", value, '\n')
        print(f"Total attempts: {self.attempts}")
        print(f"Total correct guesses: {self.guess}")
        print(f"Remaining lives: {self.lives}")
        print("+", "-" * 67, "+")
        print("|", " ".center(67), "|")
        print("|", f"{self.disp}".center(67), "|")
        print("|", " ".center(67), "|")
        print("+", "-" * 67, "+")

    def user_input(self):
        while True:
            # g1 = Game(name)
            # g1.game()
            while self.lives != 0:
                u_input = input("Enter a letter: ").upper()
                if u_input in self.current_word:
                    indexx = self.current_word.index(u_input)
                    self.n_indx = self.find_indices(self.current_word, u_input)
                    for R_value in self.n_indx:
                        self.lis_disp[R_value] = u_input
                    self.lis_disp[indexx] = u_input
                    self.disp = list_to_str(self.lis_disp)
                    self.attempts += 1
                    self.guess += 1
                    print(f"Total attempts: {self.attempts}")
                    print(f"Total correct guesses: {self.guess}")
                    print(f"Remaining lives: {self.lives}")
                    print("+", "-" * 67, "+")
                    print("|", " ".center(67), "|")
                    print("|", f"{self.disp}".center(67), "|")
                    print("|", " ".center(67), "|")
                    print("+", "-" * 67, "+")
                    self.crnt_word = list_to_str(self.current_word)
                    if self.disp == self.crnt_word:
                        break
                else:
                    self.attempts += 1
                    self.lives -= 1
                    print(f"Total attempts: {self.attempts}")
                    print(f"Total correct guesses: {self.guess}")
                    print(f"Remaining lives: {self.lives}")
                    print("+", "-" * 67, "+")
                    print("|", " ".center(67), "|")
                    print("|", f"{self.disp}".center(67), "|")
                    print("|", " ".center(67), "|")
                    print("+", "-" * 67, "+")

            if self.disp == self.crnt_word:
                print(WINNER)
                break

            else:
                print(LOOSER)
                break
        print('|', "DO you want to play again? [YES/NO]".center(67), '|')
        choice = int(input()).lower
        if choice == 'no':

            exit()

        else:
            g2 = Game(name)
            g2.game()
            g2.user_input()


g = Game(name)
g.display_Greeeting()
g.game()
g.user_input()
