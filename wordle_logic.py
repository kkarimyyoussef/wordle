# Attempting to recreate wordle from scratch 
# using No help from AI or any other online recourses 
# other than the python online doc for syntax help
import random

print("Welcome to Wordle of Day")

# array set-up 
# A random word generator from the array is selected
array_of_words = ["house", "stick", "bring", "casts"]
word = array_of_words[random.randint(0, len(array_of_words) - 1)]
print(word)

# Setting-up states 
# we can have Four states 
# - Green state -> letter is in the correct positon
# - Yello State -> letter is in the word but in the wrong position 
# - Red state -> letter is not found in the word
# - base state -> before the game evven starts all positions are set to base state


guess_array = []
guess = input("Enter your guess: ")

for num_of_guesses in range(5):
    for i in range(0, len(word)):
        
        # Validating the length of the word
        if (len(guess) < 5 or len(guess) > 5):
            print("Word Must 5 Letters Long")
            guess = input("Enter your guess: ")

        

        if(guess[i] == word[i]):
            guess_array.append(word[i] + " ")
        else:
            guess_array.append(" _ ")


final_string = ""

for i in range (len(word)):
    final_string += guess_array[i]

print(final_string)



# This is How I want the final box to look like in the console 
print(" The Guess Table")
print("-----------------")
print("|   _ _ _ _ _   |")
print("|               |")
print("|   _ _ _ _ _   |")
print("|               |")
print("|   _ _ _ _ _   |")
print("|               |")
print("|   _ _ _ _ _   |")
print("|               |")
print("|   _ _ _ _ _   |")
print("|               |")
print("-----------------")
