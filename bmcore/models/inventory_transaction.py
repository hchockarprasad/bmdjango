from django.db import models

from bmcore.models.inventory import Inventory

from bmcore.models.batch import Batch

from bmcore.models.voucher import Voucher

from bmcore.models.tax import Tax

from bmcore.models.pack import Pack


# Inventory transaction manager
class InventoryTransactionManager(models.Manager):

    def create(self, voucher, batch, pack, **kwargs):

        instance = self.model()

        instance.batch = batch

        instance.inventory = kwargs.get('inventory', None)

        instance.exp_year = kwargs.get('exp_year', None)

        instance.exp_month = kwargs.get('exp_month', None)

        instance.pack = pack

        instance.pack_conv = instance.pack.conversion

        instance.voucher = voucher

        instance.qty = kwargs.get('qty', None)

        instance.free = kwargs.get('free', 0)

        instance.p_rate = kwargs.get('p_rate', 0)

        instance.p_cost = kwargs.get('p_cost', 0)

        instance.disc = kwargs.get('disc', 0)

        instance.tax = kwargs.get('tax', None)

        instance.amount = kwargs.get('amount', None)

        instance.mrp = kwargs.get('mrp', None)

        amount_value = kwargs.get('amount_value')

        instance.supp_profit_ratio = kwargs.get('supp_profit_ratio', None)

        instance.s_rate = kwargs.get('s_rate', 0)

        instance.s_cost = kwargs.get('s_cost', 0)

        instance.disc_value = kwargs.get('disc_value', None)

        instance.tax_value = kwargs.get('tax_value', None)

        instance.amount_value = amount_value

        instance.cl = kwargs.get('cl', True)

        instance.ol = kwargs.get('ol', True)

        instance.inward = kwargs.get('inward', 0)

        instance.outward = kwargs.get('outward', 0)

        instance.save()

        return instance

    @staticmethod
    def update(inst, voucher, batch, pack, **kwargs):

        instance = inst

        instance.batch = batch

        instance.inventory = kwargs.get('inventory', None)

        instance.exp_year = kwargs.get('exp_year', None)

        instance.exp_month = kwargs.get('exp_month', None)

        instance.pack = pack

        instance.pack_conv = instance.pack.conversion

        instance.voucher = voucher

        instance.qty = kwargs.get('qty', None)

        instance.free = kwargs.get('free', 0)

        instance.p_rate = kwargs.get('p_rate', 0)

        instance.p_cost = kwargs.get('p_cost', 0)

        instance.disc = kwargs.get('disc', 0)

        instance.tax = kwargs.get('tax', None)

        instance.amount = kwargs.get('amount', None)

        instance.mrp = kwargs.get('mrp', None)

        amount_value = kwargs.get('amount_value')

        instance.supp_profit_ratio = kwargs.get('supp_profit_ratio', None)

        instance.s_rate = kwargs.get('s_rate', 0)

        instance.s_cost = kwargs.get('s_cost', 0)

        instance.disc_value = kwargs.get('disc_value', None)

        instance.tax_value = kwargs.get('tax_value', None)

        instance.amount_value = amount_value

        instance.cl = kwargs.get('cl', True)

        instance.ol = kwargs.get('ol', True)

        instance.inward = kwargs.get('inward', 0)

        instance.outward = kwargs.get('outward', 0)

        instance.save()

        return instance


# Inventory transaction
class InventoryTransaction(models.Model):

    inventory = models.ForeignKey(Inventory, blank=True, null=True)

    batch = models.ForeignKey(Batch, related_name='inventory_transaction_batch', blank=True, null=True)

    voucher = models.ForeignKey(Voucher, related_name="inventory_transactions", blank=True, null=True)

    batch_value = models.CharField(max_length=20, blank=True, null=True)

    qty = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)

    free = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)

    p_rate = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)

    p_cost = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)

    supp_profit_ratio = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)

    disc = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)

    disc_value = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)

    mrp = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)

    s_rate = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)

    s_cost = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)

    tax = models.ForeignKey(Tax, blank=True, null=True)

    tax_value = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)

    amount = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)

    amount_value = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)

    cl = models.BooleanField(default=True)

    ol = models.BooleanField(default=False)

    inward = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)

    outward = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    pack = models.ForeignKey(Pack, blank=True, null=True)

    pack_conv = models.IntegerField(blank=True, null=True)

    exp_month = models.IntegerField(blank=True, null=True)

    exp_year = models.IntegerField(blank=True, null=True)

    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)

    updated = models.DateTimeField(auto_now=True, auto_now_add=False)

    objects = InventoryTransactionManager()

    class Meta:
        db_table = 'tbl_inv_tran'

    def __unicode__(self):
        return str(self.inventory)

    def __str__(self):
        return str(self.inventory)
