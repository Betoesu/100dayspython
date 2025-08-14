import pandas
natoData = pandas.read_csv("./Projetos/26_NATO_Alphabet/nato_phonetic_alphabet.csv")

#Aqui eu pego a linha das letras e do codigo do documento
natoAlphabet = {row.letter:row.code for (index,row) in natoData.iterrows()}
print(natoAlphabet)

word = input("Enter a word: ").replace(" ","").upper()
wordList = list(word)
#pego a letra e procuro no dicionario
wordNato = [natoAlphabet[letter] for(letter) in wordList]
print(wordNato)
 