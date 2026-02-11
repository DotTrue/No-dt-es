from time import localtime

import aiogram
from aiogram import Bot, Dispatcher, types
import time
import asyncio
tbot = Bot("8557021561:AAEDonBAtzLjqGEwzEJ7XlTa_HIFqYCNWMc")
thandl = Dispatcher()
@thandl.message()
async def handler(msg: types.InputTextMessageContent):
    print('hello', msg.from_user.id,f"{localtime().tm_hour}:{localtime().tm_min}:{localtime().tm_sec}")

async def main():
    await tbot.delete_webhook(drop_pending_updates=True)
    await thandl.start_polling(tbot)

if __name__ == '__main__':
    asyncio.run(main())