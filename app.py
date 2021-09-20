from server import db, setup_app

app=setup_app()
db.create_all(app=app)

if __name__ == '__main__':
    app.run(host='0.0.0.0')
