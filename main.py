import pandas as pd

nato_phon_alph_DataFrame = pd.read_csv("nato_phonetic_alphabet.csv")
nato_phon_alph_dict = {row.letter:row.code for (index, row) in nato_phon_alph_DataFrame.iterrows()}


def translate():
    user_word = input("Enter word for phonetic translation: ").upper()
    try:
        phonetic_translation = [nato_phon_alph_dict[letter] for letter in user_word]
    except KeyError:
        print("Only enter letters in the alphabet please.")
        translate()
    else:
        for letter in phonetic_translation:
            print(letter)

translate()
