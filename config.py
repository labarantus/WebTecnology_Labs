import os

"""
    Модуль с описанием конфигурации для приложения Flask
"""


class Config(object):
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # Параметр для подключения БД
    SQLALCHEMY_DATABASE_URI = f'sqlite:///{os.path.join(os.path.abspath(os.path.dirname(__file__)), "appdb.sqlite")}'
