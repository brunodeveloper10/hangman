import random

word_list = ['banana', 'brasil', 'amor', 'conhecimento', 'abacate', 'abelha']


chosen_word = random.choice(word_list)


chosen_letter = str(input('Digite uma letra: ')).lower()

display = ['-' for _ in range(len(chosen_word))]

print(f'A palavra escolhida é: {chosen_word}')
for index, letter in enumerate(chosen_word):
    if letter == chosen_letter:
        display[index] = letter
        print('RIGHT')
    else:
        print('WRONG')

print(f'forca: {display}')