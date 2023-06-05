import random

print('''██    ██   ██████   ███   ██   ██████   ██    ██   ██████   ███   ██
██    ██  ██    ██  ████  ██  ██        ███  ███  ██    ██  ████  ██
████████  ████████  ██ ██ ██  ██  ████  ██ ██ ██  ████████  ██ ██ ██
██    ██  ██    ██  ██  ████  ██    ██  ██    ██  ██    ██  ██  ████
██    ██  ██    ██  ██   ███   ███████  ██    ██  ██    ██  ██   ███''')
print('=' * 60)

name = 'Please Enter yor name : '
nme = input(name)
print('=' * 60)

greet = [f'We are so excited to have you on our team, {nme}!',
         f'We are thrilled to have you at our terminal, {nme}!',
         f'Welcome {nme}!! 'f'lets start the exciting game']

print(random.choice(greet))
print('=' * 60)
words = {
    'COMPUTER': "A machine that performs processes, calculations and operations based on instructions provided",
    'PROGRAMMING': "A set of instructions fed into the computer that performs particular computation",
    'INHERITANCE': "What is the process in OOP when a child class"
                   " \nderrives all the features and characterstics from parents?",
    'POLYMORPHISM': "Having many forms",
    'DICTIONARY': "A collection of words and meanings",
    'COMPREHENSION': "A concise and readable way to create dictionary in python",
    'LAMBDA': 'An Anonymous Function',
    'ITERATION': 'Repeating something over and again, in a loop'
}

key, value = random.choice(list(words.items()))
computer_key = key
computer_value = value
print("Lets start with the word:\n")
print(computer_value)


# inp = input()


class Game:
    current_word = str(computer_key)
    wrong_count = 0
    list_of_guesses = len(computer_key) - 3

    def create_guess_list(self):
        # replc = str(random.choices(self.current_word, k=4))
        #
        # print(str(self.current_word.replace(replc, '_')))

        self.word = list(self.current_word)
        rand = random.choice(self.word)
        indx = self.current_word.index(rand)
        n_rand = random.choice(self.word)
        n_indx = self.current_word.index(n_rand)
        disp = '_' * len(computer_key)
        self.list_disp = list(disp)
        self.list_disp[indx] = rand
        self.list_disp[n_indx] = n_rand
        print(*self.list_disp)

        #
        # print(self.word)
        #
        # for i in self.current_word:
        #
        #     print(i, end="")

    def input(self):
        while True:
            inp = input("Enter a character").upper()
            if inp in self.word:
                print("Yes")
                indx=self.word.
                index = self.word.index(inp)
                self.list_disp[index]=inp
                print(*self.list_disp)


g = Game()
g.create_guess_list()
g.input()
