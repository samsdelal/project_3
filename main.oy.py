import local as lc
import random as r

print(lc.PASS_TXT)
game = int(input('Привет! У тебя на выбор есть мини игра и одна маленька программа , которая определят длинну слова, выбери что хочешь\n'
                 '1.[Камень, ножницы бумага]\n'
                 '2.[Определение длинны слова]\n'
                 '3.[]\n'
                 '4.[]'))
print(r.randint(1, 3))
if game == 1:
    print('Я предлагаю сыграть тебе с компьютером в игру камень ножницы бумага\n'
          '\n'
          'Программа может посчитать сколько раз ты выиграл компьютер а сколько раз проиграл. Удачи!')
    start_game = '1'
    total = 0
    fall = 0
    win = 0
    while start_game == '1':
        print(lc.PASS_TXT)
        step_game1 = int(input('Какой объект ты сейчас выкинешь?\n'
                               '\n'
                               '1.[Камень]\n'
                               '2.[Ножницы]\n'
                               '3.[Бумага]'))
        rand = r.randint(1, 3)

        if rand == 1 and step_game1 == 1:
            print(lc.PASS_TXT)
            print('Ничья, ты выкиунл камень и товой соперник тоже')
            total += 1
            start_game = input('Хочешь еще сыграть \n'
                               '\n'
                               '1.[Да]\n'
                               '2.[Нет]')
        elif rand == 1 and step_game1 == 2:
            print(lc.PASS_TXT)
            print('Ты проиграл, ты выкинул ножницы , а твой соперник камень')
            total += 1
            fall += 1
            start_game = input('Хочешь еще сыграть \n'
                               '\n'
                               '1.[Да]\n'
                               '2.[Нет]')
        elif rand == 1 and step_game1 == 2:
            print(lc.PASS_TXT)
            print('Ты выиграл, ты выкинул бумагу, а твой соперник камень')
            total += 1
            win += 1
            start_game = input('Хочешь еще сыграть \n'
                               '\n'
                               '1.[Да]\n'
                               '2.[Нет]')
        elif rand == 2 and step_game1 ==1:
            print(lc.PASS_TXT)
            print('Ты выиграл, ты выкинул ножницы, а твой соперник камень')
            total += 1
            win += 1
            start_game = input('Хочешь еще сыграть \n'
                               '\n'
                               '1.[Да]\n'
                               '2.[Нет]')
        elif rand == 2 and step_game1 == 2:
            print(lc.PASS_TXT)
            print('Ничья, ты выкиунл ножницы и товой соперник тоже')
            total += 1
            start_game = input('Хочешь еще сыграть \n'
                               '\n'
                               '1.[Да]\n'
                               '2.[Нет]')
        elif rand == 2 and step_game1 == 3:
            print(lc.PASS_TXT)
            print('Ты проиграл, ты выкинул бумагу , а твой соперник ножницы')
            total += 1
            fall += 1
            start_game = input('Хочешь еще сыграть \n'
                               '\n'
                               '1.[Да]\n'
                               '2.[Нет]')
        elif rand == 3 and step_game1 == 1 :
            print(lc.PASS_TXT)
            print('Ты проиграл, ты выкинул камень , а твой соперник бумагу')
            total += 1
            fall += 1
            start_game = input('Хочешь еще сыграть \n'
                               '\n'
                               '1.[Да]\n'
                               '2.[Нет]')
        elif rand == 3 and step_game1 == 2 :
            print(lc.PASS_TXT)
            print('Ты выиграл, ты выкинул ножницы, а твой соперник бумагу')
            total += 1
            win += 1
            start_game = input('Хочешь еще сыграть \n'
                               '\n'
                               '1.[Да]\n'
                               '2.[Нет]')
        elif rand == 3 and step_game1 == 3:
            print(lc.PASS_TXT)
            print('Ничья, ты выкиунл бумагу и товой соперник тоже')
            total += 1
            start_game = input('Хочешь еще сыграть \n'
                               '\n'
                               '1.[Да]\n'
                               '2.[Нет]')
    else:
        print(lc.PASS_TXT)
        print('Спасибо что поиграл в эту чудесную игру)')
        print(lc.PASS_TXT)
        print('Всего сыграно игры - ', total)
        print(lc.PASS_TXT)
        print('Проиграно игр - ', fall)
        print(lc.PASS_TXT)
        print('Выиграно игры - ', win)
elif game == 2:
    print(lc.PASS_TXT)
    total_word = 0
    again = 1
    while again == 1:
        print(lc.PASS_TXT)
        word = input('Введи слово')
        lenght = len(str(word))
        print(lc.PASS_TXT)
        print(lenght)
        total_word += 1
        again = int(input('Хочешь еще проверить слово \n'
                          '\n'
                          '1.[Да]\n'
                          '2.[Нет]'))
    else:
        print(lc.PASS_TXT)
        print('Спасибо что использовал эту программу, всего слов было подсчитанно - ', total_word)







