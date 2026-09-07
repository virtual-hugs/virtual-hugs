import os
import pygame
from activity_dataset import activities

# initialize pygame mixer and load the lofi music
pygame.mixer.init()

base_dir = os.path.dirname(__file__)
music_path = os.path.join(base_dir, 'lofi.mp3')
pygame.mixer.music.load(music_path)
pygame.mixer.music.play(-1) # play the music in a loop

# function get_rating prompts the user for a rating between 1-5, and return integer otherwise keep asking for integer
def get_rating(question):
    while True: # repeats until user enter correct value
        try:
            rating = int(input(question))

            if 1 <= rating <= 5: # if correct value, return rating
                return rating

            print("Please enter a number from 1 to 5.") # if more than 5 or less 1

        except ValueError:
            print("Please enter a number.") # if enter non-integer value

# this function calculates the match score between user_preferences and activity chract. 
# uses absolute difference between them, for example |3-5| = 2, and sum difference
# as difference is smaller, the match is better
def calculate_match(user_preferences, activity):
    difference = 0

    for characteristic in user_preferences:
        difference += abs(
            user_preferences[characteristic] - activity[characteristic]
        )

    return difference

print("Virtual Hugs Activity Recommender")
print("\nWhat are you looking for?")

# ask user for rating for each characteristic and stores their responses 
relaxing = get_rating("Relaxing (1-5): ")
fun = get_rating("Fun (1-5): ")
reflective = get_rating("Reflective (1-5): ")
short = get_rating("Short/Easy (1-5): ")

#dict with user's responses
user_preferences = {
    "relaxing": relaxing,
    "fun": fun,
    "reflective": reflective,
    "short": short
}

scores = []

# iterate through the activities and calculate match score for each activity
# it would help find best match for user preferences
for activity_name, activity_data in activities.items():
    score = calculate_match(user_preferences, activity_data)
    scores.append((activity_name, score))

scores.sort(key=lambda x: x[1]) # sort the scores in ascending order, from best to good

print("\n💙 Your recommendations:")

# print the top 3 recommendations based on the match score
print(f"1. {scores[0][0]} — Best Match")
print(f"2. {scores[1][0]} — Great Match")
print(f"3. {scores[2][0]} — Good Match")
