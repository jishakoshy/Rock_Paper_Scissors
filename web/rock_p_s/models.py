# from django.db import models

# # Create your models here.
# from django.db import models
# from django.utils import timezone

# class Game(models.Model):
#     PLAYER_CHOICES = [
#         ('rock', 'Rock'),
#         ('paper', 'Paper'),
#         ('scissors', 'Scissors'),
#     ]

#     RESULT_CHOICES = [
#         ('player', 'Player Wins'),
#         ('computer', 'Computer Wins'),
#         ('draw', 'Draw'),
#     ]

#     player_choice = models.CharField(max_length=10, choices=PLAYER_CHOICES)
#     computer_choice = models.CharField(max_length=10, choices=PLAYER_CHOICES)
#     result = models.CharField(max_length=10, choices=RESULT_CHOICES)
#     created_at = models.DateTimeField(default=timezone.now)

#     def __str__(self):
#         return f"{self.player_choice} vs {self.computer_choice} - {self.result} on {self.created_at.strftime('%Y-%m-%d %H:%M:%S')}"
