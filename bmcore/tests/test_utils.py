from django.test import TestCase

from bmcore.models.voucher_model import VoucherModel

from bmcore import utils

from bmcore.tests import utils as test_utils


# Write account tests here


class UtilsTests(TestCase):

    def setUp(self):

        test_utils.load_initial_data()

    def test_increment_voucher(self):
        """
        Ensure voucher model gets incremented by 1 when needed
        """

        voucher_type = 'SALE'

        vch_obj = VoucherModel.objects.get(voucher_template__voucher_type__name=voucher_type)

        existing_vch_no = vch_obj.vch_no

        new_obj = utils.increment_voucher(voucher_type)

        new_vch_no = new_obj.vch_no

        if new_vch_no > existing_vch_no:

            result = 'New voucher no is greater than old one'

        else:

            result = 'New voucher no'

        self.assertEqual(result, 'New voucher no is greater than old one')
