#logic.py

# Python includes logic tests that we can perform on our Variables.  The
# results are returned as Boolean values

large_integer = 250
small_integer = 100

less_than_test = small_integer < large_integer
print(less_than_test)

greater_than_test = small_integer > large_integer
print(greater_than_test)

equality_test = (small_integer == large_integer)
print(equality_test)

# We can also test the variales properties


variable_type_test = (type(small_integer)== type(large_integer))
print(variable_type_test)
