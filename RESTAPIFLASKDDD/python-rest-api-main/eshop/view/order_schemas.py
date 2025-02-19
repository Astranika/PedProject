from marshmallow import Schema, fields


class OrderCreateDtoSchema(Schema):
    product_idsR = fields.List(fields.Str(), required=True)


class OrderSchema(Schema):
    id = fields.String()
    product_ids = fields.List(fields.Str())
    total = fields.Float()
    name=fields.List(fields.Str(),missing=[])


class OrderGetManyParams(Schema):
    page = fields.Int(required=True)
    limit = fields.Int(required=True)

class ProductGetManyParams(Schema):
    page = fields.Int(required=True)
    limit = fields.Int(required=True)
class ProductSchema(Schema):
    id = fields.String(required=True)
    #product_ids = fields.List(fields.Str())
    price = fields.Float(required=True)
    name=fields.Str(required=True)


class ProductCreateDtoSchema(Schema):
    id = fields.Str(required=True)
    name = fields.Str(required=True)
    price = fields.Float(required=True)