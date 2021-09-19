from server import db, setup_app

app = setup_app()

if __name__ == '__main__':
    db.create_all()
    app.run(host='0.0.0.0')
