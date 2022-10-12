# Импорт необходимых библиотек
from flask import request
from flask_restx import Namespace, Resource

# Импорт модели
from models.movie import Movie, MovieSchema

# Импорт базы данных
from setup_db import db

# Формирование сереилизаторов для модели Movie для одного элемента и для списка
movies_ns = Namespace('movies')
movie_schema = MovieSchema()
movies_schema = MovieSchema(many=True)


@movies_ns.route('/')
class MoviesViews(Resource):
    def get(self):
        """
            Формирование представления для получения фильмов
        """
        try:
            all_movies = db.session.query(Movie).all()
            movies = movies_schema.dump(all_movies)

            # При квери-запросе по director
            data_director = request.args.get('director_id')
            if data_director:
                data = db.session.query(Movie).filter(Movie.director_id == data_director).all()
                movies = movies_schema.dump(data)

            # При квери-запросе по genre
            data_genre = request.args.get('genre_id')
            if data_genre:
                data = db.session.query(Movie).filter(Movie.genre_id == data_genre).all()
                movies = movies_schema.dump(data)

            # При квери-запросе по year
            data_year = request.args.get('year')
            if data_year:
                data = db.session.query(Movie).filter(Movie.year == data_year).all()
                movies = movies_schema.dump(data)

            # Если запрос возвращает пустой список, то возвращается 'No such movie'
            if len(movies) == 0:
                return 'No such movie', 200
            return movies
        except Exception as e:
            return f'{e}', 404

    def post(self):
        """
            Формирование представления для добавления нового фильма
        """
        try:
            data_json = request.json
            movie = Movie(**data_json)
            db.session.add(movie)
            db.session.commit()
            return '', 201
        except Exception as e:
            return f'{e}', 404


@movies_ns.route('/<mid>')
class MovieViews(Resource):
    def get(self, mid):
        """
            Формирование представления для получения фильма по id
            В случае отсутствия фильма - ошибка
        """
        try:
            # movie = Movie.query.get(mid)
            movie = db.session.query(Movie).filter(Movie.id == mid).one()
            return movie_schema.dump(movie), 200
        except Exception as e:
            return f'{e}', 404

    def put(self, mid):
        """
            Формирование представления для изменения данных режиссера по id
            В случае отсутствия режиссера - ошибка
        """
        try:
            data = request.json
            db.session.query(Movie).filter(Movie.id == mid).update(data)
            db.session.commit()
            return '', 201
        except Exception as e:
            return f'{e}', 404

    def delete(self, mid):
        """
            Формирование представления для удалени режиссера по id
            В случае отсутствия режиссера - ошибка
        """
        try:
            db.session.query(Movie).filter(Movie.id == mid).delete()
            db.session.commit()
            return '', 201
        except Exception as e:
            return f'{e}', 404
