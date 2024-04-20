#Xiaoxia Ning

#4/20/2024

#P5HW 

#This program is an interactive Math Quiz that offers users the opportunity to practice addition and subtraction with random numbers, providing immediate feedback and tracking the number of attempts until the correct answer is given.

import random

def display_title():
    title = "Welcome to Math Quiz"
    print(title)
    print()  # Adds an empty line for better formatting

def display_options():
    print("MAIN MENU\n------------------")
    print("1. Adding Random Numbers")
    print("2. Subtracting Random Numbers")
    print("3. Exit\n")

def addition_quiz():
    random_num1 = random.randint(1, 100)
    random_num2 = random.randint(1, 100)
    correct_answer = random_num1 + random_num2
    guesses = 0
    
    while True:
        if guesses == 0:  # Display the numbers only for the first guess
            print(f"  {random_num1}")
            print(f"+ {random_num2}")
            print()
        user_answer = int(input("Enter answer: \n" if guesses == 0 else "Try again: "))
        guesses += 1
        
        if user_answer == correct_answer:
            print(f"Congratulations!!! Your answer is correct.")
            print(f"Number of guesses: {guesses}\n")
            break
        elif user_answer < correct_answer:
            print("Sorry, guess is too low.\n")
        else:
            print("Sorry, guess is too high.\n")

def subtraction_quiz():
    random_num1 = random.randint(1, 100)
    random_num2 = random.randint(1, 100)
    correct_answer = random_num1 - random_num2
    guesses = 0
    
    while True:
        if guesses == 0:  # Display the numbers only for the first guess
            print(f"  {random_num1}")
            print(f"- {random_num2}")
            print()
        user_answer = int(input("Enter answer: " if guesses == 0 else "Try again: "))
        guesses += 1
        
        if user_answer == correct_answer:
            print(f"Congratulations! Your answer is correct.")
            print(f"Number of guesses: {guesses}\n")
            break
        elif user_answer > correct_answer:
            print("Sorry, guess is too high.\n")
        else:
            print("Sorry, guess is too low.\n")

def math_quiz():
    display_title()
    while True:
        display_options()
        choice = input("Please choose one of the menu options: ")
        
        if choice == "1":
            addition_quiz()
        elif choice == "2":
            subtraction_quiz()
        elif choice == "3":
            print("Thank you for playing... ")
            print("Bye!!")
            break
        else:
            print("Invalid entry. Please enter 1, 2, or 3.")

# Call the math_quiz function to start the program
math_quiz()
