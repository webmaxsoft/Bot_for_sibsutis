import asyncio
from datetime import datetime
from aiogram import Bot, Dispatcher, types

bot = Bot(token='6939011712:AAGMkDfNeZxdTcMO5jlVwUzt6jgpffhewKQ')
dp = Dispatcher(bot)

# Функция для отправки напоминания в чат каждую субботу в 21:00
async def send_reminder():
    while True:
        now = datetime.now()
        if now.weekday() == 5 and now.hour == 21 and now.minute == 15:
            # ID чата, куда вы хотите отправлять сообщения
            chat_id = YOUR_CHAT_ID_HERE

            # Отправляем сообщение в чат
            await bot.send_message(chat_id, "Отмечаемся!")

            # Подождем до следующей субботы
            await asyncio.sleep(7 * 24 * 60 * 60)  # 7 дней в секундах
        else:
            # Подождем 5 минут и проверим снова
            await asyncio.sleep(1 * 1200)


# Обработчик команды /start
async def start_handler(message: types.Message):
    await message.reply("Привет! Я бот-напоминалка.")

# Регистрация обработчика команды /start
@dp.message_handler(commands=['start'])
async def register_start(message: types.Message):
    await start_handler(message)

# Функция для запуска бота
async def main():
    # Запускаем задачу отправки напоминаний
    await send_reminder()


if __name__ == '__main__':
    asyncio.run(main())
