import sqlite3
import asyncio

class DB_handler():
    def __init__(self,dbpath):
        self.db_path = dbpath
        self.conn = sqlite3.connect(dbpath)
        self.cursor = self.conn.cursor()

    async def create_table(self):
        pass
    async def get_data(self):
        pass
    async def check_user_key(self,user_): # return a key of a given user
        await self.cursor.execute(f"SELECT keys FROM userskeys WHERE user = ? ",(user_,))
        result = await self.cursor.fetchone()
        return result
