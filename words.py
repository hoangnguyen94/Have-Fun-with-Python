def print_upper_words(words):
    """ Print each letter to uppercased"""

    for word in words:
        print(word.upper())


print_upper_words(["hello", "hey", "good bye", "yo", "yes"])

def print_upper_words2(words):
    """ Print each letter with letter e to uppercased"""
    
    for word in words:
        if word.startswith("e") or word.startswith("E"):
            print(word.upper())

            
print_upper_words2(["element", "hey", "good bye", "yo", "yes"])

def print_upper_words3(words, must_start_with):
    """Print words with a must_start_with to uppercased"""
    for word in words:
        for letter in must_start_with :
            if word.startswith(letter):
                print(word.upper())

print_upper_words3(["hello", "hey", "good bye", "yo", "yes"], {"h", "y"})
