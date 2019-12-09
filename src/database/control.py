import datetime
import sqlite3
import os


class Manager:
    def __init__(self, db_name):
        self.db_name = db_name
        self.write_headers(self.create_db())
    
    def create_db(self):
        if not os.path.exists(self.db_name):
            os.mknod(self.db_name)
            return False
        else:
            return True

    def connect(self):
        connection = sqlite3.connect(self.db_name)
        cursor = connection.cursor()
        return cursor , connection
    
    def write_headers(self , exist):
        if not exist:
            cursor = self.connect()
            cursor[0].execute("""CREATE TABLE users 
                            (username text , join_date datetime , user_id int , rules int , promocode int , discord text , steam text)
                        """)
            cursor[0].close()

    def add_user(self , **args):
        tupl = ( 
            args.pop('username' , None),
            args.pop('join_date' , None),
            args.pop('user_id' , None),
            args.pop('rules' , None),
            args.pop('promocode' , None),
            args.pop('discord' , None),
            args.pop('steam' , None)
        )
        d = self.connect()
        d[0].execute("INSERT INTO users VALUES(?,?,?,?,?,?,?)" , tupl)
        d[1].commit()

    
    def change_discord(self , user_id , value):
        d = self.connect()
        command = 'UPDATE users SET discord = "{0}" WHERE user_id = {1}'.format(value , user_id)
        d[0].execute(command)
        d[1].commit()
   
    def change_steam(self , user_id , value):
        d = self.connect()
        command = 'UPDATE users SET steam = "{0}" WHERE user_id = {1}'.format(value , user_id)
        d[0].execute(command)
        d[1].commit()
    def exists(self , user_id):
        d = self.connect()
        command = 'SELECT username FROM users WHERE user_id = {0}'.format(user_id)
        d[0].execute(command)
        if len(d[0].fetchall()) == 0:
            return False
        else:
            return True
    def get_urls(self , user_id):
        d = self.connect()
        command = 'SELECT discord,steam FROM users WHERE user_id = {0}'.format(user_id)
        d[0].execute(command)
        return d[0].fetchall()

# d = Manager('/home/hasan/extbot/users.db')
# print(d.get_urls(263838377))