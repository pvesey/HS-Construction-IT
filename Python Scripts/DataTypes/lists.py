# lists.py


colors = ['red', 'orange', 'yellow', 'green', 'blue', 'violet']

for color in colors:
    print(color)

# we can also access properties of the lists

print(colors.count('red'))

colors.append('indigo')

print(colors)
colors.remove('indigo')
print(colors)


colors.insert(5, 'indigo') # Insert an item into a specific placex
print(colors)

colors.reverse()
print(colors)


colors.sort()
print(colors)

index_value = colors.index('green')
print(index_value)

colors.pop(index_value)
print(colors)

colors.append('red')
colors.append('red')
colors.append('red')
colors.append('red')
print(colors)
print(colors.count('red'))

print(len(colors))
