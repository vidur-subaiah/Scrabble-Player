from scrabble_logic import InputValidator, WordGenerator, WordValidator, Word


def main():
    letter_tiles = input("Enter the letters in your rack: ")
    letter_tiles = letter_tiles.strip()
    valid_input = InputValidator(letter_tiles)
    check = valid_input.validate_input()
    if check != True:
        return print(check + " is not a valid letter. Please try again.")
    input_pattern = valid_input.type_of_input()
    if input_pattern == False:
        return print("Matching pattern could not be found.")
    if input_pattern == 1: 
        letter_tiles = letter_tiles
    if input_pattern == 2:
        letter_tiles = letter_tiles.replace(" ", "") # removes all spaces
    if input_pattern == 3:
        letter_tiles = letter_tiles.replace(",", "") # removes all commas
    characters = WordGenerator(letter_tiles)
    possible_words = characters.word_possibilities()
    valid_possible_words = WordValidator(possible_words).valid_words()
    if not valid_possible_words:
        return print("No valid scrabble words.") # the letters in the tile rack cannot create any valid words
    initial_dict = {}
    for item in valid_possible_words:
        word = Word(item)
        initial_dict[word.string] = word.score # creates a dictionary with the valid words and their points
    for i in range(2, len(letter_tiles)+1): # loops through all word length sizes and prints the top 15 if present
        dictionary_word_length = {}
        for k in initial_dict.keys():
            if len(k) == i:
                dictionary_word_length[k] = initial_dict[k]
        sorted_by_score = sorted(dictionary_word_length.items(), key = lambda kv: kv[1], reverse = True) # scores in descending order
        sorted_dictionary = dict(sorted_by_score)
        sorted_dictionary_items = sorted_dictionary.items()
        top_fifteen_word_list = list(sorted_dictionary_items)[:15] # creates a list of the top 15 scoring words for that particular word length
        print(str(i) + " Letter Words")
        print("-------------------------")
        if not top_fifteen_word_list:
            print("No Words")
        else:
            for item in top_fifteen_word_list:
                print(item[0] + " " + "-" + " " + str(item[1]) + " points") # prints to the console
        print("\n")
    return None

if __name__ == "__main__":
    main()
