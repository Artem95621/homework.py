first = 'Мама мыла раму'
second = 'Рамена мало было'

fun_lam = list(map(lambda x, y: x == y, first, second))
print(fun_lam)

def get_advanced_writer(file_name):
    def write_everething(*data_set):
        with open(file_name, 'a', encoding='utf-8') as file:
            for data in data_set:
                file.write(f'{data}\n')
    return write_everething
write = get_advanced_writer('example.txt')
write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])

from random import choice
class MysticBall:
    def __init__(self, *word):
        self.word = word

    def __call__(self):
        return choice(self.word)
first_ball = MysticBall('Да', 'Нет', 'Наверное')

print(first_ball())
print(first_ball())
print(first_ball())