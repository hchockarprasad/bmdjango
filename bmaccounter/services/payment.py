from bmcore.models import Account


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

        credit_sum = 0

        debit_sum = 0

        for item in transactions:

            credit_sum += item['credit']

            debit_sum += item['debit']

            if self._has_valid_position(item['account'], item['credit'], item['debit']) is False:

                return False

        if credit_sum + debit_sum != 0:

            return False

        return True
