from flask import Flask, send_file
from db import db
from routes import rutas_productos, rutas_categorias

app = Flask(__name__)

@app.get('/images/<filename>')
def serve_image(filename):
    print(filename)
    image_path = 'images/' + filename
    return send_file(image_path, mimetype='image/jpeg') 

app.register_blueprint(rutas_categorias, url_prefix="/categorias")
app.register_blueprint(rutas_productos, url_prefix="/productos")

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///categoria-productos.db"
# pip install pymysql OR pip install mysql-connector-python
# app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:<password>@localhost/productos"
# app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+mysqlconnector://root:<password>@localhost/productos"
# No hace falta indicar el puerto si es el 5000. Si se indica, se debe poner así: ...localhost:5000/...

db.init_app(app)

with app.app_context():
    db.create_all()

app.run()