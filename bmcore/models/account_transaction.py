from django.db import models

from bmcore.models.account import Account

from bmcore.models.voucher import Voucher


# Account Transaction manager
class AccountTransactionManager(models.Manager):

    def create(self, voucher, **kwargs):

        instance = self.model()

        instance.voucher = voucher

        instance.account = kwargs.get('account', None)

        instance.debit = kwargs.get('debit', 0)

        instance.credit = kwargs.get('credit', 0)

        instance.debit_pend = kwargs.get('debit_pend', None)

        instance.credit_pend = kwargs.get('credit_pend', None)

        instance.account1 = kwargs.get('account1', None)

        instance.narration = kwargs.get('narration', None)

        instance.instrument_no = kwargs.get('instrument_no', None)

        instance.instrument_date = kwargs.get('instrument_date', None)

        instance.bank_name = kwargs.get('bank_name', None)

        instance.save()

        return instance

    @staticmethod
    def update(inst, voucher, **kwargs):

        instance = inst

        instance.voucher = voucher

        instance.account = kwargs.get('account', None)

        instance.debit = kwargs.get('debit', None)

        instance.credit = kwargs.get('credit', None)

        instance.debit_pend = kwargs.get('debit_pend', None)

        instance.credit_pend = kwargs.get('credit_pend', None)

        instance.account1 = kwargs.get('account1', None)

        instance.narration = kwargs.get('narration', None)

        instance.instrument_no = kwargs.get('instrument_no', None)

        instance.instrument_date = kwargs.get('instrument_date', None)

        instance.bank_name = kwargs.get('bank_name', None)

        instance.save()

        return instance


class AccountTransaction(models.Model):

    voucher = models.ForeignKey(Voucher, related_name="account_transactions", blank=True, null=True)

    account = models.ForeignKey(Account, related_name="transaction_account", blank=True, null=True)

    debit = models.DecimalField(max_digits=20, decimal_places=2, default=0, blank=True, null=True)

    credit = models.DecimalField(max_digits=20, decimal_places=2, default=0, blank=True, null=True)

    debit_pend = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)

    credit_pend = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)

    account1 = models.ForeignKey(Account, related_name="cash_transfer_account", blank=True, null=True)

    narration = models.CharField(max_length=50, blank=True, null=True)

    bwd = models.CharField(max_length=50, blank=True, null=True)

    instrument_no = models.CharField(max_length=50, blank=True, null=True)

    instrument_date = models.DateField(blank=True, null=True)

    bank_name = models.CharField(max_length=50, blank=True, null=True)

    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)

    updated = models.DateTimeField(auto_now=True, auto_now_add=False)

    objects = AccountTransactionManager()

    class Meta:
        db_table = 'tbl_acc_tran'
        ordering = ["-timestamp", "-updated"]

    def __unicode__(self):
        return str(self.id)

    def __str__(self):
        return str(self.id)
