pokemon_binder = []   #list of all pokemon cards

def input_int(prompt, min_value = None, max_value = None): #prompt for an integer input with optional min and max values
    while True:   #loop until valid input is received
        try:

            value = int(input(prompt))   #get input and convert to integer
            if (min_value is not None and value < min_value) or (max_value is not None and value > max_value): #check if within range
                raise ValueError("Value out of range")   #raise error if not in range
            return value   #return valid input  
                  
        except ValueError:
            print("Invalid input. Please enter a valid integer.")   #error message for invalid input

def pokemon_card_binder():   #function to create a pokemon card binder
    print("Welcome to the Pokemon Card Binder!")
    print("\n Pokemon Card Binder")   #title of the program

    while True:
        print("\n1. Add a Pokemon Card")   #menu options
        print("2. Reset the Binder")   #reset the binder
        print("3. View the Binder")   #view the binder
        print("4. Exit")
        player = input_int("Select an option (1-4): ", 1, 4)    

        if player == 1:
            card = input("Enter the name of the Pokemon card: ")
            if card in pokemon_binder:
                print("This card is already in the binder.")   #check if card already exists
            else:
                pokemon_binder.append(card)
                print(f"{card} has been added to the binder.")   #add card to the binder
        elif player == 2:
            pokemon_binder.clear()
            print("The binder has been reset.")   #reset the binder
        elif player == 3:
            if not pokemon_binder:
                print("The binder is empty.")
            else:
                print("Pokemon Card Binder:")
                for i, card in enumerate(pokemon_binder, start=1):
                    print(f"{i}. {card}")   #view the binder
        elif player == 4:
            print("Thank you for using the Pokemon Card Binder!")
            break
        else:
            print("Invalid option. Please try again.")  #error message for invalid option

if __name__ == "__main__":
    pokemon_card_binder()   #call the function to run the program
    
    