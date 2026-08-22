import os
import pygame
from recommendation import recommendations

# initialize pygame mixer and load the lofi music
pygame.mixer.init()

base_dir = os.path.dirname(__file__)
music_path = os.path.join(base_dir, 'ai-ml', 'lofi.mp3')
pygame.mixer.music.load(music_path)
pygame.mixer.music.play(-1) # play the music in a loop

# made an universal function that validate if the user enter write number
def get_number(prompt, minimum, maximum):
    while True:
        try:
            number = int(input(prompt))

            if minimum <= number <= maximum:
                return number

            print(f"Please choose a number between {minimum} and {maximum}.")

        except ValueError:
            print("Please enter a number.")

# print comments to the use about hte program
print("How are you feeling?")
print("1. Stressed")
print("2. Tired")
print("3. Bored")
print("4. Sad")
print("5. Good")

# collect user input
feeling_number = get_number("Write the number here > ", 1, 5)


# if-elif statements to determine the user's feeling and reason for that feeling
if feeling_number == 1:
    feeling = "stressed"

    print("\nWhat's making you feel stressed?")
    print("1. School")
    print("2. Family")
    print("3. Friends")
    print("4. Something else")

    reason_number = get_number("Write the number here > ", 1, 4)

    reasons = {
        1: "school",
        2: "family",
        3: "friends",
        4: "other"
    }

    reason = reasons[reason_number]
elif feeling_number == 2:
    feeling = "tired"

    print("\nWhat kind of tired are you?")
    print("1. School/work")
    print("2. Socially")
    print("3. Physically")
    print("4. Mentally")

    reason_number = get_number("Write the number here > ", 1, 4)

    reasons = {
        1: "school",
        2: "social",
        3: "physical",
        4: "mental"
    }

    reason = reasons[reason_number]
elif feeling_number == 3:
    feeling = "bored"

    print("\nWhat would you like to do?")
    print("1. Something creative")
    print("2. Something productive")
    print("3. Something entertaining")
    print("4. Something social")

    reason_number = get_number("Write the number here > ", 1, 4)

    reasons = {
        1: "creative",
        2: "productive",
        3: "entertainment",
        4: "social"
    }

    reason = reasons[reason_number]
elif feeling_number == 4:
    feeling = "sad"

    print("\nWhat would help you most right now?")
    print("1. Relax")
    print("2. Distract myself")
    print("3. Talk to someone")
    print("4. Have some alone time")

    reason_number = get_number("Write the number here > ", 1, 4)

    reasons = {
        1: "relax",
        2: "distract",
        3: "talk",
        4: "alone"
    }

    reason = reasons[reason_number]
elif feeling_number == 5:
    feeling = "good"

    print("\nWhat do you feel like doing?")
    print("1. Create something")
    print("2. Be productive")
    print("3. Have fun")
    print("4. Help someone")

    reason_number = get_number("Write the number here > ", 1, 4)

    reasons = {
        1: "creative",
        2: "productive",
        3: "fun",
        4: "help"
    }

    reason = reasons[reason_number]

# get the recommendation based on the user's feeling and reason
recommendation = recommendations[feeling][reason]

# print the recommendation to the user
print("\n💙 We recommend:")
print(recommendation)
