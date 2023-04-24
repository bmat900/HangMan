import random
import draw
cont = 0
word_list = ['banana', 'tomate', 'cebola', 'cachorro', 'banheiro', 'computador', 'livro', 'carro', 'morango']
chosen_word = ""
draw_word_list = []
draw_word = ""
guess = ""

def check_letters(check, word):
    for i in range(0, len(word)):
        if word[i] == check:
            return True

chosen_word = random.choice(word_list)
chosen_word_list = list(chosen_word)

def display(a):
    word = "".join(a)
    return word

def final(word1,word2):
    if word1 == word2:
        print(f"Você conseguiu!! encontrou a palavra <{display(word1)}>!!")
    else:
        print('''
             +---+
             |   |
             O   |
            /|\  |
            / \  |    
                 |
            =========''')
        print(f"Você não conseguiu, a palavra era <{display(word1)}>. =(")

for i in chosen_word:
    draw_word_list.append("_")

print("Benvindo ao Jogo Hangman!")

while cont <= 5:
    draw.draw(cont)
    print(display(draw_word_list))
    guess = input('Ingresse uma letra. ').lower()
    for i in range(0, len(chosen_word_list)):
        if chosen_word_list[i] == guess:
            draw_word_list[i] = guess
    if not check_letters(guess, chosen_word_list):
        cont += 1
        if cont > 0:
            print(f'Você tem {6 - cont} tentativas. ')
    if chosen_word_list == draw_word_list:
        cont +=7
final(chosen_word_list,draw_word_list)
