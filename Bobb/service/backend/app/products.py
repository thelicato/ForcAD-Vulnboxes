import time
from app.db import Product

dummy_product = {
    "id": "0",
    "hash": "nothing",
    "value": "EHEHEH it is not so easy",
    "name": "Flag",
    "description": "This is the flag you were looking for!",
    "price": 10,
    "image": "flag.png",
}

products = [
    {
        "id": "1",
        "name": "Pizza Pomodorino",
        "description": "La pizza che più ci rappresenta,la nostra POMODORINO. In questa pizza abbiamo racchiuso le nostre origini e la nostra idea di SEMPLICITÀ E BONTÀ. ASSAPORALA AD OCCHI CHIUSI",
        "price": 50,
        "image": "pomodorino.jpg",
    },
    {
        "id": "2",
        "name": "Pizza Friarielli",
        "description": "Concediti un momento di vero godimento con la nostra #pizzanelruoto SALSICCIA E FRIARIELLI",
        "price": 60,
        "image": "friarielli.jpg",
    },
    {
        "id": "3",
        "name": "Pizza Patata",
        "description": "ALL YOU NEED IS LOVE, ALL YOU NEED IS BOBB. Ti aspettiamo domani per festeggiare la nostra grande storia d’amore",
        "price": 70,
        "image": "patata.jpg",
    },
    {
        "id": "4",
        "name": "Pizza Porchetta",
        "description": "AD MAIORA SEMPER! La nuova porchetta è troppa spaurita ",
        "price": 50,
        "image": "porchetta.jpg",
    },
    {
        "id": "5",
        "name": "Pizza Nerano",
        "description": "LA NUOVA NERANO! Crema di zucchine,zucchine fritte,formaggio e fior di latte",
        "price": 60,
        "image": "nerano.jpg",
    },
    {
        "id": "6",
        "name": "Pizza Ciurilli",
        "description": "A CIURILLI! Fiori di zucca, Salame, Ricotta, Formaggio, Pepe, Fior di latte. E che ve lo dico a fare!",
        "price": 60,
        "image": "ciurilli.jpg"
    }
]

def init_products():
    product_exists = Product.select().where(Product.id == dummy_product['id']).exists()
    if not product_exists:
        ts = time.time()
        Product.create(id=dummy_product['id'], name=dummy_product['name'], description=dummy_product['description'], value=dummy_product['value'], price=dummy_product['price'], image=dummy_product['image'], hash=dummy_product['hash'], ts=ts)
    for p in products:
        product_exists = Product.select().where(Product.id == p['id']).exists()
        if not product_exists:
            ts = time.time()
            Product.create(id=p['id'], name=p['name'], description=p['description'], value='', price=p['price'], image=p['image'], hash='', ts=ts)
