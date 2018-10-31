# -*- coding: UTF-8 -*-
import pymysql
from sshtunnel import SSHTunnelForwarder
import readConfig


class MyDB:
    def __init__(self):
        config = readConfig.ReadConfig()
        global db_host, db_user, db_pass, db_port, sh_host, sh_port, sh_user, sh_pass
        db_host = config.get_db("db_host")
        db_user = config.get_db("db_user")
        db_pass = config.get_db("db_pass")
        db_port = config.get_db("db_port")
        sh_host = config.get_ssh("sh_host")
        sh_port = config.get_ssh("sh_port")
        sh_user = config.get_ssh("sh_user")
        sh_pass = config.get_ssh("sh_pass")
        self.db = None
        self.cursor = None

    def connectDB(self):
        try:
            self.server = SSHTunnelForwarder(
                ssh_address_or_host=(sh_host, int(sh_port)),  # 跳板机的配置
                ssh_username=sh_user,  # 跳板机的用户名
                ssh_password=sh_pass,  # 跳板机的密码
                remote_bind_address=(db_host, int(db_port))  # 数据库的配置
            )
            self.server.start()
            self.db = pymysql.connect(
                host='127.0.0.1',  # 此处必须是是127.0.0.1
                port=self.server.local_bind_port,
                user=db_user,  # 数据库的用户名
                passwd=db_pass,  # 数据库的密码
                charset='utf8')
            print("Connect DB successfully!")
            self.cursor = self.db.cursor()
        except ConnectionError as ex:
            print(ex)

    def executeSQL(self, sql):
        self.connectDB()
        self.cursor.execute(sql)
        self.db.commit()
        return self.cursor

    @staticmethod
    def get_all(cursor):
        value = cursor.fetchall()
        return value

    @staticmethod
    def get_one(cursor):
        value = cursor.fetchone()
        return value

    def closeDB(self):
        self.db.close()
        self.server.stop()
        print("Database closed!")
