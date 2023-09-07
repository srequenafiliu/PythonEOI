from flask import Blueprint, jsonify, request
from PIL import Image
import io, base64, os
from db import db
from models import Producto
from schemas import validate_json, ProductoSchema, ProductoConCategoriaSchema

productos = Blueprint('productos', __name__)

def guarda_imagen(json):
    imagen_str = json["imagen"].split(",")[1] if json["imagen"].startswith("data") else json["imagen"]
    img = Image.open(io.BytesIO(base64.decodebytes(bytes(imagen_str, "utf-8"))))
    ruta = f"images/{json['nombre']}.jpg"
    img.convert('RGB').save(f"{os.path.dirname(__file__)}/../{ruta}")
    return ruta

@productos.get('') # type: ignore
def get_productos():
    args = request.args
    select = db.select(Producto)
    if args.get("categoria"):
        select = select.where(Producto.categoria_id == args.get("categoria"))
    if args.get("order"):
        select = select.order_by(getattr(Producto, args.get("order"))) # type: ignore
    productos = db.session().execute(select).scalars().all()
    schema = ProductoSchema(many=True)
    return jsonify(schema.dump(productos))

@productos.get('/<int:id>')
def get_producto(id: int):
    producto = db.get_or_404(Producto, id)
    schema = ProductoConCategoriaSchema()
    return jsonify(schema.dump(producto))

@productos.post('') # type: ignore
@validate_json(ProductoSchema)
def add_productos():
    json = request.json
    ruta = guarda_imagen(json)
    if (json):
        producto = Producto(nombre=json["nombre"], precio=json["precio"], imagen=request.host_url+ruta,
                            categoria_id=json["categoria_id"])
        db.session().add(producto)
        db.session().commit()
        schema = ProductoConCategoriaSchema()
        return jsonify(schema.dump(producto)), 201  # Devuelve el producto con código HTTP 201 (Created)

@productos.put('/<int:id>') # type: ignore
@validate_json(ProductoSchema)
def update_productos(id: int):
    producto = db.get_or_404(Producto, id)
    json = request.json
    if (json):
        if not json["imagen"].startswith("http"): # base64
            ruta = guarda_imagen(json)
            producto.imagen = request.host_url+ruta
        producto.nombre = json["nombre"]
        producto.precio = json["precio"]
        db.session().commit()
        schema = ProductoConCategoriaSchema()
        return jsonify(schema.dump(producto))
    
@productos.delete('/<int:id>')
def delete_producto(id: int):
    producto = db.get_or_404(Producto, id)
    db.session().delete(producto)
    db.session().commit()
    return "", 204