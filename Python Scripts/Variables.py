# Variables.py

# We can check the 'type' of a variable by passing it to the 'type' function

integer_variable = 14
print(integer_variable, type(integer_variable))


float_variable = 14.97
print(float_variable, type(float_variable))

string_variable = 'This is a text (string) variable'
print(string_variable, type(string_variable))


boolean_variable = True
print(boolean_variable, type(boolean_variable))






# We can convert between variable types by passing the variable to the appropriate function

print('** Converting variables **')
integer_variable = float(integer_variable)
print(integer_variable, type(integer_variable))


float_variable = int(float_variable)
print(float_variable, type(float_variable))

boolean_variable = int(boolean_variable)
print(boolean_variable, type(boolean_variable))
