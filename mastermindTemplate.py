# import the random module

# Declare a list called "colors", Populate it with the characters "R", "G", "B", "Y", "W", "P"
# Declare a variable called "attempts".  Assign 0 to it
# Declare a variable called "continue_game".  Assign the boolean value true to it
# Declare a list called "secret_list".  Use the sample function in the random module to populate the list with 4 unique chars from the colors list


# Create a loop that keeps executing as long as continue_game is true

    # Declare a variable called "clue".  Assign "" to it
    # Print out "The secret to guess is: " and then the guess. Make sure the secret is printed out as a string by using the join function. In a real
    # Mastermind game the secret wouldn't be revealed.  But for teaching and learning and testing and to conform to the grading rubric your game
    # needs to display it.
    # Using the input function, solicit a guess from the user.  Convert the input to upper case.  Store the input in a variable named "guess_input" 
    # Using the list function cast guess_input to a list.  Store the value in a variable called "guess_list"
    # Increment attempts by 1

    # ################## CLUE SECTION  ###############################
    # The following section of code generates the clue for the user. 
    # Asterix symbols (e.g. * ) designate guesses where the color and the position match.
    # Tilde symbols (e.g. "~") designate guesses where the color match but are not in the correct position
    # Pseudocode for generating the asterixes:
    # Create a loop that iterates through the guess_list.  Use x to keep track of the iteration count
        # if guess_list[x] is equal to secret_list[x] then add a "*" to the clue
    # Pseudocode for generating the tildes:
    # Create a loop that iterates through the guess_list. Use x to keep track of the iteration count
        # if guess_list[x] is NOT equal to secret_list[x] (e.g. skip any guesses that were already marked as asterixes)
            # if guess_list[x] is in secret_list then add a "~" to the clue
    # ################# END CLUE SECTION ###############################

    # Print "Your guess is:" and then the guess
    # Pring "Your clues is" and then the clue

    # if the clue is equal to "****":
        # print "Pretty good. I took you [number] attempts to figure out the secret"
        # ask the user if they want to play again
        # if they want to play again:
            # create a new secret
        # else:
            # set continue_game to false


