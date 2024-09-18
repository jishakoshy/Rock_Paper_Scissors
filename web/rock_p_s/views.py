from django.shortcuts import render
from django.http import JsonResponse
import random

# Function to get computer's choice
def get_computer_choice():
    choices = ['rock', 'paper', 'scissors']
    return random.choice(choices)

# Function to determine the winner
def determine_winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        return 'draw'
    elif (player_choice == 'rock' and computer_choice == 'scissors') or \
         (player_choice == 'paper' and computer_choice == 'rock') or \
         (player_choice == 'scissors' and computer_choice == 'paper'):
        return 'player'
    else:
        return 'computer'

# Render the game page
def index(request):
    return render(request, 'rock.html')

# Handle the game logic and return the result as JSON
def play_game(request):
    if request.method == 'POST':
        player_choice = request.POST.get('choice')
        computer_choice = get_computer_choice()
        result = determine_winner(player_choice, computer_choice)
        return JsonResponse({
            'player_choice': player_choice,
            'computer_choice': computer_choice,
            'result': result
        })
