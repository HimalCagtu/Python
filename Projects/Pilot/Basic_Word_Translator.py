from translate import Translator

print('=' * 60)
print('|', 'Enter the sentence'.center(58), '|\t')
print('|', '+' * 57, '|')
inp = input('\t')
print('|', 'Type the Source langauge'.center(58), '|\t')
print('|', '+' * 57, '|')
src = input('\t')

print('|', 'Type the Translation langauge'.center(58), '|\t')
print('|', '+' * 57, '|')
lang = input('\t')

trans = Translator(from_lang=src, to_lang=lang)

try:
    translation = Translator.translate(trans, inp)

    print('', f'{translation}'.center(58), '\t')
    print('=' * 60)
except:
    print("Error in one of the langauge")

#

# lst_of_choices = ['English', 'Nepali', 'Hindi', 'Japanese']
# # print(lst_of_choices)
# src = int(input("CHoose the source langauge\n"
#             "1.English\n"
#             "2.Nepali\n"
#             "3.Hindi\n"
#             "4.Japanese\n"))
#
# destination = int(input("CHoose the source langauge\n"
#             "1.English\n"
#             "2.Nepali\n"
#             "3.Hindi\n"
#             "4.Japanese\n"))
#
#
# if choice==1:
