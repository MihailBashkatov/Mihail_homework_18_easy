# Импорт необходимых библиотек
from flask_restx import Namespace, Resource

# Импорт модели
from models.genre import Genre, GenreSchema

# Импорт базы данных
from setup_db import db

# Формирование сереилизаторов для модели Genre для одного элемента и для списка
genres_ns = Namespace('genres')
genre_schema = GenreSchema()
genres_schema = GenreSchema(many=True)


@genres_ns.route('/')
class GenresViews(Resource):
    def get(self):
        """
            Формирование представления для получения жанров
        """
        try:
            all_genres = db.session.query(Genre).all()
            return genres_schema.dump(all_genres)
        except Exception as e:
            return f'{e}', 404


@genres_ns.route('/<gid>')
class GenreViews(Resource):
    def get(self, gid):
        """
            Формирование представления для получения жанра по id
            В случае отсутствия фильма - ошибка
        """
        try:
            genre = db.session.query(Genre).filter(Genre.id == gid).one()
            return genre_schema.dump(genre), 200
        except Exception as e:
            return f'{e}', 404
