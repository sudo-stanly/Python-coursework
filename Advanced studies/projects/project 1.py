import re

"""

    * Project: "Smart Text Analyzer" Goal:
    * Build a Python program that takes user input (like a paragraph of text) 
    * and gives back insights using functions, regex, and loops.


    !Instructions

        * Input Handling

        * Ask the user to enter a block of text (multi-line if possible).

        * Menu System (Loop Required)

        * Create a menu that repeats until the user chooses to quit.

        * Example options quit or write email address:

        * Count the number of words.

        * Count the number of sentences.

        * Find all the email addresses inside the text (regex).

        * Find all the numbers inside the text (regex).

        * Replace all occurrences of a chosen word with another (string manipulation).

        * Check if a word is a palindrome (use a function).

        * Quit.

        * Functions

        * Each menu option should be handled by its own function.

        * Example: count_words(text) should return the number of words.

        * Regex Challenge

        * Use regex for email and number detection.

        * Optional: also detect dates (like DD/MM/YYYY or YYYY-MM-DD).

        * Loops

        * Use a while loop to keep showing the menu until the user quits.

        * Use a for loop inside at least one function (e.g., iterating over words to count vowels).

        * Operators & Strings

        * Use comparison operators (==, !=) for word checking (e.g., palindrome test).

        * Use arithmetic operators for counts.

        * Use string slicing for palindrome checking.
        
        
        ! Optional Bonus Features

            * Track how many times each menu option was used before quitting.

            * Store all results in a dictionary and print a summary report when the program ends.

            * Add regex to extract hashtags (#example) or mentions (@user).
"""

#! 1.) ask for user input.
#! 2.) looped system menu

#! added try and catch for invalid input
#! 3.) checking number of sentences.
#! 4.) creating a function for number of words and sentences.
#! 5.) counting the times an option was used before quiting.
#! 6.) Check if Palindrome

def count_words(text):
    #pass
    # print(f"TEXT: {text}")
    print(f"Number of words: {len(text)}")
    
    #! check if palindrome.      
    #print(f"CURRENT: {str(text[0]).replace(',', '')}") #* convert to string?

    #* replace all unecessary characters for a palindrome.
    
    convert_text_to_string = str(text[0])
    if ',' in convert_text_to_string:
        convert_text_to_string.replace(',', '')
        
    print(f"text after {convert_text_to_string}")

def count_sentences(text):
    #pass
    sample_split_sentence = text.split(".")
    sample_count = len(sample_split_sentence) - 1 
    print(f"Number of sentence(s): {sample_count}")
    print()

option_counter = 0
while True:
    try:
        option = int(input("[1] Write, [2] Quit: "))
        
        if option == 1: #! Write condition
            print()
                        
            #* testing..
            #sample_text = "Python is awsome, and very hard. Programming is cool."
            #sample_text = 'Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula eget dolor. Aenean massa. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur.'
                #* -> sample_text = 'Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula eget dolor. Aenean massa. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur'
                #* -> sample_split_sentence = sample_text.split(".")
                #* -> sample_count = len(sample_split_sentence) - 1 #* since i'm using length, i will reduce by 1 to not include the empty element.
                #* -> print(f"Sentence(s): {sample_split_sentence}\nTotal of sentence(s): {sample_count}")
            
            #! now how to avoid a paragraph with no period in end of string.
            #* -> endswith()
                #* -> if sample_text.endswith('.'):
                #* ->     print("Sentence ends with \".\"")
                #* -> else:
                #* ->     print("Please end your sentence with a \".\"")
                
            #! inserting user input to functions for counting number of words and sentences.
            #! counting the times an option was also used.
            #* take text and validate text first if ends with a period.
            
            option_counter += 1
            user_text = input("Enter a text: ")
            
            if user_text.endswith("."):
                #print()
                
                #* format text for count_word function.
                # formatted_text = user_text.replace(",", " ")
                # formatted_text = user_text.replace("!", " ")                 
                formatted_text = user_text.split()
                count_words(formatted_text)
                count_sentences(user_text)
                
                #! after counting words and sentences, proceed to find email addresses and for numbers use regex.
                
            else:
                print("Please end your sentence with a period.")
                
        elif option == 2: #! Quit condition
            
            number_of_times_option_was_used = option_counter
            print(f" Option {option - 1} has been used '{number_of_times_option_was_used}' times.")
            #                  sneaky
            break
    except:
        print(" Invalid input.")