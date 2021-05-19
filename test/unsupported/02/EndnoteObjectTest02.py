from cffconvert import EndnoteObject
import unittest
import os
import ruamel.yaml as yaml
from test.contracts.EndnoteObject import Contract


class EndnoteObjectTest(Contract, unittest.TestCase):

    def setUp(self):
        fixture = os.path.join(os.path.dirname(__file__), "CITATION.cff")
        with open(fixture, "r", encoding="utf8") as f:
            cffstr = f.read()
            cff_object = yaml.safe_load(cffstr)
            self.eo = EndnoteObject(cff_object, initialize_empty=True)

    def test_author(self):
        pass

    def test_check_cff_object(self):
        with self.assertRaises(ValueError) as context:
            self.eo.check_cff_object()
        self.assertTrue('Expected cff_object to be of type \'dict\'.' in str(context.exception))

    def test_doi(self):
        pass

    def test_keyword(self):
        pass

    def test_name(self):
        pass

    def test_print(self):
        pass

    def test_url(self):
        pass

    def test_year(self):
        pass

