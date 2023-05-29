# a = 100
# b = 0
# try:
#     print(a / b)
# except:
#     print(f"cannot divide by {b}")
#
#
# def divide(a, b):
#     try:
#         print(f'Let\'s divide {a} by {b}')
#         print(a / b)
#
#     except ZeroDivisionError:
#         print("You should've known you cannot divide by zero")
#
#     except TypeError as a:
#         print(a)
#
#     except Exception:
#         print(Exception)
#
#
# divide(10, 'abc')

lst = [1, 'Himal', 101, 'Hats']


def print_index(index: int) -> all:
    try:
        print(f"The value at index {index} is :", lst[index])
    except IndexError:
        print("Index out of bound")
    else:
        print("I have handled exception")

    finally:
        print("Thank you for choosing this software")


print_index(1)

try:
    print(4/0)
except(TypeError,ZeroDivisionError) as e:
    print(type(e))
    print(e)
