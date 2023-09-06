from flask import Flask
from db import db
from routes import rutas_productos

app = Flask(__name__)

app.register_blueprint(rutas_productos, url_prefix="/productos")

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"

db.init_app(app)

with app.app_context():
    db.create_all()

app.run()