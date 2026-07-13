import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage

from config import Config

from handlers.handler import router
from handlers.random_charachter import router as random_character
from handlers.search_by_name import router as search_by_name



async def main():
    config = Config()
    bot = Bot(config.TOKEN)
    dp = Dispatcher(storage=MemoryStorage())

    dp.include_router(router)
    dp.include_router(random_character)
    dp.include_router(search_by_name)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())