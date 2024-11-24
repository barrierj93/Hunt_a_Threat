import csv
import random
import os

# CSV file name
csv_file = "hacker_groups_cleaned.csv"

# Load hacker data from the CSV file
def load_hacker_data(file):
    hacker_data = []
    with open(file, mode='r', encoding='utf-8') as f:
        reader = csv.reader(f, delimiter=';')
        next(reader)  # Skip headers
        for row in reader:
            hacker_data.append({"ID": row[0], "Name": row[1], "Description": row[3]})
    return hacker_data

# Generate a random question
def generate_question(data):
    correct = random.choice(data)  # Select a random entry
    incorrect_options = random.sample([h for h in data if h != correct], 3)  # Three incorrect options
    options = incorrect_options + [correct]  # Combine correct and incorrect options
    random.shuffle(options)  # Shuffle the options
    return correct, options

# Display a question
def ask_question(correct, options):
    print("\n** Guess the Hacker Group **")
    print(f"Description: {correct['Description']}")
    print("Options:")
    for i, option in enumerate(options, 1):
        print(f"{i}. {option['Name']}")
    return correct, options

# Display the "YOU'VE BEEN PWND" ASCII art with a skull
def show_hacker_ascii():
    skull_ascii = r'''
                 uuuuuuu
             uu$$$$$$$$$$$uu
          uu$$$$$$$$$$$$$$$$$uu
         u$$$$$$$$$$$$$$$$$$$$$u
        u$$$$$$$$$$$$$$$$$$$$$$$u
       u$$$$$$$$$$$$$$$$$$$$$$$$$u
       u$$$$$$$$$$$$$$$$$$$$$$$$$u         ______________________ 
       u$$$$$$"   "$$$"   "$$$$$$u        |     YOU'VE BEEN      |  
       "$$$$"      u$u       $$$$"        |        PWND          |        
        $$$u       u$u       u$$$         |______________________|
        $$$u      u$$$u      u$$$
         "$$$$uu$$$   $$$uu$$$$"
          "$$$$$$$"   "$$$$$$$"
            u$$$$$$$u$$$$$$$u
             u$"$"$"$"$"$"$u
  uuu        $$u$ $ $ $ $u$$       uuu
 u$$$$        $$$$$u$u$u$$$       u$$$$
  $$$$$uu      "$$$$$$$$$"     uu$$$$$$
u$$$$$$$$$$$uu    """""    uuuu$$$$$$$$$$
$$$$"""$$$$$$$$$$uuu   uu$$$$$$$$$"""$$$"
 """      ""$$$$$$$$$$$uu ""$"""
           uuuu ""$$$$$$$$$$uuu
  u$$$uuu$$$$$$$$$uu ""$$$$$$$$$$$uuu$$$
  $$$$$$$$$$""""           ""$$$$$$$$$$$"
   "$$$$$"                      ""$$$$""   
     $$$"                         $$$$"
    '''
    # Clear terminal and print the figure
    os.system('cls' if os.name == 'nt' else 'clear')
    print(skull_ascii)

# Display ASCII art banner for game start
def show_game_banner():
    banner = r"""
 /$$   /$$                       /$$                        
| $$  | $$                      | $$                        
| $$  | $$ /$$   /$$ /$$$$$$$  /$$$$$$          /$$$$$$     
| $$$$$$$$| $$  | $$| $$__  $$|_  $$_/         |____  $$    
| $$__  $$| $$  | $$| $$  \ $$  | $$            /$$$$$$$    
| $$  | $$| $$  | $$| $$  | $$  | $$ /$$       /$$__  $$    
| $$  | $$|  $$$$$$/| $$  | $$  |  $$$$/      |  $$$$$$$    
|__/  |__/ \______/ |__/  |__/   \___/         \_______/    
                                                            
                                                            
                                                            
 /$$$$$$$$ /$$                                       /$$    
|__  $$__/| $$                                      | $$    
   | $$   | $$$$$$$   /$$$$$$   /$$$$$$   /$$$$$$  /$$$$$$  
   | $$   | $$__  $$ /$$__  $$ /$$__  $$ |____  $$|_  $$_/  
   | $$   | $$  \ $$| $$  \__/| $$$$$$$$  /$$$$$$$  | $$    
   | $$   | $$  | $$| $$      | $$_____/ /$$__  $$  | $$ /$$
   | $$   | $$  | $$| $$      |  $$$$$$$|  $$$$$$$  |  $$$$/
   |__/   |__/  |__/|__/       \_______/ \_______/   \___/  
"""
    os.system('cls' if os.name == 'nt' else 'clear')
    print(banner)

# Handle end-of-game options
def game_over():
    show_hacker_ascii()
    while True:
        choice = input("Would you like to restart the game? (yes/no): ").strip().lower()
        if choice in ['yes', 'y']:
            return True  # Restart the game
        elif choice in ['no', 'n']:
            print("Thank you for playing! Goodbye!")
            return False  # End the game
        else:
            print("Invalid input. Please type 'yes' or 'no'.")

# Main game logic
def play_game():
    data = load_hacker_data(csv_file)
    show_game_banner()  # Show the banner at the start

    while True:
        score = 0
        lives = 3

        while lives > 0:
            correct, options = generate_question(data)
            correct, options = ask_question(correct, options)

            # Ask the player for their answer
            try:
                answer = int(input("Choose an option (1-4): "))
                if options[answer - 1]['Name'] == correct['Name']:
                    print("Correct! 🎉")
                    score += 1
                else:
                    print(f"Wrong! The correct answer was: {correct['Name']}")
                    lives -= 1
            except (ValueError, IndexError):
                print("Please choose a valid number between 1 and 4.")
                continue

            print(f"Score: {score} | Lives remaining: {lives}")

        # End of the game
        if not game_over():
            break

# Run the game
if __name__ == "__main__":
    play_game()
