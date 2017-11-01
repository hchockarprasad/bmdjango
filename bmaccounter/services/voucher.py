from bmcore import utils

from bmcore.models import Voucher, AccountTransaction, BillWiseDetail, Pending


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

            # Vouchers are allowed only for branch with type as 2
            if voucher_data['branch'].branch_type == 2:

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

                for ac_tran in self.account_transactions:

                    account_transaction_data = dict()

                    account_transaction_data['account'] = ac_tran.get('account', None)

                    if not account_transaction_data['account']:

                        raise ValueError('Account transactions cannot be performed without an account')

                    account_transaction_data['debit'] = ac_tran.get('debit', 0)

                    account_transaction_data['credit'] = ac_tran.get('credit', 0)

                    account_transaction_data['narration'] = ac_tran.get('narration', None)

                    account_transaction_data['instrument_no'] = ac_tran.get('instrument_no', None)

                    account_transaction_data['voucher'] = voucher_obj

                    account_transaction_obj = AccountTransaction.objects.create(**account_transaction_data)

                    for ac_bwd in self.account_transactions.billwisedetails:

                        billwisedetail_data = dict()

                        billwisedetail_data['account'] = account_transaction_obj.account

                        billwisedetail_data['amount'] = ac_bwd.get('amount', None)

                        if not billwisedetail_data['amount']:

                            raise ValueError('Account bwd cannot be added without amount value')

                        billwisedetail_data['adj_id'] = ac_bwd.get('adj_id', None)

                        billwisedetail_obj = BillWiseDetail.objects.create(**billwisedetail_data)

                        pending_data = dict()

                        if billwisedetail_obj.adj_ref == 0:

                            pending_data['bill_amount'] = billwisedetail_obj.amount

                            pending_data['adjusted'] = 0

                            pending_data['adj_id'] = billwisedetail_obj.adj_id

                            pending_data['account'] = billwisedetail_obj.account

                            pending_data['ref_no'] = voucher_obj.voucher_no

                            pending_data['branch'] = voucher_obj.branch

                            Pending.objects.create(**pending_data)

                        elif billwisedetail_obj.adj_ref == 1:

                            pending_obj = Pending.objects.get(adj_id=billwisedetail_obj.adj_id)

                            pending_data['adj_id'] = billwisedetail_obj.adj_id

                            pending_data['adjusted'] = pending_obj.adjusted + billwisedetail_obj.amount

                            Pending.objects.update(pending_obj, pending_data)

                return voucher_obj

            return ValueError('Vouchers are not allowed for this branch')

        return ValueError('Account transactions are not valid')
