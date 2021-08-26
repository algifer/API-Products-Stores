"""
@file app.py
@ingroup CARGAMOS
@project Test
@brief
                This software is copyright protected and proprietary to CARGAMOS.
                All other rights remain with CARGAMOS.
@author Algemiro J. Gil Fernandez
@version Module: 1.0.0.0
@delivery 202108
@date 2021-08-25
@company CARGAMOS
@description:	This document follows the standards defined in
                https://devguide.python.org/documenting/
@known issues:  None

"""
__author__ = "Algemiro J. Gil Fernandez"
__copyright__ = "Copyright 2010, CARGAMOS"
__licence__ = "GPL"
__version__ = "1.0.0.0"
__maintainer__ = "Algemiro Jose Gil Fernandez"
__email__ = "algifer53@gmail.com"
__status__ = "Production"

from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from logging.config import dictConfig
import threading, asyncio, logging

from config.config import *

# Database and flask server configuration
app = Flask(__name__)
dictConfig(logging_config)
app.config.from_object(config_by_name['dev'])
db = SQLAlchemy(app)

# Import models from the database
from app.models import Store, Product, StoreProducts

# Constructor for log records
log = logging.getLogger(__name__)
log.info("App Initializing.")

@app.route('/')
def index():
    """
    @function index()
    @brief Method that allows the display of the start message.
    @return json type message.
    """
    log.info(f"Inside flask function: {threading.current_thread().name}")
    asyncio.set_event_loop(asyncio.new_event_loop())
    loop = asyncio.get_event_loop()
    result = loop.run_until_complete(index())
    return jsonify({"result": result})

@app.route('/store', methods=['GET','POST','PUT'])
def store():
    """
    @function store()
    @brief Method that allows the display of the start message.
    @return json type message.
    """
    if request.method == 'GET':
        log.info(f"Inside flask function: {threading.current_thread().name}")
        asyncio.set_event_loop(asyncio.new_event_loop())
        loop = asyncio.get_event_loop()
        result = loop.run_until_complete(get_store())
        return jsonify({"result": result})

    elif request.method == 'POST':
        log.info(f"Inside flask function: {threading.current_thread().name}")
        asyncio.set_event_loop(asyncio.new_event_loop())
        loop = asyncio.get_event_loop()
        result = loop.run_until_complete(add_store())
        return jsonify({"result": result})

    elif request.method == 'PUT':
        log.info(f"Inside flask function: {threading.current_thread().name}")
        asyncio.set_event_loop(asyncio.new_event_loop())
        loop = asyncio.get_event_loop()
        result = loop.run_until_complete(update_inventory())
        return jsonify({"result": result})
    
    else:
        return {"message": "Incorrect query."}

@app.route('/product', methods=['POST','GET'])
def product():
    """
    @function store()
    @brief Method that allows the display of the start message.
    @return json type message.
    """
    if request.method == 'POST':
        log.info(f"Inside flask function: {threading.current_thread().name}")
        asyncio.set_event_loop(asyncio.new_event_loop())
        loop = asyncio.get_event_loop()
        result = loop.run_until_complete(add_product())
        return jsonify({"result": result})

    elif request.method == 'GET':
        log.info(f"Inside flask function: {threading.current_thread().name}")
        asyncio.set_event_loop(asyncio.new_event_loop())
        loop = asyncio.get_event_loop()
        result = loop.run_until_complete(get_product())
        return jsonify({"result": result})

# Information path '/store/info' queried using the GET method.
@app.route('/store/info')
def information():
    """
    @function information()
    @brief Method that allows only store inventory information.
    """
    if request.method == 'GET':
        log.info(f"Inside flask function: {threading.current_thread().name}")
        asyncio.set_event_loop(asyncio.new_event_loop())
        loop = asyncio.get_event_loop()
        result = loop.run_until_complete(get_inventory())
        return jsonify({"result": result})

    else:
        return {"message": "Incorrect query."}

## Synchronous handling of startup message.
async def index():
    """
    @function index()
    @brief This method allows to display the welcome or start message to
            the server.
    @return json type message.
    """
    try:
        return {"message": "Welcome to Store!"}

    except Exception as e:
        result = {"Exception": str(e)}
        return result

## Asynchronous handling to get all the stores from the database.
async def get_store():
    """
    @function get_store()
    @brief Method to obtain the information of the stores 
            registered in the database.
    @return json type message.
    """
    await asyncio.sleep(DELAY_TIME)
    stores = Store.query.all()
    if (len(stores) > 0):
        results = [{"idStore": store.idStore,
                "name": store.name,
                "information": store.information} for store in stores]
        return {"message": "Stores List",
                "count": len(results), 
                "stores": results}
 
    else:
        return {
            "message": "There aren't registered stores",
            "count": len(stores)}

## Asynchronous handling to add store to database.
async def add_store():
    """
    @function add_store()
    @brief Method to register new stores in the database.
    @return json type message.
    """
    await asyncio.sleep(DELAY_TIME)    
    storeData = request.get_json()
    if ("name" and "information" in storeData):
        #Add new stores.
        newStore = Store(name = storeData['name'],
                        information = storeData['information'])
        try:
            Store.save(newStore)
            return {"message": "The Store has been added succesfully"}
        except Exception as e:
            result = {
                "message": "Store data cannot be added because it"+' '+
                            "is already in the database."}
            return result

    elif ("idStore" and "idProduct" and "quantity" in storeData):
        id_store = storeData['idStore']
        id_product = storeData['idProduct']
        quantity = storeData['quantity']
        storeProduct = db.session.query(StoreProducts).filter(
            StoreProducts.id_store == id_store).filter(
            StoreProducts.id_product == id_product).first()
        if storeProduct:
            # Update inventory
            db.session.query(StoreProducts).filter(
                StoreProducts.id_store == id_store).filter(
                StoreProducts.id_product == id_product).update({
                    StoreProducts.id_store: id_store,
                    StoreProducts.id_product: id_product,
                    StoreProducts.quantity: quantity})
            db.session.commit()
            return {
                "message": """The inventory has been updated successfully"""}
        else:
            # Add new inventory
            product = db.session.query(Product).filter(
                    Product.idProduct == id_product).first()
            store = db.session.query(Store).filter(
                    Store.idStore == id_store).first()
            if (product and store):
                newInv = StoreProducts(id_store,id_product,quantity)
                StoreProducts.save(newInv)
                return {
                    "message": "New inventory has been added successfully"}
            else:
                return {
                    "message": "Product or Store incorrect"}

    else:
        return {"message": "Query Incorrect"}

## Asynchronous handling to update store inventory.
async def update_inventory():
    """
    @function update_inventory()
    @brief Method that allows updating and/or relating a product to 
            a store and its quantity.
    @return json type message.
    """
    await asyncio.sleep(DELAY_TIME)
    # Modify the data of the stores.
    storeData = request.get_json()
    if ("idStore" and "idProduct" and "quantity" in storeData):
        id_store = storeData['idStore']
        id_product = storeData['idProduct']
        quantity = storeData['quantity']
        storeProduct = db.session.query(StoreProducts).filter(
            StoreProducts.id_store == id_store).filter(
            StoreProducts.id_product == id_product).first()
        if storeProduct:
            # Update inventory
            db.session.query(StoreProducts).filter(
                StoreProducts.id_store == id_store).filter(
                StoreProducts.id_product == id_product).update({
                    StoreProducts.id_store: id_store,
                    StoreProducts.id_product: id_product,
                    StoreProducts.quantity: quantity})
            db.session.commit()
            return {
                "message": "The inventory has been updated successfully"}
        else:
            return {"message": "Unable to update inventory"}

    else:
        return {"message": "Query Incorrect"}

## Asynchronous handling to obtain the stock of a store's products.
async def get_product():
    """
    @function get_product()
    @brief This method allows you to obtain the stock of a product 
            from a certain store.
    @return json type message.
    """
    if request.is_json:
        storeData = request.get_json()
        # Get Stock of product in Store.
        if ("idProduct" in storeData):
            id_product = storeData['idProduct']
            storeProducts = db.session.query(StoreProducts).filter(
                StoreProducts.id_product == id_product).first()
            productData = db.session.query(Product).filter(
                Product.idProduct == id_product).first()
            if storeProducts:
                products = StoreProducts.query.all()
                results = [{"idStore": product.id_store,
                            "quantity": product.quantity
                    } for product in products if (
                        product.id_product == id_product)]
                return {"message": "Stores List by Product.",
                        "sku": productData.sku,
                        "count": len(results),
                        "stores": results}
            else:
                return {
                    "message": "The product is not associated with the "+
                                "store."}
        else:
            return {"message": "Incorrect message."}

    else:
        # Query of all products created.
        products = Product.query.all()
        results = [{"idProduct": product.idProduct,
                "sku": product.sku,
                "information": product.information
            } for product in products]

        return {"message": "Products List",
                "count": len(results),
                "products": results}

## Asynchronous handling to add new products.
async def add_product():
    """
    @function add_product()
    @brief Method to add products to the database.
    @return json type message.
    """
    await asyncio.sleep(DELAY_TIME)
    # Insert new products to the database
    productData = request.get_json()
    newProduct = Product(sku = productData['sku'],
                    information = productData['information'])
    try:
        Product.save(newProduct)
        return {
            "message": "The product has been added succesfully"}
    except Exception as e:
        result = {
            "message": "Store data cannot be added because "+
                        "it is already in the database."}
        return result

## Asynchronous inventory query handling.
async def get_inventory():
    """
    @function get_inventory()
    @brief Method to query the inventory of stores asynchronously.
    @return json type message.
    """
    data = {}
    data["store"] = []
    stores = Store.query.all()
    if (len(stores) > 0):
        for store in stores:
            data1 = {"idStore": store.idStore,
                    "name": store.name,
                    "information": store.information,
                    "inventory": []}
            storesProducts = db.session.query(StoreProducts).filter(
                StoreProducts.id_store == store.idStore).all()
            if storesProducts:
                for stProd in storesProducts:
                    product = db.session.query(Product).filter(
                        Product.idProduct == stProd.id_product).first()
                    if product:
                        data2 = {
                            "idProduct": product.idProduct,
                            "sku": product.sku,
                            "quantity": stProd.quantity,
                            "information": product.information}
                        data1["inventory"].append(data2)
            data["store"].append(data1)

        return {
            "message": "Stores Inventory.", "data": data}
    else:
        return {
            "message": "There aren't stores products."}
