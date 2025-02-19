from flask import Flask, request
from marshmallow import ValidationError

from eshop.businsess_logic.order_usecases import order_create, order_get_many, order_get_by_id
from eshop.businsess_logic.product_usecases import product_get_many,product_create,product_get_by_id
from eshop.view.order_schemas import OrderCreateDtoSchema, OrderSchema, OrderGetManyParams
from eshop.view.order_schemas import ProductSchema,ProductCreateDtoSchema,ProductGetManyParams

app = Flask(__name__)


@app.post("/api/v1/order")
def order_create_endpoint():
    print("rrrr")
    try:
        order_create_dto = OrderCreateDtoSchema().load(request.json)
    except ValidationError as err:
        return err.messages, 400

    try:
        order = order_create(
            product_ids=order_create_dto['product_idsR']
        )
    except Exception as e:
        return {
            "error": str(e)
        }

    return OrderSchema().dump(order)


@app.get("/api/v1/order")
def order_get_many_endpoint():
    try:
        order_get_many_params = OrderGetManyParams().load(request.args)
    except ValidationError as err:
        return err.messages, 400

    order = order_get_many(
        page=order_get_many_params['page'],
        limit=order_get_many_params['limit'],
    )
    return OrderSchema(many=True).dump(order)

@app.get("/api/v1/product")
def product_get_many_endpoint():
    try:
        product_get_many_params = ProductGetManyParams().load(request.args)
    except ValidationError as err:
        return err.messages, 400

    order = product_get_many(
        page=product_get_many_params['page'],
        limit=product_get_many_params['limit'],
    )
    return ProductSchema(many=True).dump(order)
@app.get("/api/v1/order/<id>")
def order_get_by_id_endpoint(id):
    order = order_get_by_id(id)

    if order is None:
        return {
            "error": 'Not found'
        }, 404

    return OrderSchema().dump(order)
@app.get("/api/v1/product/<id>")
def product_get_by_id_endpoint(id):
    product = product_get_by_id(id)

    if product is None:
        return {
            "error": 'Not found'
        }, 404

    return ProductSchema().dump(product)
@app.post("/api/v1/product")
def create_product():
    print("ssss")
    try:
        data = request.get_json()
        product_create_dto = ProductCreateDtoSchema().load(data)
    except ValidationError as err:
        return err.messages, 400

    try:
        product,www = product_create(product_create_dto)
    except Exception as e:
        return {
            "error": str(e)
        }
    #OrderSchema().dump(order)
    if www:
        return ["Продукт был обновлён",ProductSchema().dump(product)]
    else:
        return ProductSchema().dump(product)

def run_server():
    app.run()
