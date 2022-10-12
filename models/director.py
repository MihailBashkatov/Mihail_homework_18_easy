# Импорт нееобходимых биьлиотек
from marshmallow import Schema, fields

# Импорт базы данных
from setup_db import db


# Формирование класса Director
class Director(db.Model):
    __tablename__ = 'director'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)


# Формирование схемы Director
class DirectorSchema(Schema):
    id = fields.Int()
    name = fields.Str()
