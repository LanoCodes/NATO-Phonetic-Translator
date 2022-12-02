import pandas as pd

nato_phon_alph_DataFrame = pd.read_csv("nato_phonetic_alphabet.csv")
nato_phon_alph_dict = {row.letter:row.code for (index, row) in nato_phon_alph_DataFrame.iterrows()}

user_word = input("Enter word for phonetic translation: ").upper()
phonetic_translation = [nato_phon_alph_dict[letter] for letter in user_word]
for letter in phonetic_translation:
    print(letter)