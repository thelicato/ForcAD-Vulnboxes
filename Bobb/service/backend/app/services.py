import time
from pathlib import Path
from app.db import User, Coupon, Product
from app.extensions import bcrypt
from app.utils import get_uuid
from app.products import dummy_product
import app.logger as logger


def me(user_id: int):
    user = User.get(User.id == user_id)
    coupons = [{"coupon": coupon.id, "value": coupon.value}
               for coupon in user.coupons]
    res = {"id": user_id, "username": user.username,
           "credit": user.credit, "coupons": coupons}
    return res


def register(username: str, password: str):
    user_exists = User.select().where(User.username == username).exists()

    if user_exists:
        raise Exception('User already exists')

    hashed_password = bcrypt.generate_password_hash(password)
    new_user = User.create(id=get_uuid(), username=username, password=hashed_password)

    # Generate a coupon associated with this user
    Coupon.create(id=get_uuid(), user=new_user)

    res = {"message": "User correctly created"}
    return res

def image(image_path: str):
    MAIN_DIR = Path(__file__).parent.absolute()
    full_path = str(MAIN_DIR) + "/static/" + image_path
    return full_path

def login(username: str, password: str):
    user_exists = User.select().where(User.username == username).exists()
    if not user_exists:
        raise Exception('Wrong credentials')

    user = User.get(User.username == username)
    coupons = [{"coupon": coupon.id, "value": coupon.value}
               for coupon in user.coupons]
    if not bcrypt.check_password_hash(user.password, password):
        raise Exception('Wrong credentials')

    res = {"id": user.id, "username": user.username,
           "credit": user.credit, "coupons": coupons}
    return res

def products():
    products = Product.select()
    res = {'products': [{"id": p.id, "name": p.name, "description": p.description, "image": p.image, "price": p.price} for p in products]}
    return res

def redeem(user_id: int, coupon_id: str):
    coupon_exists = Coupon.select().where(Coupon.id == coupon_id).exists()
    if not coupon_exists:
        raise Exception('Invalid coupon')

    coupon = Coupon.get(Coupon.id == coupon_id)
    if coupon.used:
        raise Exception('Invalid coupon')

    user = User.get(User.id == user_id)

    # Add the credit and set the coupon as used
    User.update(credit=user.credit+coupon.value).where(User.id == user.id).execute()
    Coupon.update(used=True).where(Coupon.id == coupon.id).execute()

    res = {"message": "Coupon redeemed correctly"}
    return res


def buy(user_id: int, product_id: int):
    product_exists = Product.select().where(Product.id == product_id).exists()
    if not product_exists:
        raise Exception('Invalid product')

    product = Product.get(Product.id == product_id)
    user = User.get(User.id == user_id)

    if user.credit < product.price:
        raise Exception("You don't have enough money to buy this product!")

    # Subtract the credit and obtain the product
    User.update(credit=user.credit-product.price).where(User.id == user.id).execute()

    res = {"id": product.id, "name": product.name, "value": product.value}
    return res

def get_flag(product_hash: str):
    product_exists = Product.select().where(Product.hash == product_hash).exists()
    if not product_exists:
        logger.error(f"Unable to find the product with hash '{product_hash}'")
        logger.info("Currently the products are:")
        for p in Product.select().dicts():
            print(p)

        raise Exception('Invalid product')

    product = Product.get(Product.hash == product_hash)
    res = {"id": product.id, "name": product.name, "value": product.value}
    return res

def put_flag(product):
    db_products = Product.select().where(Product.id != dummy_product['id']).dicts()
    oldest_product = db_products[0]
    for p in db_products:
        if p['ts'] < oldest_product['ts']:
            oldest_product = p
    logger.info(f"Updating the product with id {oldest_product['id']}")
    
    ts = time.time()
    Product.update(value=product['value'], hash=product['hash'], ts=ts).where(Product.id == oldest_product['id']).execute()
    res = {"message": "Flag correctly set"}
    return res