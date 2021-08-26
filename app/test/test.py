"""
@file test.py
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

import unittest
from app.app import app
import json
 
class Test(unittest.TestCase):
    """
    @class Test() 
    @brief is to define the test.
    """

    def setUp(self):
        "" "test setup" ""
 
        self.app = app

        # Definition of client app
        self.client = app.test_client()
 
    def test_index(self):
        "" "Test for index" ""

        self.setUp()

        # Use object client to send a get request to the backend, the data
        # indicates the data sent and a response object will be returned
        response = self.client.get("/")

        # response data
        resp_json = response.data

        # deserialize json data to dictionary
        resp_dict = json.loads(resp_json)
 
        # Verification of the content of the deserialized response data
        self.assertIn("message", resp_dict['result'])
  
    def test_add_store(self):
        "" "Test to add stores" ""

        self.setUp()

 
if __name__ == '__main__':
    unittest.main()
