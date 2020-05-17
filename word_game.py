import pandas as pd
import random


# Functions

# def find_word(file_path):
#     with open(path, 'r') as text_s:
#         text = text_s.read()
#         dictionary = {}
#
#         word = re.compile(r'\d+\.\s([a-zA-Z]+)')
#         meaning = re.compile(r'Meaning: (.*)')
#         mnemonic = re.compile(r'Mnemonics: : ([a-zA-Z_.,+=()<>?/;:&%#\'@!"~`\-\s]+\n?[^\d][a-zA-Z]*?)')
#
#         words = word.findall(text)
#         meanings = meaning.findall(text)
#         mnemonics = mnemonic.findall(text)
#
#         for i, j, k in zip(words, meanings, mnemonics):
#             dictionary[i] = [j, k]
#     return dictionary

def word_game(inputs):
    global dictionary, correct, NA

    if inputs.upper() == 'A':
        numbering = len(dictionary['word'])
        word_in = input("Enter the word: ")
        meaning_in = input("Enter the meaning of the word: ")
        mneumonics_in = input("Enter the Mnemonics(if there is no Mnemonics give the underscore): ")
        dictionary.loc[numbering, :] = [word_in.capitalize(), meaning_in, mneumonics_in]
        dictionary.to_csv('panda_dict.csv', index=False)
        print(f"{word_in} added successfully!!!")
        x = input("If you want to add more words press A and if you want to play Word Game press P: ")
        if x.upper() == 'A':
            return word_game('A')
        elif x.upper() == 'P':
            return word_game('P')
        else:
            print("Invalid Input!!!")
            return inputNrun()

    elif inputs.upper() == 'P':
        for _ in range(20):
            x = random.choice(dictionary['word'].unique())
            ans = input(f"What is the meaning of {x}? ")
            filt = dictionary['word'] == x
            m = 'meaning'
            mne = 'mnemonics'
            vistar = dictionary[filt]
            row = vistar.index[0]
            if ans == '':
                NA += 1
                print(f'Meaning of {x} : {vistar.loc[row, m]} \nMnemonics: {vistar.loc[row, mne]}\n')
            elif ans.lower() in vistar.loc[row, m].lower():
                print("You are right")
                correct += 1
                print(f'Meaning of {x} : {vistar.loc[row, m]} \nMnemonics: {vistar.loc[row, mne]}\n')
            else:
                print("You are wrong")
                print(f'Meaning of {x} : {vistar.loc[row, m]} \nMnemonics: {vistar.loc[row, mne]}\n')

    else:
        print("Invalid Input!!!")
        return inputNrun()


def inputNrun():
    inputs = input('If you want to add a new word press A and if you want to play Word Game press P: ')
    return word_game(inputs)


correct = 0
NA = 0
dictionary = pd.read_csv('panda_dict.csv')
inputNrun()
print(f"Correct Answer: {correct}              Incorrect Answer: {20 - correct - NA}               Not have any Guess: {NA}")
dictionary.to_csv('panda_dict.csv', index= False)
