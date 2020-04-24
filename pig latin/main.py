# Pig Latin Translator
# By Ethan J
# April 24, 2020


vowels = 'aeiouyAEIOUY'



def rule1(word):
    return word[1:] + "-" + word[0] + "ay"

def rule2(word):
    return word[2:] + "-" + "quay"

def rule3(word):
    return word[2:] + "-" + word[:2] + "ay"

def rule4(word):
    return word + "-yay"

def rule1_reverse(last, first):
    return last[0] + first
def rule2_reverse(last, first):
    return "qu" + first
def rule3_reverse(last, first):
    return last[:2] + first
def rule4_reverse(last, first):
    return first

def to_pig_latin(words):
    translation = []

    for word in words:

        if word[0] not in vowels and word[0] != "q" and word[1:2] in vowels:
            new_word = rule1(word)
        elif word[:2] == "qu":
            new_word = rule2(word)
        elif word[0] not in vowels and word[1:2] not in vowels:
            new_word = rule3(word)
        elif word[0] in vowels:
            new_word = rule4(word)

        translation.append(new_word)

    return " ".join(translation)

def to_english(words):

    translation = []

    for word in words:
        first,last = word.split("-")

        if last[0] not in vowels and last[0] != "q" and last[1] in vowels:
            new_word = rule1_reverse(last, first)

        elif last == "quay":
            new_word = rule2_reverse(last, first)

        elif last[0] not in vowels and last[1] not in vowels:
            new_word = rule3_reverse(last, first)

        elif last == "yay" and first[0] in vowels:
            new_word = rule4_reverse(last, first)

        translation.append(new_word)
    
    return " ".join(translation)

selection = 0


while selection != 4:
    message = input("Enter a word: ")
    print(""" 
    1 - convert to pig latin
    2 - convert to english
    3 - auto
    4 - quit
    """)
    selection = int(input("Enter a number: "))

    words = message.split()

    if selection == 1:
        print(to_pig_latin(words))
    elif selection == 2:
        print(to_english(words))
    elif selection == 3:
        language = "pig_latin"
        for word in words:
            if "-" not in word and word[-2:] != "ay":
                language = "english"
        if language == "english":
            print(to_pig_latin(words))
        else:
            print(to_english(words))
               
            
    elif selection == 4:
        print("Have a great day")