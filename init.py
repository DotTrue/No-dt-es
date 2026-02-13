import json
from fileinput import close
from time import localtime
from prettytable import PrettyTable as PT

import asyncio
import aiogram
from aiogram import F
from aiogram import Bot, Dispatcher, types
from aiogram.utils.formatting import Spoiler, Text

from dataclasses import dataclass

#bot
tbot = Bot("8517781384:AAGnekkD_RoQFFdyw5wxPKxPBT61AGsSVhA")
tl_handle = Dispatcher()

#DB
import DB_handler
DBMS = DB_handler.DBMS("data.db3")

def laodcfg(cfgpath):
    with open(cfgpath, "r", encoding="utf-8") as f:
        return json.load(f)
data_cmd = laodcfg("commands.json")

@dataclass
class BotHandler:
    def __init__(self,handler: Dispatcher):
        self.t_handler = handler
        self.private_session_keys = []
        self.group_session_keys = []
        self.users_keys = {} #лучше сохранять в бд или джсон
        self.debounce = False
        self._debtime = 0.1
        self.init_links()
    async def debouncew(self):
        self.debounce = 0.2
        await asyncio.sleep(self._debtime)
        self.debounce = False

    def init_links(self):
        @self.t_handler.message(F.text.contains("айди"))
        async def handler(message: types.Message):
            print(message.from_user.id,"|",message.chat.id,"|",message.text)

        @self.t_handler.message(F.text.lower().contains(data_cmd["homework"]["connect"]))
        async def connect(msg: types.Message):
            if not msg.from_user.id: return "There's no user here"
            key = await DBMS.key_in_chat(msg.chat.id)
            if key in msg.text:
                await DBMS.assing_key_value(msg.from_user.id, key)
        @self.t_handler.message(F.text.lower().contains(data_cmd["homework"]["get_all"]))
        async def get(msg: types.Message):
            print("Do if statement",msg.from_user.id)
            #If statements
            # if not msg.from_user.id: return "There's no user here"
            # if not await DBMS.check_user_key(msg.from_user.id): return "There's no userkey here"
            # if not await DBMS.have_access(msg.from_user.id,msg.chat.id): return "No Access or DB not exists"
            messages = await DBMS.get_bydate(msg.from_user.id,msg.chat.id)
            print("GetMessages:",[[i[0],str(i[1])] for i in messages])
            #main
            pret = PT()
            pret.border = False
            pret.field_names = ["Сообщение","Юзер"]
            rows = [[i[0], await tbot.get_chat(i[1])] for i in messages]
            for i in rows:
                i[1] = i[1].first_name or i[1].username

            pret.add_rows(rows)
            print(pret)
            content = Text(
                Spoiler(pret)
            )
            await msg.reply(**content.as_kwargs())
        @self.t_handler.message(F.text.lower().contains(data_cmd["homework"]["get_today"]))
        async def get(msg: types.Message):
            if not msg.from_user.id: return "There's no user here"

        @self.t_handler.message(F.text.lower().contains(data_cmd["homework"]["wrote"]))
        async def get(msg: types.Message):
            print("funcHasBennCalled")
            #If statements
            if not msg.from_user.id: return "There's no user here"
            if not await DBMS.have_access(msg.from_user.id,msg.chat.id): return "No Access or DB not exists"
            if len(msg.text) <= 5: return "There's no text here"



            # main
            await DBMS.load_in_msg(msg.text,msg.from_user.id,msg.chat.id)

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
    bot = BotHandler(tl_handle)
    await tbot.delete_webhook(drop_pending_updates=True)
    await tl_handle.start_polling(tbot)

if __name__ == '__main__':
    asyncio.run(main())