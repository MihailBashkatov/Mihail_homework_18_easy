# Импорт необходимых библиотек
from flask_restx import Namespace, Resource

# Импорт модели
from models.director import Director, DirectorSchema

# Импорт базы данных
from setup_db import db

# Формирование сереилизаторов для модели Director для одного элемента и для списка
directors_ns = Namespace('directors')
director_schema = DirectorSchema()
directors_schema = DirectorSchema(many=True)


@directors_ns.route('/')
class DirectorsViews(Resource):
    def get(self):
        """
            Формирование представления для получения режиссеров
        """
        try:
            all_directors = db.session.query(Director).all()
            return directors_schema.dump(all_directors)
        except Exception as e:
            return f'{e}', 404


@directors_ns.route('/<did>')
class DirectorViews(Resource):
    def get(self, did):
        """
            Формирование представления для получения режиссера по id
            В случае отсутствия фильма - ошибка
        """
        try:
            director = db.session.query(Director).filter(Director.id == did).one()
            return director_schema.dump(director), 200
        except Exception as e:
            return f'{e}', 404
