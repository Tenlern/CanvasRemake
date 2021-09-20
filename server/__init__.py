import os
import uuid
from typing import Union, Any
from flask import Flask, request, render_template, url_for, jsonify
from server.database import db, Node


def setup_app() -> Flask:
    """
    Инициализация и настройка сервера, обслуживающего api приложения
    :rtype: Flask
    :return: экземпляр Flask
    """
    # Создаем экземпляр приложения
    server: Flask = Flask(
        __name__,
        instance_relative_config=True,
        template_folder='../templates',
        static_folder='../static'
    )
    # Добавляем неоьходимые настройки для работы с SQLAlchemy
    server.config.from_mapping(
        SQLALCHEMY_DATABASE_URI='sqlite:///D:\\Projects\\CanvasRemake\\static\\app.db',
        SQLALCHEMY_TRACK_MODIFICATIONS=False
    )

    # Подключаем базу данных
    db.init_app(server)

    # Прописываем адреса, прослушиваемые сервером
    @server.route('/')
    def hello_world() -> object:
        """
        Возвращаем главную страницу и подключаем к ней статический файл js-скрипта
        :rtype: object
        """
        script_url = url_for('static', filename='script.js')
        return render_template('editor.html', script_url=script_url)

    @server.route('/api/init/', methods=['GET'])
    def init_editor():
        """
        Метод подготовки редактора к работе
        :rtype: JSON
        """
        nodes = Node.query.all()
        result = []
        for node in nodes:
            result.append(dict(
                group='nodes',
                data=dict(
                    id=node.id,
                ),
                position=dict(
                    x=node.x,
                    y=node.y
                ),
            ))
        return jsonify(result), 200

    @server.route('/api/node/', methods=['POST'])
    def create_node():
        """
        Метод регистрации нового узла
        :rtype: object
        :return:
        """
        data = request.get_json()

        node = Node(
            id=data['id'],
            x=data['position']['x'],
            y=data['position']['y']
        )

        db.session.add(node)
        db.session.commit()

        return {}, 201

    @server.route('/api/node/<uuid:node_id>', methods=['GET', 'PUT', 'PATCH', 'DELETE'])
    def node_rud(node_id: uuid) -> object:
        """
        Метод READ, UPDATE, DELETE для работы с узлами
        :rtype: object
        """

        node = Node.query.filter_by(id=str(node_id)).first_or_404()

        # Перегружаем метод api для разных методов запроса
        # Получение данных
        if request.method == "GET":
            return jsonify(node), 200

        # Обновление
        elif request.method == 'PATCH':
            data = request.get_json()

            node.x = float(data['x'])
            node.y = float(data['y'])

            db.session.commit()
            return {}, 204

        # Удаление
        elif request.method == "DELETE":
            # node = Node.query().get(node_id)
            node = Node.query.filter_by(id=str(node_id)).first_or_404()
            db.session.delete(node)
            db.session.commit()
            return {}, 204

    @server.errorhandler(404)
    def not_found():
        """
        Обработчки ошибки 404
        :return:
        """
        return 'OOPS'

    return server


if __name__ == '__main__':
    app = setup_app()
    app.run()
