# UserDefinedFunction.py

def print_some_text():
    print('This is some text that will be used a lot')

def request_integer_value():
    input_value = int(input('Enter an intger value: '))
    return input_value

def product_of_two_values(v1, v2):
    return v1 * v2

print_some_text()

print('--- Product of two numbers:')
val1 = request_integer_value()
val2 = request_integer_value()

print(product_of_two_values(val1, val2))
