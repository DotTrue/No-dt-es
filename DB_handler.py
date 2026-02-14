import sqlite3
import asyncio
from dataclasses import dataclass
import datetime
@dataclass
class DBMS:
    def __init__(self,dbpath):
        self.db_path = dbpath
        self.conn = sqlite3.connect(dbpath)
        self.cursor = self.conn.cursor()

    async def create_table(self):
        pass
    async def get_data(self):
        pass

    async def close_data(self):
        a = input("are you sure u want to close DBMS? Y/N:")
        if a.lower() == "y":
            self.conn.close()
        else:
            return None

    async def have_access(self,user_,chat):

        self.cursor.execute("SELECT key FROM keys WHERE chat = ?",(chat,))
        key1 = self.cursor.fetchone()

        if key1 is None: return False

        return key1 in self.cursor.execute("SELECT key FROM userskeys WHERE user = ?",(user_,)).fetchall()
    async def key_in_chat(self, chat): #ключ для этога чата
        if chat is int: chat = str(chat)

        self.cursor.execute("SELECT key FROM keys WHERE chat LIKE ?",(chat,))
        result = self.cursor.fetchall()
        return result

    async def get_bydate(self,user_,chat):

            if await self.have_access(user_,chat):
                print("acces granted")
                return self.cursor.execute("SELECT message,userid FROM messages WHERE datetime = ? and chatid = ?",(datetime.datetime.now().strftime("%d.%m"),chat)).fetchall()
    async def assing_key_value(self,user_,key):
        if not user_: return None
        self.cursor.execute("INSERT OR REPLACE INTO userskeys (user,key) VALUES (?,?)",(user_,key))
        self.conn.commit()

    async def check_user_key(self,user_): # return a keys of a given user
        self.cursor.execute(f"SELECT key FROM userkeys WHERE user = ?",(user_,))
        result =  self.cursor.fetchone()
        return result

    async def load_in_msg(self,msg,chat_id,user_):
        today = datetime.datetime.now()
        formatted = today.strftime("%d.%m")  # 12.03
        print(f"{formatted} -> {user_}, | INSERT TO A DATABASE")
        self.cursor.execute("INSERT INTO messages (message,chatid,userid,datetime) VALUES(?,?,?,?)",(msg,chat_id,user_,formatted))
        self.conn.commit()
