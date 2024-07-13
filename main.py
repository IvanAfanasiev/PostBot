import aiogram 
import asyncio
from aiogram import Bot, Dispatcher
from app.handlers import router 

# example_token
API_TOKEN = '6814546521:AAEn-A0qhwzDBG7o5UUFIwRcOGkDR5A_dp0'

bot = Bot(token=API_TOKEN)


async def main():
    dp = Dispatcher()
    dp.include_router(router)
    await dp.start_polling(bot)


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except:
        print('The bot is offline')
    aiogram.methods.delete_webhook.DeleteWebhook


