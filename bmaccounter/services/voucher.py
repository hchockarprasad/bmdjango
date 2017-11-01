from bmcore import utils

from bmcore.models import Voucher


# Voucher Service
class VoucherService(object):

    def __init__(self, voucher, ac_tran_required=False, inv_tran_required=False):

        self.voucher = voucher

        self.account_transactions = voucher.get('account_transactions', [])

        self.inventory_transactions = voucher.get('inventory_transactions', [])

        self.ac_tran_required = ac_tran_required

        self.inv_tran_required = inv_tran_required

    def _has_valid_ac_tran(self):

        credit_sum = 0

        debit_sum = 0

        for item in self.account_transactions:

            credit_sum += item['credit']

            debit_sum += item['debit']

        if credit_sum + debit_sum != 0:

            return False

        if self.ac_tran_required:

            if self.account_transactions.count() == 0:

                return False

        return True

    def has_valid_voucher(self):

        if self._has_valid_ac_tran():

            return True

        return False

    def _account1(self):

        ac_tran = self.account_transactions

        try:

            return ac_tran[0].account

        except IndexError:

            return None

    def _account2(self):

        ac_tran = self.account_transactions

        try:

            return ac_tran[1].account

        except IndexError:

            return None

    def create_voucher(self):

        voucher_data = dict()

        voucher_data['created_by'] = self.voucher.get('created_by')

        voucher_data['branch'] = self.voucher.get('created_by').userprofile.branch

        voucher_data['trans_date'] = self.voucher.get('trans_date')

        voucher_data['value_date'] = self.voucher.get('value_date', self.voucher.get('trans_date'))

        voucher_data['rounded'] = self.voucher.get('rounded', 0)

        voucher_data['discount'] = self.voucher.get('discount', 0)

        voucher_data['voucher_type'] = self.voucher.get('voucher_type')

        voucher_data['voucher_no'] = utils.gen_vch_no(self.voucher.get('voucher_type'))

        voucher_data['ref_no'] = self.voucher.get('ref_no', None)

        voucher_data['tax_exempt'] = self.voucher.get('tax_exempt', False)

        voucher_data['status'] = self.voucher.get('status', True)

        voucher_data['account1'] = self.voucher.get('account1', self._account1())

        voucher_data['account2'] = self.voucher.get('account1', self._account2())

        voucher_data['cashier'] = self.voucher.get('cashier', None)

        voucher_data['customer'] = self.voucher.get('customer', None)

        voucher_data['doctor'] = self.voucher.get('doctor', None)

        voucher_data['op_account'] = self.voucher.get('op_account', None)

        voucher_data['op_inventory'] = self.voucher.get('op_inventory', None)

        voucher_obj = Voucher.objects.create(**voucher_data)

        return voucher_obj
