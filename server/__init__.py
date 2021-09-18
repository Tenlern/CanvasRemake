import os
from typing import Union, Any
from flask import Flask, request, render_template, url_for


# Основная функция сервера
def setup_app():
    # Создаем экземпляр приложения
    app = Flask(
        __name__,
        instance_relative_config=True,
        template_folder='../templates',
        static_folder='../static'
    )
    app.config.from_mapping(
        DATABASE=os.path.join(app.instance_path, 'canvas.sqlite')
    )

    @app.route('/')
    def hello_world():
        script_url = url_for('static', filename='script.js')
        return render_template('editor.html', script_url=script_url)

    @app.route('/api/init')
    def init_editor():
        return {}

    @app.route('/api/node/<int:id>')
    def node(id) -> Union[dict[str, Any], dict[str, Any], str]:
        # Перегружаем метод api для разных методов запроса
        # Получение данных
        if request.method == "GET":
            return {"id": id}

        # Удаление
        elif request.method == "DELETE":
            return {"id": id}

        else:
            return 'OOPS'
    return app


if __name__ == '__main__':
    app = setup_app()
    app.run()
