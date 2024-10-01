"""

Домашнее задание №1

Условный оператор: Возраст

* Попросить пользователя ввести возраст при помощи input и положить
  результат в переменную
* Написать функцию, которая по возрасту определит, чем должен заниматься пользователь:
  учиться в детском саду, школе, ВУЗе или работать
* Вызвать функцию, передав ей возраст пользователя и положить результат
  работы функции в переменную
* Вывести содержимое переменной на экран

"""

def main(age):
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    if age < 6:
        result = "Вы должны учиться в детском саду"
    elif age < 19:
        result = "Вы должны учиться в школе"
    if age < 25:
        result = "Вы должны учиться в ВУЗе"
    else:
        result = "Вы должны работать"
    return result

if __name__ == "__main__":
    age = int(input("Введите возраст. "))
    status = main(age)
    print(status)
