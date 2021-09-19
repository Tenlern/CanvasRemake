import os
import uuid
from typing import Union, Any
from flask import Flask, request, render_template, url_for
from flask_sqlalchemy import SQLAlchemy
from server.database import db, Node


def setup_app() -> Flask:
    """
    Инициализация сервера
    :return: Flask экземпляр Flask
    """
    # Создаем экземпляр приложения
    app = Flask(
        __name__,
        instance_relative_config=True,
        template_folder='../templates',
        static_folder='../static'
    )
    app.config.from_mapping(
        # DATABASE=os.path.join(app.instance_path, 'canvas.sqlite')
        SQLALCHEMY_DATABASE_URI='sqlite:////tmp/test.db'
    )

    db.init_app(app)

    @app.route('/')
    def hello_world():
        """
        Возвращаем главную страницу и подключаем к ней статический скрипт
        :rtype: object
        """
        script_url = url_for('static', filename='script.js')
        return render_template('editor.html', script_url=script_url)

    @app.route('/api/init')
    def init_editor():
        """
        Метод подготовки редактора к работе
        :rtype: object
        """
        return {}

    @app.route('/api/node/', methods=['POST'])
    def create_node():
        """
        Метод регистрации нового узла
        :return:
        """

        db.session.add

        return {}

    @app.route('/api/node/<uuid:node_id>', methods=['GET', 'UPDATE', 'DELETE'])
    def node(node_id):
        """
        Метод для работы с узлами
        :rtype: object
        """
        # Перегружаем метод api для разных методов запроса
        # Получение данных
        if request.method == "GET":
            return {"id": node_id}

        # Удаление
        elif request.method == "DELETE":
            return {"id": node_id}

        else:
            return 'OOPS'

    @app.errorhandler(404)
    def not_found():
        """
        Обработчки ошибки 404
        :return:
        """
        return 'OOPS'

    return app


if __name__ == '__main__':
    app = setup_app()
    app.run()
