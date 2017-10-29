from django.db import models

from django.contrib.auth.models import User

from bmcore import utils

from bmcore.models.account_group import AccountGroup


# Account manager
class AccountManager(models.Manager):

    def create(self, **kwargs):

        instance = self.model()

        instance.name = kwargs.get('name').upper()

        instance.val_name = utils.gen_val_str(instance.name)

        instance.alias_name = kwargs.get('alias_name', None)

        instance.print_name = kwargs.get('print_name', None)

        instance.group = kwargs.get('group')

        instance.bwd = kwargs.get('bwd')

        instance.door = kwargs.get('door', None)

        instance.street = kwargs.get('street', None)

        instance.station = kwargs.get('station', None)

        instance.district = kwargs.get('district', None)

        instance.state = kwargs.get('state', None)

        instance.telephone = kwargs.get('telephone', None)

        instance.mobile = kwargs.get('mobile', None)

        instance.fax = kwargs.get('fax', None)

        instance.email = kwargs.get('email', None)

        instance.it_pan = kwargs.get('it_pan', None)

        instance.gst_no = kwargs.get('gst_no', None)

        instance.cst_no = kwargs.get('cst_no', None)

        instance.tin_no = kwargs.get('tin_no', None)

        instance.is_default = kwargs.get('is_default', False)

        instance.created_by = kwargs.get('created_by')

        instance.save()

        return instance

    @staticmethod
    def update(inst, **kwargs):

        instance = inst

        instance.name = kwargs.get('name').upper()

        instance.val_name = utils.gen_val_str(instance.name)

        instance.alias_name = kwargs.get('alias_name', None)

        instance.print_name = kwargs.get('print_name', None)

        instance.group = kwargs.get('group')

        instance.bwd = kwargs.get('bwd')

        instance.door = kwargs.get('door', None)

        instance.street = kwargs.get('street', None)

        instance.station = kwargs.get('station', None)

        instance.district = kwargs.get('district', None)

        instance.state = kwargs.get('state', None)

        instance.telephone = kwargs.get('telephone', None)

        instance.mobile = kwargs.get('mobile', None)

        instance.fax = kwargs.get('fax', None)

        instance.email = kwargs.get('email', None)

        instance.it_pan = kwargs.get('it_pan', None)

        instance.gst_no = kwargs.get('gst_no', None)

        instance.cst_no = kwargs.get('cst_no', None)

        instance.tin_no = kwargs.get('tin_no', None)

        instance.is_default = kwargs.get('is_default', False)

        instance.created_by = kwargs.get('created_by')

        instance.save()

        return instance


# Account
class Account(models.Model):

    name = models.CharField(max_length=55)

    alias_name = models.CharField(max_length=55, blank=True, null=True)

    print_name = models.CharField(max_length=55, blank=True, null=True)

    val_name = models.CharField(max_length=55, blank=True, null=True)

    group = models.ForeignKey(AccountGroup, related_name="account_group")

    bwd = models.BooleanField()

    door = models.CharField(max_length=10, blank=True, null=True)

    street = models.CharField(max_length=100, blank=True, null=True)

    station = models.CharField(max_length=20, blank=True, null=True)

    district = models.CharField(max_length=15, blank=True, null=True)

    state = models.CharField(max_length=15, blank=True, null=True)

    telephone = models.CharField(max_length=15, blank=True, null=True)

    mobile = models.CharField(max_length=10, blank=True, null=True)

    fax = models.CharField(max_length=20, blank=True, null=True)

    email = models.EmailField(blank=True, null=True)

    it_pan = models.CharField(max_length=15, blank=True, null=True)

    gst_no = models.CharField(max_length=15, blank=True, null=True)

    cst_no = models.CharField(max_length=15, blank=True, null=True)

    tin_no = models.CharField(max_length=15, blank=True, null=True)

    is_default = models.BooleanField(default=False)

    default_name = models.CharField(max_length=55, blank=True, null=True)

    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)

    updated = models.DateTimeField(auto_now=True, auto_now_add=False)

    created_by = models.ForeignKey(User, default=1)

    objects = AccountManager()

    class Meta:
        db_table = 'tbl_acc'
        ordering = ["-timestamp", "-updated"]

    def __unicode__(self):
        return str(self.name)

    def __str__(self):
        return str(self.name)


class FlaggedAccount(models.Model):

    name = models.CharField(max_length=100, blank=True, null=True)

    bwd = models.BooleanField()

    class_flag = models.IntegerField()

    class Meta:
        managed = False


# Account Pending display
class PendingDisplay(models.Model):

    account_id = models.IntegerField()

    account_name = models.CharField(max_length=100)

    ref_no = models.CharField(max_length=40)

    bill_amount = models.DecimalField(max_digits=20, decimal_places=2)

    adjusted = models.DecimalField(max_digits=20, decimal_places=2)

    adj_id = models.IntegerField()

    branch_id = models.IntegerField()

    branch_name = models.CharField(max_length=100)

    class Meta:
        managed = False


# Account ledger for voucher
class VoucherLedger(models.Model):

    bwd = models.BooleanField()

    name = models.CharField(max_length=55)

    class_flag = models.IntegerField()

    class Meta:
        managed = False
