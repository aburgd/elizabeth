import re
from unittest import TestCase

from elizabeth.builtins import Brazil, USA


class BrazilTest(TestCase):
    def setUp(self):
        self.pt_br = Brazil()

    def tearDown(self):
        del self.pt_br

    def test_cpf(self):
        # test if the cpf has 14 digits with the mask
        cpf_with_mask = self.pt_br.cpf()
        self.assertEqual(len(cpf_with_mask), 14, cpf_with_mask)
        # test the mask
        non_numeric_digits = re.sub('\d', '', cpf_with_mask)
        self.assertEqual('..-', non_numeric_digits, non_numeric_digits)
        self.assertEqual(len(re.sub('\D', '', cpf_with_mask)),
                         11, cpf_with_mask)
        # test for the cpf without mask
        cpf_without_mask = self.pt_br.cpf(False)
        self.assertEqual(len(cpf_without_mask), 11, cpf_without_mask)
        non_numeric_digits = re.sub('\d', '', cpf_without_mask)
        self.assertEqual('', non_numeric_digits, non_numeric_digits)

    def test_cnpj(self):
        # test if the cnpj has 14 digits with the mask
        cnpj_with_mask = self.pt_br.cnpj()
        self.assertEqual(len(cnpj_with_mask), 18, cnpj_with_mask)
        # test the mask
        non_numeric_digits = re.sub('\d', '', cnpj_with_mask)
        self.assertEqual('../-', non_numeric_digits, non_numeric_digits)
        self.assertEqual(len(re.sub('\D', '', cnpj_with_mask)),
                         14, cnpj_with_mask)
        # test for the cnpj without mask
        cnpj_without_mask = self.pt_br.cnpj(False)
        self.assertEqual(len(cnpj_without_mask), 14, cnpj_without_mask)
        non_numeric_digits = re.sub('\d', '', cnpj_without_mask)
        self.assertEqual('', non_numeric_digits, non_numeric_digits)


class USATest(TestCase):
    def setUp(self):
        self.en = USA()

    def tearDown(self):
        del self.en

    def test_usps_tracking_number(self):
        result = self.en.usps_tracking_number()
        self.assertIsNotNone(result)
        self.assertTrue(len(result) == 24 or len(result) == 17)

    def test_fedex_tracking_number(self):
        result = self.en.fedex_tracking_number()
        self.assertIsNotNone(result)
        self.assertTrue(len(result) == 14 or len(result) == 18)

    def test_ups_tracking_number(self):
        result = self.en.ups_tracking_number()
        self.assertIsNotNone(result)
        self.assertTrue(len(result) == 18)