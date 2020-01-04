# Main Program

import user_module as um   # 'as' is used to create an alias for user_module

base_string = 'Hello World'

um.show_letters_in_string(base_string)

reversed_string = um.reverse_letters_in_string(base_string)

print(reversed_string)
