#!/usr/bin/env python
# -*- coding: utf-8 -*-

""":Mod: test_eml_to_dom

:Synopsis:

:Author:
    servilla
  
:Created:
    9/30/16
"""

import unittest
import logging

import eml_2_1_1

logging.basicConfig(format='%(asctime)s %(levelname)s (%(name)s): %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S%z')
logging.getLogger('').setLevel(logging.WARN)
logger = logging.getLogger('test_eml_to_dom')


class TestEmlToDom(unittest.TestCase):

    def setUp(self):
        self.eml = open('../data/knb-lter-bes.1000.120.xml').read()

    def tearDown(self):
        self.eml = None

    def test_assert_eml(self):
        self.assertIsNotNone(self.eml)

    def test_create_dom(self):
        eml = eml_2_1_1.CreateFromDocument(self.eml)


if __name__ == '__main__':
    unittest.main()
