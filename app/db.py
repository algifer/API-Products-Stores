"""
@file db.py
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

from flask_sqlalchemy import SQLAlchemy
from app.app import db

# Helper class for some general database methods.
class BaseModelMixin:
    """
    @class BaseModelMixin()
    @brief this class is used as inheritance in models.
    """
    def save(self):
        """
        @function save()
        @brief Method to add new register in database.
        """
        db.session.add(self)
        db.session.commit()

    def delete(self):
        """
        @function delete()
        @brief Method to delete new register in database.
        """
        db.session.delete(self)
        db.session.commit()

    @classmethod
    def get_all(cls):
        """
        @function get_all()
        @brief Method to get all the registers of a table in the database.
        @return a object.
        """
        return cls.query.all()

    @classmethod
    def get_by_id(cls, id):
        """
        @function get_by_id()
        @brief Method to obtain a record by Id of a table in the database.
        @return a object.
        """
        return cls.query.get(id)

    @classmethod
    def simple_filter(cls, **kwargs):
        """
        @function simple_filter()
        @brief Method to perform a filtered query on a table in the 
                database.
        @return a object.
        """
        return cls.query.filter_by(**kwargs).all()
