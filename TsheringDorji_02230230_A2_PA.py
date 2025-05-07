import random   # for random number to generate

def guess_number_game():
    number = random.randint(1, 10)   #generating a random number between 1 to 10
    print("\nWelcome to guessing number game!")   #telling user about the game
    print("I have selected a number between 1 and 10.")   #informing user about the range of numbers
    score = 9   #initializing score to 9
    while True:  #creating an infinite loop until the user guesses the number
        try:   #taking unput from the user
            user = int(input("Guess a number:"))   #asking user to guess a number
            if user < number:
                print("Your guess is too low!")
                score -= 1   #decrementing score by 1
            elif user > number:
                print("Your guess is too high!")
                score -= 1   #decrementing score by 1
            else:   #if user guesses the correct number
                print(f"Congratulations! You guessed the number {number} correctly!")   #congratulating user for guessing the correct number
                score += 1
                print(f"Your score is {score}")   #printing the score
                return main()   #ending the loop
            
        except ValueError:   #if user enters a non-integer value
            print("Please enter a valid number.")

def rock_paper_scissor():
    choices = ["rock", "paper", "scissors"]   # creating a list of options for the computer
    print("\nWelcome to Rock, Paper, Scissors game!")   # telling user about the game
    score = 0   # initializing score to 0

    while True:
        computer = random.choice(choices)   # computer randomly chooses rock, paper, or scissors
        player = input("Enter your choice (rock, paper, scissors): ").lower()   # taking input from the user and converting it to lowercase
        if player not in choices:   # if user enters an invalid option
            print("Invalid choice. Please select rock, paper, or scissors.")
            continue
        print(f"Computer chose: {computer}")   # displaying computer's choice
        if player == computer:   # if user and computer choose the same option
            print("It's a tie!")
            print(f"Your score remains: {score}")
        elif (player == "rock" and computer == "scissors") or (player == "paper" and computer == "rock") or (player == "scissors" and computer == "paper"):   # user wins
            print("You win!")
            score += 1   # incrementing score by 1
            print(f"Your score is now: {score}")
        else:   # user loses
            print("You lose!")
            score -= 1   # decrementing score by 1
            print(f"Your score is now: {score}")

        play_again = input("Do you want to play again? (yes/no): ").lower()   # asking user if they want to play again
        if play_again != "yes":
            print(f"Final score: {score}")
            return main()

def trivia_pursuit_quiz():
    questions = {
        "What is the first letter of the English alphabet?": "a",
        "What is the capital of Bhutan?": "thimphu",
        "What is the full form of CST?": "college of science and technology",
        "What is the full form of ICE?": "instrumentation and control engineering",
    }
    print("\nWelcome to Trivia Pursuit Quiz!")
    print("Answer the following questions:")
    score = 0   #initializing score to 0
    for question, answer in questions.items():   #iterating through the questions and answers
        user_answer = input(f"{question} ").lower()   #taking input from the user and converting it to lowercase
        if user_answer == answer:   #if user answers correctly
            print("Correct!")
            score += 1   #incrementing score by 1
        else:
            print("Incorrect!")
    print(f"Your score is {score}/{len(questions)}")   #printing the score out of total number of questions

def overall_score_record(scores):   # function to record the scores
    total_score = sum(scores)   # summing up all the scores
    print(f"\nYour overall score across all games is: {total_score}")   # displaying the total score
    return total_score


def main():
    scores = []  # List to keep track of scores from all games

    while True:
        print("\nSelect a game (1-4):")
        print("1. Guess the Number")
        print("2. Rock, Paper, Scissors")
        print("3. Trivia Pursuit Quiz")
        print("4. Overall Score Record")
        print("5. Exit")

        gamer = int(input("Enter your choice: "))   # Taking input from the user to select a game
        if gamer == 1:
            guess_number_game()
            scores.append(9)  # Example score for Guess the Number (update logic as needed)
        elif gamer == 2:
            rock_paper_scissor()
            scores.append(5)  # Example score for Rock, Paper, Scissors (update logic as needed)
        elif gamer == 3:
            trivia_pursuit_quiz()
            scores.append(3)  # Example score for Trivia Pursuit Quiz (update logic as needed)
        elif gamer == 4:
            overall_score_record(scores)  # Call the overall score function before exiting
            print("Thank you for playing!")
            break
        elif gamer == 5:
            print("Exiting the game. Thank you for playing!")
            break
        
        else:
            print("Invalid choice. Please select a valid game.")

if __name__ == "__main__":
    main()