import sqlite3
import threading
import time
import getter
import SQLiteManger


class saver():

    def __init__(self):

        self.table_name = "MainData"
        self.Basename = "Mineral.db"
        self.getter = getter.getter()
        self.sm = SQLiteManger.SQLiteManger(self.Basename)

    def getVal(self, i):
        print(f"准备获取第{i}个数据")
        res = self.getter.getInfo(i)
        try:
            res = res["features"][0]["attributes"]
        except Exception as e :
            print(e)
            return None
        list = []
        for v in res.values():
            list.append(v)
        return tuple(list)

    def saveInfo(self, i):

        sql = """
        insert into %s values (?,?,?,?,?,?,?,?,?,?)
        """ % self.table_name

        val = self.getVal(i)
        if not val:
            print(f"无法获取第{i}个数据")
            return

        self.sm.insert2(sql, val)

    def save100Info(self, start):
        for i in range(start, start + 100):
            try:
                self.saveInfo(i)
            except Exception as e:
            # except sqlite3.OperationalError as e:
                with open("err.txt","a",encoding='utf-8') as f:
                    f.write(str(i)+"\n")

                print(e)
            time.sleep(0.5)

    def save100Info2(self):
        start = self.getStart() + 1
        for i in range(start, start + 100):
            self.saveInfo(i)

    def save100Info3(self):
        start = self.getStart() + 1

        while True:
            for i in range(start, start + 100):
                self.saveInfo(i)
                time.sleep(0.1)
            start +=100

    def mutiSave(self):
        s = self.getStart()+1
        Max_thread_num  = 5
        while 1:
            while len(threading.enumerate()) > Max_thread_num:
                time.sleep(0.5)
            threading.Thread(target=self.save100Info, args=(s,)).start()
            s += 100

    def saveErr(self):
        with open("err.txt", 'r') as f:
            while True:
                t = f.readline()
                if not t:
                    break
                try:
                    self.saveInfo(int(t))
                except sqlite3.IntegrityError as e :
                    print(f"第{t}个数据已存在")

    def getStart(self):

        sql = """
                select max (OBJECTID) from %s
        """ % self.table_name

        start = self.sm.select(sql)
        if not start:
            return 0

        return int(start)


if __name__ == '__main__':
    s = saver()
    # s.save100Info3()

    # s.mutiSave()
    s.saveErr()