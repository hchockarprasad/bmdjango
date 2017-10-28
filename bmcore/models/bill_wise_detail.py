from django.db import models

from bmcore.models.account import Account

from bmcore.models.account_transaction import AccountTransaction


# BillWiseDetail
class BillWiseDetailManager(models.Manager):

    def create(self, **kwargs):

        instance = self.model()

        instance.tran = kwargs.get('tran', None)

        instance.account = kwargs.get('account', None)

        instance.amount = kwargs.get('amount', None)

        instance.adj_id = kwargs.get('adj_id', None)

        instance.adj_ref = 1

        instance.ref_no = kwargs.get('ref_no', None)

        instance.save()

        if instance.adj_id is None:

            instance.adj_id = instance.id

            instance.adj_ref = 0

            instance.save()

        return instance

    @staticmethod
    def update(inst, **kwargs):

        instance = inst

        instance.tran = kwargs.get('tran', None)

        instance.account = kwargs.get('account', None)

        instance.amount = kwargs.get('amount', None)

        instance.adj_ref = kwargs.get('adj_ref', None)

        instance.adj_id = kwargs.get('adj_id', None)

        instance.ref_no = kwargs.get('ref_no', None)

        instance.save()

        return instance


# BillWiseDetail
class BillWiseDetail(models.Model):

    tran = models.ForeignKey(AccountTransaction, related_name='billwisedetails', blank=True, null=True)

    account = models.ForeignKey(Account, related_name='billwisedetail_account', blank=True, null=True)

    amount = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)

    adj_ref = models.IntegerField(blank=True, null=True)

    adj_id = models.IntegerField(blank=True, null=True)

    ref_no = models.CharField(max_length=25, blank=True, null=True)

    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)

    updated = models.DateTimeField(auto_now=True, auto_now_add=False)

    objects = BillWiseDetailManager()

    class Meta:
        db_table = 'tbl_acc_bwd'
        ordering = ["-timestamp", "-updated"]

    def __unicode__(self):
        return str(self.id)

    def __str__(self):
        return str(self.id)
