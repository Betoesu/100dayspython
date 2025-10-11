import pandas

natoData = pandas.read_csv("./Projetos/26_NATO_Alphabet/nato_phonetic_alphabet.csv")

#Aqui eu pego a linha das letras e do codigo do documento
natoAlphabetDict = {row.letter:row.code for (index,row) in natoData.iterrows()}
print(natoAlphabetDict)

def generate_phonetic():
    word = input("Enter a word: ").replace(" ","").upper()
    try:
        #pego a letra e procuro no dicionario
        wordNato = [natoAlphabetDict[letter] for(letter) in word]
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
        generate_phonetic()
    else:
        print(wordNato)

generate_phonetic()