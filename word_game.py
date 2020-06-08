import pandas as pd
import random
import time


# Global variables
dictionary = pd.read_csv('panda_dict.csv')
correct = 0
NA = 0
incorrect = 0
random_word = ""
question = ""


# Functions
def add_words():
    global dictionary
    
    numbering = len(dictionary['word'])
    word_in = input("Enter the word: ")
    meaning_in = input("Enter the meaning of the word: ")
    mneumonics_in = input("Enter the Mnemonics(if there is no Mnemonics give the underscore): ")
    dictionary.loc[numbering, :] = [word_in.capitalize(), meaning_in, mneumonics_in]
    dictionary.to_csv('panda_dict.csv', index=False)


def answer(ans):
    global dictionary, correct, NA, random_word, incorrect
    
    filt = dictionary['word'] == random_word
    m = 'meaning'
    mne = 'mnemonics'
    vistar = dictionary[filt]
    row = vistar.index[0]
    if ans == '':
        status = "Not Answered"
        NA += 1
        correct_ans = f'Meaning of {random_word} : {vistar.loc[row, m]} \nMnemonics: {vistar.loc[row, mne]}\n'
        return status, correct_ans
    elif ans.lower() in vistar.loc[row, m].lower():
        status = "You are right"
        correct += 1
        correct_ans = f'Meaning of {random_word} : {vistar.loc[row, m]} \nMnemonics: {vistar.loc[row, mne]}\n'
        return status, correct_ans
    else:
        status = "You are wrong"
        incorrect += 1
        correct_ans = f'Meaning of {random_word} : {vistar.loc[row, m]} \nMnemonics: {vistar.loc[row, mne]}\n'
        return status, correct_ans


def play():
    global dictionary, random_word, question
    
    random_word = random.choice(dictionary['word'].unique())
    question = f"What is the meaning of {random_word}?"
    return question
        

def word_game(inputs):
    global dictionary, correct, NA

    if inputs.upper() == 'A':
        add_words()
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
            play()

    else:
        print("Invalid Input!!!")
        return inputNrun()


def inputNrun():
    inputs = input('If you want to add a new word press A and if you want to play Word Game press P: ')
    return word_game(inputs)


if __name__ == "__main__":
    inputNrun()
    print(f"Correct Answer: {correct}              Incorrect Answer: {20 - correct - NA}               Not have any Guess: {NA}")
    time.sleep(3)
