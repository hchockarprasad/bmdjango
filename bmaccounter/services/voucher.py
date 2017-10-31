

# Voucher Service
class VoucherService(object):

    def __init__(self, voucher, ac_tran_required=False, inv_tran_required=False):

        self.voucher = voucher

        self.ac_tran_required = ac_tran_required

        self.inv_tran_required = inv_tran_required

    def _has_valid_ac_tran(self):

        credit_sum = 0

        debit_sum = 0

        for item in self.voucher.account_transactions:

            credit_sum += item['credit']

            debit_sum += item['debit']

        if credit_sum + debit_sum != 0:

            return False

        if self.ac_tran_required:

            if self.voucher.account_transactions.count() == 0:

                return False

        return True

    def has_valid_voucher(self):

        if self._has_valid_ac_tran():

            return True

        return False
