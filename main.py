# # print function
# print(20 * 24 * 60)
#
# # String concatenation
# print('20 days are ' + str(28800) + ' minutes')
#
# # String concatenation formatting
# print(f'20 days are {20 * 24 * 60} minutes')
#
seconds_in_day = 24 * 60 * 60
name_of_unit = 'seconds'


#
# print(f'5 days are {5 * seconds_in_day} seconds long')
# print(f'10 days are {10 * seconds_in_day} {name_of_unit} long')
#
#
# # Functions
# def days_to_units():
#     print(f'5 days are {5 * seconds_in_day} seconds long')
#     print('this is weird that you have to indent')
#
#
def days_to_units(user_input):
    print(f'{user_input} days have {user_input * seconds_in_day} {name_of_unit}')


#
#
# days_to_units(5)
#
#
# def add_two_nums(x, y):
#     print(f'{x} + {y} = {x + y}')
#
#
# add_two_nums(5, 3)

# User Input
# input()

# input('Enter number of days to find hours in those days\n')

# input saves as a string
# user_input = input('enter your favorite number\n')
#
# # Casting: String to a number
# user_input_as_number = int(user_input)
#
# print(f'your favorite number is {user_input}')
# # Wrong
# print(f'your number time 2 is {user_input * 2}')
# # Right
# print(f'your number times 2 is actually {user_input_as_number * 2}')


# input Validation
def divide_two_nums(x, y):
    if y <= 0:
        return "Cannot divide by zero"
    else:
        print(x/y)
        return f'{x / y}'


divide_two_nums(2, 0)


def days_to_units(x):
    if x > 0:
        return f'{x} day/s are {x * seconds_in_day} seconds long'
    elif x == 0:
        return 'number cannot be 0'
    else:
        return 'entered an invalid number'

user_input = input('enter a number of days\n')


def validate_and_execute():
    if user_input.isdigit():
        user_input_as_num = int(user_input)
        calculated_value = days_to_units(user_input_as_num)
        print(calculated_value)
    else:
        print('input is not valid')

validate_and_execute()
# print(type('string'))
# print(type(1))
# print(type(1.0))
# print(type(True))