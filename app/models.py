"""
@file models.py
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

from app.app import db
from app.db import BaseModelMixin
from flask import jsonify
from sqlalchemy.dialects.postgresql import JSON

# Store model
class Store(db.Model,BaseModelMixin):
    """
    @class Store() 
    @brief The Store model allows creating the "stores" table in with 
            the following parameters:
    @param
            idStore: Integer, primary_key
            name: String, unique, nullable
            information: JSON
            stores: This parameter indicates that the table is related 
                        to the StoreProducts model.

            These parameters take parameters associated with the database 
            such as primary key, foreign key, etc.
    """
    __tablename__ = 'stores'

    idStore = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(), unique=True, nullable=False)
    information = db.Column(JSON)
    stores = db.relationship('StoreProducts')

    def __init__(self, name, information):
        """
        @function __init__()
        @brief Model initializer or constructor. This method needs the 
                "name" and "information" parameters.
        @param 
                name: str
                information: json
        """
        self.name = name
        self.information = information

    def __str__(self):
        """
        @function __str__()
        @brief magic method that returns a string of message.
        @return json type message.
        """
        return str(jsonify({"storeName": self.name}))

# Product model
class Product(db.Model,BaseModelMixin ):
    """
    @class Product()
    @brief The Store model allows creating the "products" in table with 
        the following parameters:
    @param 
            idProduct: Integer, primary_key
            sku: String, unique, nullable
            information: JSON
            products: This parameter indicates that the table is related 
                        to the StoreProducts model.

            These parameters take parameters associated with the database 
            such as primary key, foreign key, etc.
    """
    __tablename__ = 'products'

    idProduct = db.Column(db.Integer, primary_key=True)
    sku = db.Column(db.String(), unique=True, nullable=False)
    information = db.Column(JSON)
    products = db.relationship('StoreProducts')

    def __init__(self, sku, information):
        """
        @function __init__()
        @brief Model initializer or constructor.
                This method needs the "sku" and "information" parameters.
        @param 
                sku: str
                information: json
        """
        self.sku = sku
        self.information = information

    def __str__(self):
        """
        @function __str__()
        @brief magic method that returns a string of message.
        @return json type message.
        """
        return str(jsonify({"sku": self.sku}))

# StoreProducts model
class StoreProducts(db.Model,BaseModelMixin):
    """
    @class StoreProducts()
    @brief The Store model allows creating the "storeProducts" in table 
            with the following parameters:
    @param 
            idStoreProducts: Integer, primary_key
            id_store: Integer
            id_product: Integer
            quantity: IntegerThis parameter indicates that the table is related 
                        to the StoreProducts model.

            These parameters take parameters associated with the database 
            such as primary key, foreign key, etc.
    """
    __tablename__ = 'storeProducts'

    idStoreProducts = db.Column(db.Integer, primary_key=True)
    id_store = db.Column(db.Integer, db.ForeignKey('stores.idStore'))
    id_product = db.Column(db.Integer, db.ForeignKey('products.idProduct'))
    quantity = db.Column(db.Integer)

    def __init__(self, id_store, id_product, quantity):
        """
        @function __init__()
        @brief Model initializer or constructor. This method needs the 
                "id_store", "id_product" and "quantity" parameters.
        @param  
                sku: str
                information: json
        """
        self.id_store = id_store
        self.id_product = id_product
        self.quantity = quantity

    def __str__(self):
        """
        @function __str__()
        @brief magic method that returns a string of message.
        @return json type message.
        """
        return str(jsonify({"quantity": self.quantity}))

