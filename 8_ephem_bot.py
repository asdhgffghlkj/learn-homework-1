"""
Домашнее задание №1

Использование библиотек: ephem

* Установите модуль ephem
* Добавьте в бота команду /planet, которая будет принимать на вход
  название планеты на английском, например /planet Mars
* В функции-обработчике команды из update.message.text получите
  название планеты (подсказка: используйте .split())
* При помощи условного оператора if и ephem.constellation научите
  бота отвечать, в каком созвездии сегодня находится планета.

"""
import logging
from datetime import datetime as dt
# Не написав as dt, появляется конфликт с библиотекой телеграм бота, у которой тоже есть datetime

import ephem
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log')


def greet_user(update, context):
    text = 'Вызван /start'
    print(text)
    update.message.reply_text(text)


def talk_to_me(update, context):
    user_text = update.message.text
    print(user_text)
    update.message.reply_text(user_text)


def main():
    mybot = Updater("6390003041:AAHNllrZHSXCVusVRdjpsvpevFYylBUstb0", use_context=True)

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler("planet", planet_command))
    # dp.add_handler(MessageHandler(Filters.text, talk_to_me))

    mybot.start_polling()
    mybot.idle()


def planet_command(update, context):
    planet_name = context.args[0].capitalize()
    current_time = dt.now()
    planet = getattr(ephem, planet_name)(current_time)  # Получаем объект планеты
    constellation = ephem.constellation(planet)
    update.message.reply_text(f"Сегодня планета {planet_name} находится в созвездии {constellation[1]}.")



if __name__ == "__main__":
    main()
