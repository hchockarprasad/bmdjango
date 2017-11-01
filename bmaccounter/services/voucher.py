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

    def create(self):

        if self._has_valid_ac_tran():

            voucher_data = dict()

            voucher_data['created_by'] = self.voucher.get('created_by', None)

            voucher_data['voucher_type'] = self.voucher.get('voucher_type', None)

            # Created by user is required for creating a voucher
            if not voucher_data['created_by']:

                raise ValueError('Cannot create voucher without created-by user')

            # Voucher type is required for creating a voucher
            if not voucher_data['voucher_type']:

                raise ValueError('Cannot create voucher without voucher-type')

            # Get user's branch from his profile
            voucher_data['branch'] = self.voucher.get('created_by').userprofile.branch

            voucher_data['trans_date'] = self.voucher.get('trans_date')

            # Add trans_date as value_date if value_date is not provided
            voucher_data['value_date'] = self.voucher.get('value_date', self.voucher.get('trans_date'))

            # Rounded defaults to 0 if not provided
            voucher_data['rounded'] = self.voucher.get('rounded', 0)

            # Discount defaults to 0 if not provided
            voucher_data['discount'] = self.voucher.get('discount', 0)

            # Generate voucher_no using the provided voucher-type
            voucher_data['voucher_no'] = utils.gen_vch_no(self.voucher.get('voucher_type'))

            # Reference defaults to null if not provided
            voucher_data['ref_no'] = self.voucher.get('ref_no', None)

            # Tax exempts defaults to False if not provided
            voucher_data['tax_exempt'] = self.voucher.get('tax_exempt', False)

            # Mark status of all voucher as True if not explicitly given
            voucher_data['status'] = self.voucher.get('status', True)

            # Account1 value defaults to null if not provided or extracted
            voucher_data['account1'] = self.voucher.get('account1', self._account1())

            # Account2 value defaults to null if not provided or extracted
            voucher_data['account2'] = self.voucher.get('account1', self._account2())

            # Cashier default to null if not provided
            voucher_data['cashier'] = self.voucher.get('cashier', None)

            # Customer defaults to null if not provided
            voucher_data['customer'] = self.voucher.get('customer', None)

            # Doctor defaults to null if not provided
            voucher_data['doctor'] = self.voucher.get('doctor', None)

            # Opening account defaults to null if not provided
            voucher_data['op_account'] = self.voucher.get('op_account', None)

            # Opening inventory defaults to null if not provided
            voucher_data['op_inventory'] = self.voucher.get('op_inventory', None)

            # Create voucher based on above arguments
            voucher_obj = Voucher.objects.create(**voucher_data)

            return voucher_obj

        return ValueError('Account transactions are not valid')
