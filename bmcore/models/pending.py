from django.db import models

from bmcore.models import (
    Account,
    Branch,
)
# Pending manager
class PendingManager(models.Manager):

    def create(self, branch, **kwargs):

        instance = self.model()

        instance.account = kwargs.get('account', None)

        instance.ref_no = kwargs.get('ref_no', None)

        instance.bill_amount = kwargs.get('bill_amount', None)

        instance.adjusted = kwargs.get('adjusted', 0)

        instance.branch = branch

        instance.adj_id = kwargs.get('adj_id', None)

        instance.save()

        return instance

    @staticmethod
    def update(inst, **kwargs):

        instance = inst

        instance.account = kwargs.get('account', None)

        bill_amount = kwargs.get('bill_amount', None)

        if bill_amount is None:

            instance.adjusted = instance.adjusted + kwargs.get('adjusted', None)

        else:

            instance.bill_amount = bill_amount

        instance.adj_id = kwargs.get('adj_id', None)

        instance.save()

        return instance


# Pending
class Pending(models.Model):

    account = models.ForeignKey(Account, related_name='pending_account', blank=True, null=True)

    ref_no = models.CharField(max_length=40, null=True, blank=True)

    bill_amount = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)

    adjusted = models.DecimalField(max_digits=20, decimal_places=2)

    adj_id = models.IntegerField()

    branch = models.ForeignKey(Branch, related_name='pending_branch', blank=True, null=True)

    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)

    updated = models.DateTimeField(auto_now=True, auto_now_add=False)

    objects = PendingManager()

    class Meta:
        db_table = 'tbl_acc_pending'
        ordering = ["-timestamp", "-updated"]

    def __unicode__(self):
        return str(self.id)

    def __str__(self):
        return str(self.id)
