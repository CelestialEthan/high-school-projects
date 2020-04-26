# Pig Latin Translator
# By Ethan J
# April 24, 2020

import tkinter as tk 
import tkinter.font as tkFont

vowels = 'aeiouyAEIOUY'

def rule1(word):
    """ First letter of word is consonant and second is vowel """
    return word[1:] + "-" + word[0] + "ay"

def rule2(word):
    """  First letter is 'q' and second is 'u'  """
    return word[2:] + "-quay"

def rule3(word):
    """ First letter of word is consonant and second is constant """
    return word[2:] + "-" + word[:2] + "ay"

def rule4(word):
    """ First letter of the word is a vowel """
    return word + "-yay"

def rule1_reverse(last, first):
    """ first letter of last is a consonant and first letter of last is not a 'q' and second letter is a vowel """
    return last[0] + first
def rule2_reverse(last, first):
    """ first letter of last is 'q' and second letter of last is 'u' """
    return "qu" + first
def rule3_reverse(last, first):
    """ first letter of last is a consonant and second letter of last is a consonant """
    return last[:2] + first
def rule4_reverse(last, first):
    """ last === 'yay' """
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

def translate():
    ent_result.delete(0, "end")
    sentence = ent_input.get()
    words = sentence.split()
    
    if selection.get() == 1:
        translation = to_pig_latin(words)
    elif selection.get() == 2:
        translation = to_english(words)
    elif selection.get() == 3:
        language = "pig_latin"
        for word in words:
            if "-" not in word and word[-2:] != "ay":
                language = "english"
        if language == "english":
            translation = to_pig_latin(words)
        else:
            translation = to_english(words)
    ent_result.insert(0, "".join(translation))

def clear():
    ent_input.delete(0, "end")
    ent_result.delete(0, "end")

def end_program():
    window.destroy()



window = tk.Tk()
window.title("Pig Latin Translator")

window.resizable(False,False)
font_size = tkFont.Font(size = 12)

frm_input = tk.Frame()
lbl_input = tk.Label(master = frm_input, font = font_size, text = "Enter a message")

ent_input = tk.Entry(master = frm_input, font = font_size, width = 60)

lbl_input.pack(pady = 10)
ent_input.pack(padx = 10, pady = 5)
frm_input.pack()

frm_control = tk.Frame()
selection = tk.IntVar()
tk.Radiobutton(master = frm_control, font = font_size, text = "To Pig Latin", variable = selection, value = 1).grid(row = 0, column = 0 )
tk.Radiobutton(master = frm_control, font = font_size, text = "To English", variable = selection, value = 2).grid(row = 0, column = 1 )
tk.Radiobutton(master = frm_control, font = font_size, text = "Automatic", variable = selection, value = 3).grid(row = 0, column = 2 )

btn_translate = tk.Button(master = frm_control, font = font_size, text = "Translate", width = 10, height = 2, command = translate)
btn_clear = tk.Button(master = frm_control, font = font_size, text = "Clear", width = 10, height = 2, command = clear)
btn_quit = tk.Button(master = frm_control, font = font_size, text = "Quit", width = 10, height = 2, command = end_program)

btn_translate.grid(row = 1, column = 0, pady = 5, padx = 5)
btn_clear.grid(row = 1, column = 1, pady = 5, padx = 5)
btn_quit.grid(row = 1, column = 2, pady = 5, padx = 5)
frm_control.pack()

frm_output = tk.Frame()
lbl_answer = tk.Label(master = frm_output, font = font_size, text = "Translation")
ent_result = tk.Entry(master = frm_output, font = font_size, width = 60)

frm_output.pack()
lbl_answer.pack(pady = 10)
ent_result.pack(pady = 10, padx = 10)

window.mainloop()

