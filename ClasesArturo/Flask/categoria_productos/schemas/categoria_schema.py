from marshmallow import Schema, fields, validate

class CategoriaSchema(Schema):
    id = fields.Integer() # id es opcional
    nombre = fields.Str(
        required=True,
        error_messages={
            "required": "El nombre es obligatorio",
            "invalid": "El campo no tiene un formato de string",
        },
        validate=validate.Length(min=4, error="El nombre debe tener al menos 4 letras"),
    )

class CategoriaConProductosSchema(CategoriaSchema):
    productos = fields.Nested("ProductoSchema", many=True)