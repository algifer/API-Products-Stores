"""
@file manage.py
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

from flask_script import Manager 
from flask_migrate import Migrate, MigrateCommand
from app.app import app, db
import unittest

# Handling database migrations
migrate = Migrate(app, db)

# Command handling for the application
manager = Manager(app)

# To add database-related commands
manager.add_command('db', MigrateCommand)

@manager.command
def run():
    """
    @function run() 
    @brief This method executes the entire application, allowing the 
            database to start and the flask server to start.

    """
    db.init_app(app)
    app.run()

@manager.command
def test():
    """
    @function test() 
    @brief This method allows the unit tests to be executed automatically, 
            by calling the files in the path "... / app / test /".
    @return int
            0: ok
            1: nok
    """
    tests = unittest.TestLoader().discover('app/test', pattern='test*.py')
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    if result.wasSuccessful():
        return 0
    return 1

if __name__ == '__main__':
	manager.run()