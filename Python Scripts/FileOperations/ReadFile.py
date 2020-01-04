# ReadFile.py

file_name = str(input('Enter the filename to read: '))

text_file = open(file_name, 'r')

text = text_file.read()

text_file.close()

print(text)
