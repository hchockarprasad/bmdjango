from django.db import models

from django.contrib.auth.models import User

from bmcore.models import (
    Account,
    Inventory,
    Customer,
    Branch,
    Doctor,
)


# Voucher manager
class VoucherManager(models.Manager):

    def create(self, branch, created_by, **kwargs):

        instance = self.model()

        instance.trans_date = kwargs.get('trans_date', None)

        instance.value_date = kwargs.get('value_date', None)

        instance.voucher_model = kwargs.get('voucher_model', None)

        instance.voucher_type = kwargs.get('voucher_type', None)

        instance.ref_no = kwargs.get('ref_no', None)

        instance.op_account = kwargs.get('op_account', None)

        instance.op_inventory = kwargs.get('op_inventory', None)

        instance.account1 = kwargs.get('account1', None)

        instance.account2 = kwargs.get('account2', None)

        instance.rounded = kwargs.get('rounded', None)

        instance.discount = kwargs.get('discount', None)

        instance.narration = kwargs.get('narration', None)

        instance.cashier = kwargs.get('cashier', None)

        instance.customer = kwargs.get('customer', None)

        instance.doctor = kwargs.get('doctor', None)

        instance.tax_exempt = kwargs.get('tax_exempt', False)

        instance.branch = branch

        instance.status = kwargs.get('status', True)

        instance.created_by = created_by

        instance.voucher_no = kwargs.get('voucher_no', None)

        instance.save()

        instance.id = instance.pk

        return instance

    @staticmethod
    def update(inst, branch, created_by, **kwargs):

        instance = inst

        instance.ref_no = kwargs.get('ref_no', None)

        instance.op_account = kwargs.get('op_account', None)

        instance.op_inventory = kwargs.get('op_inventory', None)

        instance.account1 = kwargs.get('account1', None)

        instance.account2 = kwargs.get('account2', None)

        instance.rounded = kwargs.get('rounded', None)

        instance.discount = kwargs.get('discount', None)

        instance.narration = kwargs.get('narration', None)

        instance.cashier = kwargs.get('cashier', None)

        instance.tax_exempt = kwargs.get('tax_exempt', False)

        instance.branch = branch

        instance.status = kwargs.get('status', True)

        instance.created_by = created_by

        instance.voucher_no = kwargs.get('voucher_no', None)

        instance.save()

        return instance


# Voucher
class Voucher(models.Model):

    trans_date = models.DateField(blank=True, null=True)

    value_date = models.DateField(blank=True, null=True)

    account1 = models.ForeignKey(Account, related_name="voucher_account1", blank=True, null=True)

    account2 = models.ForeignKey(Account, related_name="voucher_account2", blank=True, null=True)

    rounded = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)

    discount = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)

    voucher_no = models.CharField(max_length=10, blank=True, null=True)

    voucher_type = models.CharField(max_length=30, blank=True, null=True)

    ref_no = models.CharField(max_length=10, blank=True, null=True)

    narration = models.CharField(max_length=100, blank=True, null=True)

    op_account = models.ForeignKey(Account, blank=True, null=True)

    op_inventory = models.ForeignKey(Inventory, blank=True, null=True)

    voucher_model = models.IntegerField(blank=True, null=True)

    tax_exempt = models.BooleanField(default=False)

    tran = models.CharField(max_length=50, blank=True, null=True)

    batch = models.CharField(max_length=50, blank=True, null=True)

    branch = models.ForeignKey(Branch, blank=True, null=True)

    cashier = models.ForeignKey(Account, related_name="voucher_cashier", blank=True, null=True)

    customer = models.ForeignKey(Customer, related_name="voucher_customer", blank=True, null=True)

    doctor = models.ForeignKey(Doctor, related_name="voucher_doctor", blank=True, null=True)

    status = models.BooleanField(default=True)

    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)

    updated = models.DateTimeField(auto_now=True, auto_now_add=False)

    created_by = models.ForeignKey(User, default=1)

    objects = VoucherManager()

    class Meta:
        db_table = 'tbl_voucher'
        ordering = ["-timestamp", "-updated"]

    def __unicode__(self):
        return str(self.voucher_no)

    def __str__(self):
        return str(self.voucher_no)
