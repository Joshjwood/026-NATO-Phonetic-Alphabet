import pandas

#TODO 1. Create a dictionary in this format:
#{"A": "Alfa", "B": "Bravo"}

data = pandas.read_csv("nato_phonetic_alphabet.csv")
alphabet_data = data.to_dict()

alphabet_data_dict = {row.letter:row.code for (index, row) in data.iterrows()}
#print(alphabet_data_dict)

alphabet_frame = pandas.DataFrame(alphabet_data)

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.


on = True
while on == True:
    word_split = [i.upper() for i in (input("Write a word: "))]
    try:
        output_list = [alphabet_data_dict[letter] for letter in word_split]
    except KeyError:
        print("Please input only letters.")

    output = ""
    for i in range(0, len(output_list)):
        output += f"{output_list[i]}, "
    print(f"{output[:-2]}\n")