from flask import Blueprint, jsonify, request
from db import db
from models import Tarea
from schemas import validate_json, TareaSchema

tareas = Blueprint('tareas', __name__)

@tareas.get('') # type: ignore
def get_tareas():
    select = db.select(Tarea)
    tareas = db.session().execute(select).scalars().all()
    return jsonify(tareas)

@tareas.get('/<int:id>')
def get_tarea(id: int):
    tarea = db.get_or_404(Tarea, id)
    return jsonify(tarea)

@tareas.post('') # type: ignore
@validate_json(TareaSchema)
def add_tareas():
    json = request.json
    if (json):
        tarea = Tarea(descripcion=json["descripcion"], realizada=json["realizada"])
        db.session().add(tarea)
        db.session().commit()
        return jsonify(tarea), 201

@tareas.put('/<int:id>') # type: ignore
@validate_json(TareaSchema)
def update_tareas(id: int):
    tarea = db.get_or_404(Tarea, id)
    json = request.json
    if (json):
        tarea.descripcion = json["descripcion"]
        tarea.realizada = json["realizada"]
        db.session().commit()
        return jsonify(tarea)
    
@tareas.delete('/<int:id>')
def delete_tarea(id: int):
    tarea = db.get_or_404(Tarea, id)
    db.session().delete(tarea)
    return "", 204