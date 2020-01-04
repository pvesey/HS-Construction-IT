# Write to a File

file_name = input('Enter the filename: ')

grace_hopper_quotes = '''A ship in port is safe, but that's not what ships are built for.
It is often easier to ask for forgiveness than to ask for permission.
You don't manage people; you manage things. You lead people.
If it's a good idea, go ahead and do it. It's much easier to apologize than it is to get permission.
Leadership is a two-way street, loyalty up and loyalty down. Respect for one's superiors; care for one's crew.'''

# print(grace_hopper_quotes)

text_file = open(file_name, 'w')

text_file.write(grace_hopper_quotes)

text_file.close()
