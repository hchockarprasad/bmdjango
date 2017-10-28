from django.db import models

from bmcore.models.account import Account

from bmcore.models.voucher import Voucher

from bmcore.models.branch import Branch


# Cashier cash display
class CashierCashDisplay(models.Model):
    cashier = models.ForeignKey(Account, related_name="cashsale_cashier")
    voucher = models.ForeignKey(Voucher, related_name="cashsale_voucher")
    branch = models.ForeignKey(Branch, related_name="cashsale_batch")
    checked = models.BooleanField(default=False)
    viewed = models.BooleanField(default=False)
    created_by = models.CharField(max_length=50, blank=True, null=True)
    voucher_no = models.CharField(max_length=10, blank=True, null=True)
    voucher_type = models.CharField(max_length=30, blank=True, null=True)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)

    class Meta:
        db_table = 'tbl_cashier_cash_display'
        ordering = ["-timestamp", "-updated"]


# Cashier cash display report
class CashierCashDisplayReport(models.Model):
    voucher_no = models.CharField(max_length=10, blank=True, null=True)
    voucher_type = models.CharField(max_length=30, blank=True, null=True)
    cashier_id = models.IntegerField()
    voucher_id = models.IntegerField()
    checked = models.BooleanField(default=False)
    viewed = models.BooleanField(default=False)
    amount = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    created_by = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
