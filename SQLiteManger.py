import sqlite3
import time


class SQLiteManger():
    # conn = sqlite3.connect()
    # c = conn.cursor()

    def __init__(self,db_path):
        self.conn = sqlite3.connect(db_path,check_same_thread=False)


    def insert(self, sql):
        self.c = self.conn.cursor()
        self.c.execute(sql)
        self.conn.commit()

    def insert2(self, sql,val):
        self.c = self.conn.cursor()
        self.c.execute(sql,val)
        self.conn.commit()

    def select(self,sql):
        self.c = self.conn.cursor()
        res = tuple(self.c.execute(sql))
        return res[0][0]

    def select2(self,sql, val):
        res = tuple(self.c.execute(sql, val))
        return res

    def creat_table(self,sql):
        self.c = self.conn.cursor()
        self.c.execute(sql)
        self.conn.commit()

    def end(self):
        self.conn.close()


if __name__ == '__main__':
    db_path = 'Mineral.db'
    sm = SQLiteManger(db_path)
    # sql = '''
    #     create table Mineral
    #         (time int primary_key not null,
    #         price int
    #
    #         )
    # '''






