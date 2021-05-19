from cffconvert.ApalikeObject import ApalikeObject
import unittest
import os
import ruamel.yaml as yaml
from test.contracts.ApalikeObject import Contract


class ApalikeObjectTest(Contract, unittest.TestCase):

    def setUp(self):
        fixture = os.path.join(os.path.dirname(__file__), "CITATION.cff")
        with open(fixture, "r", encoding="utf8") as f:
            cffstr = f.read()
            cff_object = yaml.safe_load(cffstr)
            self.ao = ApalikeObject(cff_object, initialize_empty=True)

    def test_check_cff_object(self):
        with self.assertRaises(ValueError) as context:
            self.ao.check_cff_object()
        self.assertTrue('Missing key "cff-version" in CITATION.cff file.' in str(context.exception))

    def test_author(self):
        pass

    def test_year(self):
        pass

    def test_title(self):
        pass

    def test_version(self):
        pass

    def test_doi(self):
        pass

    def test_url(self):
        pass
