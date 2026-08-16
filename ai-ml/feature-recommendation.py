import pygame

# initialize pygame mixer and load the lofi music
pygame.mixer.init()
pygame.mixer.music.load("ai-ml/lofi.mp3")
pygame.mixer.music.play(-1) # play the music in a loop

# print comments to the use about hte program
print("How are you feeling?")
print("1. Stressed")
print("2. Tired")
print("3. Bored")
print("4. Sad")
print("5. Good")

# collect user input
feeling = input("Write the number here> ")

# validate user input, so for now it only accepts numbers 1-5 + keep asking the user for input until they provide a valid number
while feeling not in ["1", "2", "3", "4", "5"]:
    print("Please choose a number between 1 and 5.")
    feeling = input("Write the number here> ")

# if-elif stats to provide recommendation
if feeling == "1":
    recommendation = "Try a breathing exercise!"
elif feeling == "2":
    recommendation = "Take a short break and get some rest!"
elif feeling == "3":
    recommendation = "Try a fun puzzle or game!"
elif feeling == "4":
    recommendation = "Listen to some calming music or talk to someone you trust!"
elif feeling == "5":
    recommendation = "Keep the good energy going! Try something creative!"

# print the recommendation to the user
print("\n💙 We recommend:")
print(recommendation)