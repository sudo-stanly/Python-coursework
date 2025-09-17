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

def count_words(text):

    #! count words
    format_text = str(text).split()
    print(f"Number of words: {len(format_text)}")
    
    
    #! check palindrome.  
    replace_text = re.sub(r"[,!.]", "", text)    
    print(f"REPLACED TEXT: {replace_text}")
    
    #* then loop
    split_replaced_text = str(replace_text).lower().split()
    for word in split_replaced_text:
        #! important! print("ELEMENT: ", word)
        
        #* split each element?
        element_to_list = list(word)
        #! important! print(f"ELEMENT THAT SPLIT: {element_to_list}")

        #* then get index and length of the list andcheck for palindrome
        # index_of_word = 0
        # last_index_of_word = len(element_to_list) - 1
        #! important! print(f"\nFirst letter of {word}\t: {element_to_list[index_of_word]}\nLast letter of {word}\t:{element_to_list[last_index_of_word]}")
        
        #isPalindrome = index_of_word == last_index_of_word
        isPalindrome = word == word[::-1]
        if isPalindrome:
            print(f"\"{word}\" is a Palindrome!")
        else:
            print(f"\"{word}\" is not a Palindrome!")

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

            option_counter += 1
            user_text = input("Enter a text: ")
            
            if user_text.endswith("."):                   
                count_words(user_text)
                count_sentences(user_text)
                
            else:
                print("Please end your sentence with a period.")
                
        elif option == 2: #! Quit condition
            number_of_times_option_was_used = option_counter
            print(f" Option {option - 1} has been used '{number_of_times_option_was_used}' times.")
            break
        
    except:
        print(" Invalid input.")