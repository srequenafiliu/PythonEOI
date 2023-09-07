from flask import Blueprint, jsonify, request
from PIL import Image
import io, base64, os
from db import db
from models import Categoria
from schemas import validate_json, CategoriaSchema, CategoriaConProductosSchema

categorias = Blueprint('categorias', __name__)

@categorias.get('') # type: ignore
def get_categorias():
    select = db.select(Categoria)
    categorias = db.session().execute(select).scalars().all()
    schema = CategoriaSchema(many=True)
    return jsonify(schema.dump(categorias))

@categorias.get('/<int:id>')
def get_categoria(id: int):
    categoria = db.get_or_404(Categoria, id)
    schema = CategoriaConProductosSchema()
    return jsonify(schema.dump(categoria))

@categorias.post('') # type: ignore
@validate_json(CategoriaSchema)
def add_categorias():
    json = request.json
    if (json):
        categoria = Categoria(nombre=json["nombre"])
        db.session().add(categoria)
        db.session().commit()
        return jsonify(categoria), 201  # Devuelve el producto con código HTTP 201 (Created)

@categorias.put('/<int:id>') # type: ignore
@validate_json(CategoriaSchema)
def update_categorias(id: int):
    categoria = db.get_or_404(Categoria, id)
    json = request.json
    if (json):
        categoria.nombre = json["nombre"]
        db.session().commit()
        return jsonify(categoria)
    
@categorias.delete('/<int:id>')
def delete_categoria(id: int):
    categoria = db.get_or_404(Categoria, id)
    db.session().delete(categoria)
    db.session().commit()
    return "", 204