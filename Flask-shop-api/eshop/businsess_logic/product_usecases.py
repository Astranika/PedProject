from typing import Optional, List
from eshop.businsess_logic.product import Product
from eshop.data_access.product_repo import save, get_by_id, get_many

def product_create(Dto) -> Product:
    product_create_dto=Dto
    existing_product = get_by_id(product_create_dto['id'])
    www=False
    if existing_product is not None:
        www=True

    product = Product(
        id=product_create_dto['id'],
        name=product_create_dto['name'],
        price=product_create_dto['price']
    )

    save(product)

    return product,www

def product_get_by_id(id: str) -> Optional[Product]:
    return get_by_id(id)
    #raise Exception('Not implemented yet')


def product_get_many(page: int, limit: int) -> List[Product]:
    return get_many(page=page, limit=limit)
    #raise Exception('Not implemented yet')