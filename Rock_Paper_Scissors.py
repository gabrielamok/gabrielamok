import random

def get_computer_choice():
  """Generates a random choice for the computer.

  Returns:
    A string representing the computer's choice (rock, paper, or scissors).
  """

  choices = ["rock", "paper", "scissors"]
  return random.choice(choices)

def determine_winner(player_choice, computer_choice):
  """Determines the winner of the game.

  Args:
    player_choice: The player's choice.
    computer_choice: The computer's choice.

  Returns:
    A string indicating the winner or a tie.
  """

  if player_choice == computer_choice:
    return "It's a tie!"
  elif (player_choice == "rock" and computer_choice == "scissors") or \
       (player_choice == "paper" and computer_choice == "rock") or \
       (player_choice == "scissors" and computer_choice == "paper"):
    return "You win!"
  else:
    return "Computer wins!"

def play_game():
  """Plays a round of Rock-Paper-Scissors.

  Returns:
    A string indicating the winner or a tie.
  """

  player_choice = input("Enter your choice (rock, paper, or scissors): ").lower()
  computer_choice = get_computer_choice()

  print(f"You chose: {player_choice}")
  print(f"Computer chose: {computer_choice}")

  return determine_winner(player_choice, computer_choice)

if __name__ == "__main__":
  while True:
    result = play_game()
    print(result)

    play_again = input("Do you want to play again? (y/n): ").lower()
    if play_again != 'y':
      break