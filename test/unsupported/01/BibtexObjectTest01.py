from cffconvert.BibtexObject import BibtexObject
import unittest
import os
import ruamel.yaml as yaml
from test.contracts.BibtexObject import Contract


class BibtexObjectTest(Contract, unittest.TestCase):

    def setUp(self):
        fixture = os.path.join(os.path.dirname(__file__), "CITATION.cff")
        with open(fixture, "r", encoding="utf8") as f:
            cffstr = f.read()
            cff_object = yaml.safe_load(cffstr)
            self.bo = BibtexObject(cff_object, initialize_empty=True)

    def test_author(self):
        # CFF file is not valid, hence contract does not apply
        pass

    def test_check_cff_object(self):
        with self.assertRaises(ValueError) as context:
            self.bo.check_cff_object()
        self.assertTrue(str(context.exception).startswith('\'cff-version\':') and
                        str(context.exception).endswith('isn\'t a supported version.'))

    def test_doi(self):
        # CFF file is not valid, hence contract does not apply
        pass

    def test_month(self):
        # CFF file is not valid, hence contract does not apply
        pass

    def test_print(self):
        # CFF file is not valid, hence contract does not apply
        pass

    def test_title(self):
        # CFF file is not valid, hence contract does not apply
        pass

    def test_url(self):
        # CFF file is not valid, hence contract does not apply
        pass

    def test_year(self):
        # CFF file is not valid, hence contract does not apply
        pass
