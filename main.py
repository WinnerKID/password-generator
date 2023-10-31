import random
import string

print('Password Generator\n'
      'Choose the following required characters\n'
      '1. Must contain at least 1 lowercase character\n'
      '2. Must contain at least 1 uppercase character\n'
      '3. Must contain at least 1 special character\n'
      '4. Must be at least 5 characters long, up to 20 characters\n')

# Define the character sets
lower_chars = string.ascii_lowercase
upper_chars = string.ascii_uppercase
special_chars = string.punctuation

# Initialize an empty list to store selected character sets
selected_chars = []

# Function to select and add a character set to the selected_chars list
def select_character_set(char_set, description):
    user_choice = input(f'Include {description} in the password? (y/n): ')
    if user_choice.lower() == 'y':
        selected_chars.append(char_set)

# Let the user choose which character sets to include
select_character_set(lower_chars, 'at least 1 lowercase character')
select_character_set(upper_chars, 'at least 1 uppercase character')
select_character_set(special_chars, 'at least 1 special character')

# Check if the selected_chars list is empty and include lowercase characters by default
if not selected_chars:
    selected_chars.append(lower_chars)

# Function to specify the password length within the range [5, 20]
def specify_password_length():
    while True:
        length = input('Enter the desired password length (5 to 20): ')
        try:
            length = int(length)
            if 5 <= length <= 20:
                return length
            else:
                print('Invalid input. Please enter a number between 5 and 20.')
        except ValueError:
            print('Invalid input. Please enter a number.')

password_length = specify_password_length()

# Define a function to generate the password
def generate_password():
    # Initialize an empty list for the password
    password = []

    # Add random characters from the selected character sets to reach the specified length
    while len(password) < password_length:
        char_set = random.choice(selected_chars)
        password.append(random.choice(char_set))

    # Shuffle the characters to make it random
    random.shuffle(password)

    # Convert the list of characters to a string
    password = ''.join(password)

    return password

user_input = input('Press ENTER to create a password: \n')
if user_input == "":
    password = generate_password()
    print('Generated Password:', password)
    with open('storage.txt', 'a') as f:
        print(password, file=f)
else:
    print('Invalid input. Please press ENTER to generate a password.')
