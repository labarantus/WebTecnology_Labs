import os
import datetime

"""
    Модуль с описанием конфигурации для приложения Flask
"""


class Config(object):
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # Параметр для подключения БД
    SQLALCHEMY_DATABASE_URI = f'sqlite:///{os.path.join(os.path.abspath(os.path.dirname(__file__)), "appdb.sqlite")}'
    SECRET_KEY = 'usatu2024code'
    SESSION_COOKIE_NAME = 'user_sid'
    SESSION_COOKIE_HTTPONLY = True
    SESSION_COOKIE_SECURE = False
    PERMANENT_SESSION_LIFETIME = datetime.timedelta(minutes=10)

