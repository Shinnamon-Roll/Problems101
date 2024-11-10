import random

def show_instructions():
    print("Welcome to the Number Guessing Game!")
    print("1. The system will randomly select a number between 1 and 100.")
    print("2. Your task is to guess the number.")
    print("3. After each guess, you will be informed if your guess is too high, too low, or correct.")
    print("4. Keep guessing until you find the correct number.")
    print("5. The game will show you the number of attempts you took to guess the number.")

def start_new_game():
    target_number = random.randint(1, 100)
    attempts = 0
    while True:
        guess = int(input("Guess a number between 1 and 100: "))
        attempts += 1
        if guess < target_number:
            print("Your guess is too low. Try again!")
        elif guess > target_number:
            print("Your guess is too high. Try again!")
        else:
            print(f"Congratulations! You guessed the number correctly in {attempts} attempts.")
            break

def number_guessing_game():
    while True:
        print("\nMenu:")
        print("1. Start New Game")
        print("2. Show Instructions")
        print("3. Exit")
        option = input("Please select an option: ")
        
        if option == '1':
            start_new_game()
        elif option == '2':
            show_instructions()
        elif option == '3':
            print("Thank you for playing! Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")

number_guessing_game()
