from _datetime import datetime

user_input = input('Enter your goal with a deadline seperated by a : please!\n example: learn to cook chicken: 10.05.2022\n')

input_list = user_input.split(':')

goal = input_list[0]
deadline = input_list[1]

print(datetime.strptime(deadline, '%d.%m.%Y'))
print(type(datetime.strptime(deadline, '%d.%m.%Y')))

deadline_date = datetime.strptime(deadline, '%d.%m.%Y')

print(input_list)

todays_date = datetime.today()

time_till_deadline = deadline_date - todays_date

print(datetime.today())

print(f'days remaining till goal: {goal} are {time_till_deadline}')