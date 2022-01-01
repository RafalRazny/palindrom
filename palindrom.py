list_of_letters = []
revers_list_of_letters = []
def palindrom(word):
    for i in word:
        list_of_letters.append(i)
    revers_list_of_letters = list (reversed(list_of_letters))
    if revers_list_of_letters == list_of_letters:
        print("Tak, ten wyraz to jest palindrom!")
    else:
        print("Nie, ten wyraz to nie jest palindrom.")

palindrom('kajak')