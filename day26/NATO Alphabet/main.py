import pandas

data = pandas.read_csv(r'nato_phonetic_alphabet.csv')

phonetic_dictionary = {row.letter: row.code for (index, row) in data.iterrows()}

def generate_phoenetic():
    word = input("Enter a word: ").upper()
    try:
        output = [phonetic_dictionary[letter] for letter in word]
    except KeyError:
        print('Sorry only letters in the alphabet please.')
        generate_phoenetic()
    else:
        print(output)

generate_phoenetic()