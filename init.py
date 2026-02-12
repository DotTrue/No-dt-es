from time import localtime

import asyncio
import aiogram
from aiogram import Bot, Dispatcher, types

#bot
tbot = Bot("8517781384:AAGnekkD_RoQFFdyw5wxPKxPBT61AGsSVhA")
tl_handle = Dispatcher()

class BotHandler():
    def __init__(self,handler: Dispatcher,):
        self.t_handler = handler
        self.private_session_keys = []
        self.group_session_keys = []
        self.debounce = False
        self.debtime = 0.1
    async def debouncew(self):
        self.debounce = True
        await asyncio.sleep(self.debtime)
        self.debounce = False


    async def init_links(self):
        @self.t_handler.message()
        async def handler(msg: types.InputTextMessageContent):
            if not self.debounce:
                await self.debouncew()


    async def command_list(self):
        pass
    async def guidence(self):
        pass
    async def get_keys(self):
        #todo make a DB request to get an generated API keys
        pass

#updater-entrypoint
async def main():
    await tbot.delete_webhook(drop_pending_updates=True)
    await tl_handle.start_polling(tbot)

if __name__ == '__main__':
    asyncio.run(main())