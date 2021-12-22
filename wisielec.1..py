import sys

no_of_tries = 5
word = "kamila"
used_letters =[]

user_word = []

def find_indexes(word, letter):
    indexes=[]
    #k a m i l a
    #0 1 2 3 4 5
    for index, letter_in_word in enumerate(word):
        if letter == letter_in_word:
            indexes.append(index)
   

    return indexes 

def show_state_of_game():
    print()
    print(user_word)
    print("POZOSTAŁE próby")
    print("użyte litery"),used_letters

###
for letter in word :
    user_word.append("_")

while True:
    letter= input("podaj literę: ")
    used_letters.append(letter)

    found_indexes= find_indexes(word, letter)
    if len(found_indexes)==0:
        print("Nie ma takiej litery. ")
        no_of_tries -= 1
    

        if no_of_tries == 0:
            print("Koniec gry :(")
            sys.exit(0)
    else:
        for index in found_indexes:
            user_word[index]=letter
         

         #[k,a,m,i,l,a] -> kamila
        if "".join(user_word) == word:
            print("Brawo! Odgadłeś słowo!")
            sys.exit(0)

    show_state_of_game()
