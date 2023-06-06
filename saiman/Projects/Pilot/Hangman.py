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
    total_correct_guess = 0
    list_of_guesses = len(computer_key) - 3
    str = ''

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
        print('+', '-' * 56, '+')
        print('|', ''.center(56), '|')
        for i in self.list_disp:
            self.str += i
        print('|', f'{self.str}'.center(56), '|')
        print('|', ''.center(56), '|')
        print('+', '-' * 56, '+')

        #
        # print(self.word)
        #
        # for i in self.current_word:
        #
        #     print(i, end="")

    def find(self, word, value):
        self.indx = []
        for k, v in enumerate(word):
            if v == value:
                self.indx.append(k)
            return self.indx

    def list_to_str( vall):
        str = ''
        for i in vall:
            str += i
        return str

    def input(self):
        while True:
            inp = input("Enter a character").upper()



            indx = self.find(self.word, inp)

            print(indx)
            strng = self.list_to_str(indx)
            print(strng)
            self.list_disp[int(strng)] = inp
            print('+', '-' * 56, '+')
            print(*self.list_disp)
            print('+', '-' * 56, '+')
            if self.word == self.list_disp:
                print("Winner")



            else:
                self.wrong_count += 1
                print(self.wrong_count)


g = Game()
g.create_guess_list()
g.input()
