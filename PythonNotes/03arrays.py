## This introduces the concept of simple lists


my_numbers = [10,40,60,80,60]

for number in my_numbers:
    print("my number is:", number)


## A list can be words too

my_fruit_list = ['apples', 'oranges', 'lemons', 'grapes']

for fruit in my_fruit_list:
    print("I don't like", fruit)


# we can also pull out a single value from a list by referring to its index value;
# note that the index value starts at 0

print(my_fruit_list[0])
print(my_fruit_list[3])