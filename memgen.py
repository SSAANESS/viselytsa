# deals = [
#     'погулять с друзьями',
#     'почитать новости и сцепиться с кем-нибудь в комментах',
#     'почитать книжку',
#     'рассмотреть потолок',
#     'поиграть в Brawl stars',
#     'помыть посуду',
#     'сказать родителям, что заболел',
#     'залипнуть в летсплеях по роблоксу',
# ]
#
#
#
# while True:
#     userinput =int(input ('Какой элемент удалить?: '))
#     if userinput== '':
#         break
#     else:
#         del deals['']
#
# print(deals)
# deals = [
#     'погулять с друзьями',
#     'почитать новости и сцепиться с кем-нибудь в комментах',
#     'почитать книжку',
#     'рассмотреть потолок',
#     'поиграть в Brawl stars',
#     'помыть посуду',
#     'сказать родителям, что заболел',
#     'залипнуть в летсплеях по роблоксу',
#     'покормить кота'
# ]
# for deal in deals:
#     print(f'Не делать уроки, а {deal}')


import random

print('Привет. Некогда объяснять, иди угадывай слово.')
input('*нажми enter*')

print('Поехали')
words = ['сумка','игра','выскочка','аппендектомия','пастушка','трубочист','водолей','близняшка']

word = random.choice(words)
letters = []
isWin= True
hp = 10

while hp > 0:
    isWin = True
    letter = input('Введите букву:')
    letters.append(letter)

    for symb in word:
      if symb in letters:
       print(symb,end=' ')
      else:
       print('*', end=' ')
       isWin=False
    print()

    if isWin:
       print('Ты угадал!')
       break

    letter = input('Введите букву:')
    letters.append(letter)


    if letter not in word :
        hp-= 1
    print(f'Осталось попыток: {hp}')

    if hp == 0:
        print('Проиграл!')
