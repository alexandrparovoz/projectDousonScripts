# прога АНАГРАММА - тасуем буквы в слове
if __name__ == '__main__':
    import random

    words = ('umbrella', 'yellow', 'mushrooms', 'python', 'octopus')
    word = random.choice(words)
    correct = word  # создаем переменную, с которой сравним версию игрока
    jumble = ''
    while word: # пока в слове есть буквы это  TRUE
        position = random.randrange(len(word))
        jumble += word[position]  # пополняем буквами из WORD
        word = word[:position] + word[(position + 1):]  # вынимаем букву из WORD, меняя значение переменной WORD

    # начало игры
    print(
    '''
            Привет! Это игра Анаграмма!
            Надо переставит буквы так, чтобы получилось слово со смыслом.
            (Для выхода нажмите Enter)
    '''
    )
    print('Вот анаграмма - ', jumble)
    guess = input('\nПробуйте отгадать слово: ')
    while guess != correct and guess != '':
        print('Вы не правы!')
        guess = input('\nПробуйте отгадать слово: ')

    if guess == correct:
        print('Ура! Вы отгадали.')
    print('Спасибо!')
    input('\nНажмите Enter чтобы выйтию')
