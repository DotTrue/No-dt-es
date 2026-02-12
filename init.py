import json
from time import localtime


import asyncio
import aiogram
from aiogram import F
from aiogram import Bot, Dispatcher, types

from dataclasses import dataclass
#bot
tbot = Bot("8517781384:AAGnekkD_RoQFFdyw5wxPKxPBT61AGsSVhA")
tl_handle = Dispatcher()


with open("commands.json", "r", encoding="utf-8") as f:
    data_cmd = json.load(f)

@dataclass
class BotHandler:
    def __init__(self,handler: Dispatcher):
        self.t_handler = handler
        self.private_session_keys = []
        self.group_session_keys = []
        self.users_keys = {} #лучше сохранять в бд или джсон
        self.debounce = False
        self._debtime = 0.1

        #DB


    async def debouncew(self):
        self.debounce = 23123231234
        await asyncio.sleep(self._debtime)
        self.debounce = False

    async def init_links(self):
        @self.t_handler.message(F.text.lower().contains(data_cmd["homework"]["connect"]))
        async def connect(msg: types.Message):
            if not msg.from_user.id: return "There's no user here"
            if not msg.from_user.id in self.private_session_keys:
                self.users_keys[msg.from_user.id] = []
            self.key = "wait"
            if not self.key in self.users_keys[msg.from_user.id]:
                self.users_keys[msg.from_user.id].append(self.key)

        @self.t_handler.message(F.text.lower().contains(data_cmd["homework"]["get_on_tomorrow"]))
        async def get(msg: types.Message):
            if not msg.from_user.id: return "There's no user here"

        @self.t_handler.message(F.text.lower().contains(data_cmd["homework"]["get_today"]))
        async def get(msg: types.Message):
            if not msg.from_user.id: return "There's no user here"

        @self.t_handler.message(F.text.lower().contains(data_cmd["homework"]["write_in"]))
        async def get(msg: types.Message):
            if not msg.from_user.id: return "There's no user here"

        @self.t_handler.message(F.text.lower().contains(data_cmd["homework"]["edit_in"]))
        async def get(msg: types.Message):
            if not msg.from_user.id: return "There's no user here"
    async def command_list(self):
        pass
    async def guidence(self):
        pass
    async def get_keys(self):
        #todo make a DB request to get a generated API keys
        pass

#updater-entrypoint
async def main():
    await tbot.delete_webhook(drop_pending_updates=True)
    await tl_handle.start_polling(tbot)

if __name__ == '__main__':
    asyncio.run(main())