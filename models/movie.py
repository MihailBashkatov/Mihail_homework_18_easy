# Импорт нееобходимых биьлиотек
from marshmallow import Schema, fields

# Импорт схем
from models.director import DirectorSchema
from models.genre import GenreSchema

# Импорт базы данных
from setup_db import db


# Формирование класса Movie
class Movie(db.Model):
    __tablename__ = 'movie'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    description = db.Column(db.String)
    trailer = db.Column(db.String)
    year = db.Column(db.Integer)
    rating = db.Column(db.Integer)
    genre_id = db.Column(db.Integer, db.ForeignKey('genre.id'))
    director_id = db.Column(db.Integer, db.ForeignKey('director.id'))
    genre = db.relationship('Genre')
    director = db.relationship('Director')


# Формирование схемы Movie
class MovieSchema(Schema):
    id = fields.Int()
    title = fields.Str()
    description = fields.Str()
    trailer = fields.Str()
    year = fields.Int()
    rating = fields.Str()
    genre = fields.Pluck(field_name='name', nested=GenreSchema)
    director = fields.Pluck(field_name='name', nested=DirectorSchema)
