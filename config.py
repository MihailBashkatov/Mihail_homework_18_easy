# Формирование конфигурации приложения


class Config:

    SQLALCHEMY_DATABASE_URI = "sqlite:///movies.db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JSON_PRETTYPRINT_REGULAR = True
    DEBUG = True
    RESTX_JSON = {'ensure_ascii': False, 'indent': 4}
