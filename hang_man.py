import random

print('H A N G M A N')

list_of_words = ['python', 'java', 'kotlin', 'javascript']

n = random.randint(0, (len(list_of_words) - 1))

selected_word = list_of_words[n]

solved_string = "-" * len(selected_word)

list_of_characters = list(selected_word)

guessed_character = []
turns = 8

while True:
    game_menu = input("""Type "play" to play the game, "exit" to quit: """)
    print()
    if game_menu == "play":
        print(solved_string)
        while "-" in list(solved_string):
            letter = input('Input a letter: ')
            if len(letter) != 1:
                print("You should input a single letter")
                print()
                print(f'{solved_string}')
            elif not letter.islower():
                print("It is not an ASCII lowercase letter")
                print()
                print(f'{solved_string}')
            elif letter in guessed_character:
                print("You already typed this letter")
                print()
                print(f'{solved_string}')
            elif letter not in list_of_characters:
                turns -= 1
                guessed_character.append(letter)
                if turns == 0:
                    print("No such letter in the word")
                    print("You lost!")
                    break
                else:
                    print("No such letter in the word")
                    print()
                    print(f'{solved_string}')
            elif letter in list_of_characters:
                guessed_character.append(letter)
                for index, character in enumerate(list_of_characters):
                    if character == letter:
                        solved_string = solved_string[:index] + letter + solved_string[index + 1:]
                print()
                print(f'{solved_string}')
        else:
            print('You guessed the word!')
            print('You survived!')
        continue
    elif game_menu == "exit":
        break
