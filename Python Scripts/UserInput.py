# User Input.py

# To get input from the user we use the 'Input' function

user_name = input('Enter your Name: ')

print('Your name is:', user_name)

print('Now enter some other data types to see how Python interprets them:')

type_one = input('Enter some data: ')
print('The data-type is', type(type_one))

type_two = input('Enter some data: ')
print('The data-type is', type(type_two))

type_three = input('Enter some data: ')
print('The data-type is', type(type_three))

# Note that the input function always returns a string.  If you want other
# variable types, then you have to convert them.
