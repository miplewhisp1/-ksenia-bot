import asyncio
import logging
import sys
import os

# Добавляем корневую папку в путь, чтобы Python видел bot.py
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Импортируем бота
from bot import bot, dp, main

# Это функция, которую Vercel вызовет при старте
async def handler(request):
    # Запускаем Ксюшу
    logging.basicConfig(level=logging.INFO)
    print("❤️ Ксюша запускается на Vercel (через Webhook) ❤️")
    
    # Запускаем polling
    try:
        await dp.start_polling(bot)
    except Exception as e:
        logging.error(f"Бот упал с ошибкой: {e}")
    
    return {"status": "running"}

# Vercel ожидает, что переменная будет называться handler
handler = handler