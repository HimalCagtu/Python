import random

print('=' * 60)
print('|', "Enter your name".center(56), '|')
print('+' * 60)
user_name = input()
choices = ['rock', 'paper', 'scissor']


# print(bot_choice)

class Game:
    user_score = 0
    _bot_score = 0
    _draws = 0
    bot_choice = ''
    user_choice = ''
    match = 0

    def __init__(self, user_name):
        self.user_name = user_name
        # self.bot_choice = bot_choice
        # self.user_choice = user_choice

    def get_bot_choice(self):
        print(f"Bot choice is {self.bot_choice}")

    # while True:
    def main_game(self):
        while True:
            self.bot_choice = random.choice(choices)
            print('+' * 60)
            print('|', "Enter your choice".ljust(56), '|')
            print('|', "->rock".ljust(56), '|')
            print('|', "->paper".ljust(56), '|')
            print('|', "->scissor".ljust(56), '|')
            print('+' * 60)
            self.user_choice = input().lower()
            print('|', f'Bot choice is {self.bot_choice}'.center(56), '|')

            if self.bot_choice == 'rock':
                if self.user_choice == 'paper':
                    print('+' * 60)
                    print('|', f"{user_name} won".center(56), '|')
                    print('+' * 60)
                    self.user_score += 1
                    print(self.user_score)
                elif self.user_choice == 'scissor':
                    print('+' * 60)
                    print('|', "bot won".center(56), '|')
                    print('+' * 60)
                    self._bot_score += 1
                    print(self._bot_score)
                else:
                    print('+' * 60)
                    print('|', "It's a draw".center(56), '|')
                    print('+' * 60)
                    self._draws += 1
                    print(self._draws)

            elif self.bot_choice == 'paper':
                if self.user_choice == 'scissor':
                    print('+' * 60)
                    print('|', f"{user_name} won".center(56), '|')
                    print('+' * 60)
                    self.user_score += 1
                    print(self.user_score)
                elif self.user_choice == 'rock':
                    print('+' * 60)
                    print('|', "bot won".center(56), '|')
                    print('+' * 60)
                    self._bot_score += 1
                    print(self._bot_score)
                else:
                    print('+' * 60)
                    print('|', "It's a draw".center(56), '|')
                    print('+' * 60)
                    self._draws += 1
                    print(self._draws)
            else:
                if self.user_choice == 'rock':
                    print('+' * 60)
                    print('|', f"{user_name} won".center(56), '|')
                    print('+' * 60)
                    self.user_score += 1
                    print(self.user_score)
                elif self.user_choice == 'paper':
                    print('+' * 60)
                    print('|', "bot won".center(56), '|')
                    print('+' * 60)
                    self._bot_score += 1
                    print(self._bot_score)

                else:
                    print('+' * 60)
                    print('|', "It's a draw".center(56), '|')
                    print('+' * 60)
                    self._draws += 1
                    print(self._draws)
            self.match += 1
            print('+' * 60)
            print('|', f'You\'ve palyed {self.match} matches'.center(56), '|')
            print('|', ''.center(56), '|')
            print('|', f'User_Won : {self.user_score}'.ljust(18), f''
                                                                  f'Draws : {self._draws}'.ljust(18),
                  f'Bot_Won : {self._bot_score}'.ljust(18), '|')
            print('+' * 60)
            print('|', "Do you want to play again? [YES/NO]".ljust(56), '|\n\t')
            again = input().lower()
            if again == 'no':
                exit()


g1 = Game(user_name)
g1.main_game()
