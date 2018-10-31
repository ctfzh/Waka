# -*- coding: UTF-8 -*-

import configparser
import os


class ReadConfig:
    def __init__(self):
        config_path = "%s/config.ini" % os.path.abspath(os.path.join(os.getcwd(), ".."))
        self.cf = configparser.ConfigParser()
        self.cf.read(config_path, encoding="utf-8-sig")

    def get_db(self, name):
        value = self.cf.get("DATABASE", name)
        return value

    def get_ssh(self, name):
        value = self.cf.get("SSH", name)
        return value

    def get_http(self, name):
        value = self.cf.get("HTTP", name)
        return value

    def get_email(self, name):
        value = self.cf.get("EMAIL", name)
        return value

    def get_data(self, name):
        value = self.cf.get("DATA", name)
        return value
