from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Node(db.Model):
    __tablename__ = 'nodes'

    id = db.Column(db.String(36), primary_key=True)
    # name = db.Column(db.String(50), unique=True)
    x = db.Column(db.Float, nullable=False)
    y = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f"Node {self.id} placed x={self.x}, y={self.y}"

class Edge(db.Model):
    __tablename__ = 'edges'

    id = db.Column(db.String(36), primary_key=True)
    # parent = db.MANYTOONE()
