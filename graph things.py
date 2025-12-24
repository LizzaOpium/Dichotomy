import numpy as np
from matplotlib import pyplot as plt

'''
Словарь для большего удобства
'''

def f(x):
    try:
        dict = {
            'x': x,
            'sin': np.sin,
            'cos': np.cos,
            'tan': np.tan,
            'exp': np.exp,
            'log': np.log,
            'sqrt': np.sqrt,
            'abs': np.abs,
            'pi': np.pi,
            'e': np.e,
            'X': x
        }
        return eval(func, dict)
    except:
        return np.nan


'''
Дихтомия, принимает на вход функцию и a, b
a, b - границы отрезка
'''

def dichotomy(a, b):
    eps = 1e-6 # эпсилон - он же шаг
    r = eps/2 # отступы от середины отрезка
    global c # ввел глобальную переменную, чтобы потом ее использовать

    if np.isnan(f(a)) or np.isnan(f(b)):
        c = None
        return f'Ошибка: функция не определена на отрезке ({a}; {b})'

    while abs(b - a) > eps: # оценка отрезков, пока их длина не станет меньше шага
        c = (a + b) / 2

        # сравним значения функций по разные концы отрезка:

        if f(c - r) > f(c + r):
            b = c
        else:
            a = c
    # вывод данных
    if np.isnan(f(c)):
        c = None
        return f'Ошибка: функция не определена на отрезке ({a}; {b})'

    print('> Найден максимум функции: ')
    # округление сделано до 4 цифр после запятой для большего удобства
    return f'f(x_max) = {round(f(c), 4)}, x_max = {round(c, 4)}'

'''
Основная функция для работы программы,
какую мы и будем анализировать
'''

func = input('> Введите функцию f(x) = ')
a = float(input('   Введите начало отрезка: '))
b = float(input('   Введите конец отрезка: '))

print(dichotomy(a, b))

'''
Отображение графика на оси:

    * красным - основной график;
    * синим - полученный максимум на отрезке путем дихтомии;
    
Расстояние между действительным максимумом красного
и пересечением синих пунктиров - есть погрешность
'''

if c == None:
    print(f'> График не был построен')
else:
    x = np.linspace(a, b, 1000)
    y = f(x)

    plt.axhline(y=f(c), color='blue', linestyle='--')
    plt.axvline(x=c, color='blue', linestyle='--')
    plt.plot(x, y, label='f(x)', color = 'red', linestyle = 'solid')
    plt.title('График f(x)')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.grid(True)
    plt.show()
