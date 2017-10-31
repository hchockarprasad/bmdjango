from bmcore.models import Account

from bmaccounter.services.voucher import VoucherService


# Payment Service
class PaymentService(object):

    _permitted_groups_for_debit = [24]

    _permitted_groups_for_credit = [25, 33]

    def __init__(self, user):

        self.user = user

    @property
    def cash_account(self):

        return self.user.userprofile.cash_account

    @property
    def credit_accounts(self):

        return Account.objects.filter(group__in=self._permitted_groups_for_credit).id

    @property
    def debit_accounts(self):

        return Account.objects.filter(group_id=self._permitted_groups_for_debit).id

    def _has_valid_position(self, account_id, credit, debit):

        if (credit > 0 and account_id in self.credit_accounts or
                debit > 0 and account_id in self.debit_accounts):

            return True

        return False

    def has_valid_transactions(self, transactions):

        for item in transactions:

            if self._has_valid_position(item['account'], item['credit'], item['debit']) is False:

                return False

        return True

    def create(self, voucher):

        voucher_service = VoucherService(voucher)

        if voucher_service.has_valid_voucher():

            return True

        return False
