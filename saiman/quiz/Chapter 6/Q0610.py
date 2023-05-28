# Create lambda functions for the following:
#
#     A lambda function that accepts a number and returns the square of it.
#     A lambda function that accepts a list of numbers and returns the list of squares of them
#     A lambda function that accepts the length in meter and returns the value in feet.
#     A lambda function that accepts 3 integer arguments for month, year, and day, and returns a single string in format YYYY/MM/DD format.
#     A lambda that accepts a sentence and returns the sentence with spaces replaced by hyphens.
#
#     # example
#     input_sentence = 'A quick brown fox jumps over the lazy dog.'
#
#     output_sentence = 'A-quick-brown-fox-jumps-over-the-lazy-dog.'
#


# square= lambda n: n**2
# print(square(6))



# meter_to_feet=lambda meter: 3.281*meter
#
# print(meter_to_feet(10))


# month_year_day= lambda m,y,d: print(f'{y}/0{m}/{d}')
# m=int(input("Enter month"))
# y=int(input("Enter year"))
# d=int(input("Enter day"))
# (month_year_day(m,y,d))


# a=[]
#
# while  True:
#     inp=int(input("Enter anum"))
#     a.append(inp)
#
#     ex=input("Add another [yes/no]")
#
#     if ex=='no':
#         break
#
#
#
# sqr_lst= lambda a: print([ i*i for i in a])
#
# sqr_lst([1,2,3,4,5])
#
#
space_by_hyphens=lambda sentence :  print('-'.join(sentence.split(" ")))


input_sentence = 'A quick brown fox jumps over the lazy dog.'

space_by_hyphens(input_sentence)





