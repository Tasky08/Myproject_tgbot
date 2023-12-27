import asyncio
from handlers import router
from aiogram import Bot, Dispatcher

# Объект бота
bot = Bot(token="6353580222:AAEwKxAQCwsajFFltpsMv_h-Gi_5DLUBm5w")

# Запуск процесса поллинга новых апдейтов
async def main():
    """
           Асинхронная функция для запуска процесса поллинга новых обновлений бота.

           Создает объект Dispatcher, включает в него роутер и запускает процесс поллинга на основе данного диспетчера и
           объекта бота.

           Raises:
               Any: Возможные исключения, связанные с работой aiogram и запуском процесса поллинга.

           Example:
               Пример использования:

               ```python
               if __name__ == "__main__":
                   asyncio.run(main())
               ```
           """
    dp = Dispatcher()
    dp.include_router(router)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Exit')