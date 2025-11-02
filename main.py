# Rock Paper Scissors Game

# Simple CLI game where a player chooses rock, paper, or scissors and plays against the computer.

import random  # standard library module to make random choices for the computer

def get_choices():
    # Prompt the player to enter their choice and ensure it's valid.
    # Returns a dict with keys 'player' and 'computer' containing the final choices.
    player_Choice = input('Enter a choice Rock, Paper, Scissors:  ').lower()  # get player input and normalize to lowercase
    options = ['rock', 'paper', 'scissors']  # allowed options

    # Validate player input: keep asking until a valid option is entered
    while player_Choice not in options:
        print("Invalid choice! Please try again.")
        player_Choice = input('Enter Rock, Paper, or Scissors: ').lower()

    # Let the computer choose randomly from the same options
    computer_Choice = random.choice(options)

    # If both choices are the same, inform the player and re-prompt until they differ.
    # This loop enforces that this implementation does not allow ties to stand.
    while player_Choice == computer_Choice:
        print(f"Both players chose {player_Choice}. Let's try again.")
        player_Choice = input('Enter Rock, Paper, or Scissors: ').lower()
        # validate again in case the player types an invalid option after a tie
        while player_Choice not in options:
            print("Invalid choice! Please try again.")
            player_Choice = input('Enter Rock, Paper, or Scissors: ').lower()
        computer_Choice = random.choice(options)

    # Package the choices in a dictionary for easy passing to the result-checking function
    choices = {'player': player_Choice, 'computer': computer_Choice}
    return choices

def check_Win(player, computer):
    # Determine the outcome of the round given the player's choice and the computer's choice.
    # Returns a string message indicating win/lose/tie and the winning rule.
    print(f'You chose: {player}, Computer chose: {computer}')  # echo both choices to the player

    # First check for a tie (this branch won't run with the current get_choices logic,
    # because ties are re-asked there, but it's kept for completeness)
    if player == computer:
        return 'It\'s a tie'
    # If player chose rock, compare against the computer's choice
    elif player == 'rock':
        if computer == 'scissors':
            return 'Rock smashes Scissors. YOU WIN'  # rock beats scissors
        else:
            return 'Paper covers Rock. YOU LOSE'     # paper beats rock
    # If player chose paper, compare against the computer's choice
    elif player == 'paper':
        if computer == 'rock':
            return 'Paper covers Rock. YOU WIN'      # paper beats rock
        else:
            return 'Scissors cuts Paper. YOU LOSE'   # scissors beats paper
    # If player chose scissors, compare against the computer's choice
    elif player == 'scissors':
        if computer == 'paper':
            return 'Scissors cuts Paper. YOU WIN'    # scissors beats paper
        else:
            return 'Rock smashes Scissors. YOU LOSE' # rock beats scissors

# Running the game: get choices from player and computer, evaluate the result, and print it.
choices = get_choices()  # prompt player and select a computer choice
result = check_Win(choices['player'], choices['computer'])  # determine the outcome
print(result)  # display the outcome to the player