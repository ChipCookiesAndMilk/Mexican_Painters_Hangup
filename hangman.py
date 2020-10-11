import random

painters_dictionary = {0: 'kahlo', 1: 'rivera', 2: 'ortiz', 3: 'carrington', 4: 'velasco', 5: 'atl', 6: 'reyes',
                       7: 'revueltas', 8: 'tamayo', 9: 'ogorman', 10: 'siquiros', 11: 'orozco', 12: 'izquierdo',
                       13: 'gerzso', 14: 'cuevas', 15: 'herran'}


def display_menu():
    print('\t\tWelcome to MEXICAN painters \n\t\t\tand\n\t\tH A N G M A N\n')
    print('Press 1 to Start game\t Press 0 to End game')
    try:
        return int(input('Option: '))
    except ValueError:
        return -1


# Save a word into a list as characters
def split(word):
    return [char for char in word]


# Display and play
def display_word():
    # a list is created in order to save the letters in the position
    # the range [0,15] represents the length of the 'painters' dictionary
    painter_list = split(painters_dictionary.get(random.randint(0, 15)))
    # is the list that will store the player's progress
    player_progress_list = []
    # opportunities the player originally has
    opportunities_missing = 3
    # was the word completed?
    completed = len(painter_list)

    # debug
    # print(painter_list)
    # fill up the list to be displayed with '_'
    for index in range(len(painter_list)):
        player_progress_list.append('_ ')

    # display current progress of the player helps to visualize the length of the word to be found
    print(player_progress_list)

    # if the player still has opportunities and the word is not completed then play
    while opportunities_missing > 0 and completed > 0:
        # helps in pointing if the letter was found in the list, avoids decrementing opportunities for the player
        letter_found = 0
        # helps storing the position of the list
        # in here it resets
        index = 0
        # tries the player does and it fails
        print('\nOpportunities_missing: '+str(opportunities_missing)+'\n')
        input_letter = input('Give a letter : ').lower()

        # gets the character at painters_list
        for letter in painter_list:
            # compare the players input vs the painters_list's content
            if input_letter == letter:
                # if player_progress_list, still has the '_' it means that a letter was found by
                # player so add from painter_list that has the word to be found
                if player_progress_list[index] == '_ ':
                    # indicate a character was found
                    letter_found = 1
                    # now there are less letters to be found
                    completed = completed - 1
                    # save the letter at position found
                    # player_progress_list[index] = painter_list[index]
                    player_progress_list[index] = input_letter
            # what ever is on the player_progress_list display it
            print(player_progress_list[index]+' ', end='')
            # move to the next position
            index = index + 1
        # if the for loop ends and not a single letter was found then decrease the number of opportunities_missing
        if letter_found == 0:
            opportunities_missing = opportunities_missing - 1
    # if chances to be mistaken are over or player won
    if opportunities_missing == 0:
        print('\n\n\tYou lose ):')
    elif completed == 0 and opportunities_missing > 0:
        print('\n\n\tYou win!')


start = display_menu()

# the option menu will be displayed here else exit
if start == 1:
    print('\n\n-----------------------------\nFind the artist...\n')
    # Play game
    display_word()
elif start == 0:
    print('\nThanks for playing. Bye!')
else:
    print('Please, verify your option...Exit...')