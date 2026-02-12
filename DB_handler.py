import sqlite3
import asyncio
from dataclasses import dataclass
import datetime
@dataclass
class DB_handler:
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

    async def assing_key_value(self,user_,key):
        if not user_: return None
        self.cursor.execute("INSERT OR REPLACE INTO userskeys (user,key) VALUES (?,?)",(user_,key))
        self.conn.commit()

    async def check_user_key(self,user_): # return a key of a given user
        if not user_: return "Pls give a user"
        self.cursor.execute(f"SELECT keys FROM userskeys WHERE user = ? ",(user_,))
        result = await self.cursor.fetchone()
        return result

    async def load_in_msg(self,msg,chat_id,user_):
        today = datetime.datetime.now()
        formatted = today.strftime("%d.%m")  # 12.03
        print(f"{formatted} -> {user_}, | INSERT TO A DATABASE")
        if not (user_ or chat_id or msg): return "Non Valid Data"
        self.cursor.execute("INSERT INTO messages (message,chatid,userid,datetime) VALUES(?,?,?,?)",(msg,chat_id,user_,formatted))
        self.conn.commit()
