from marshmallow import Schema, fields, validate

class ProductoSchema(Schema):
    id = fields.Integer() # id es opcional
    nombre = fields.Str(
        required=True,
        error_messages={
            "required": "El nombre es obligatorio",
            "invalid": "El campo no tiene un formato de string",
        },
        validate=validate.Length(min=4, error="El nombre debe tener al menos 4 letras"),
    )
    precio = fields.Number(
        required=True,
        error_messages={
            "required": "El precio es obligatorio",
            "invalid": "El campo no tiene un formato numérico",
        },
        validate=validate.Range(min=0, error="El precio no puede ser negativo"),
    )
    imagen = fields.Str(required=True)
    categoria_id = fields.Integer(required=True)

class ProductoConCategoriaSchema(ProductoSchema):
    categoria = fields.Nested("CategoriaSchema")