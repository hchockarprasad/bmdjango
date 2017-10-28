from django.db import models

from bmcore.models import (
    Branch,
    Inventory,
    Pack,
)


# Batch Manager
class BatchManager(models.Manager):

    def create(self, pack, branch, **kwargs):

        instance = self.model()

        instance.name = kwargs.get('name', None)

        instance.inventory = kwargs.get('inventory', None)

        instance.pack = pack

        instance.pack_conv = instance.pack.conversion

        instance.exp_month = kwargs.get('exp_month', None)

        instance.exp_year = kwargs.get('exp_year', None)

        instance.debit = kwargs.get('debit', None)

        instance.credit = 0

        instance.stock = instance.debit - instance.credit

        instance.mrp = kwargs.get('mrp', None)

        instance.branch = branch

        instance.p_rate = kwargs.get('p_rate', None)

        instance.p_cost = kwargs.get('p_cost', None)

        instance.save()

        return instance

    @staticmethod
    def update(inst, validated_data):

        instance = inst

        debit = validated_data.get('debit', None)

        credit = validated_data.get('credit', None)

        if debit:

            instance.debit = instance.debit + debit

        elif credit:

            instance.credit = instance.credit + credit

        instance.stock = instance.debit - instance.credit

        instance.s_rate = validated_data.get('s_rate', None)

        instance.s_cost = validated_data.get('s_cost', None)

        instance.save()

        return instance

    @staticmethod
    def update_func2(inst, **kwargs):

        instance = inst

        instance.name = kwargs.get('name', None)

        instance.inventory = kwargs.get('inventory', None)

        instance.pack = kwargs.get('pack', None)

        instance.exp_month = kwargs.get('exp_month', None)

        instance.exp_year = kwargs.get('exp_year', None)

        instance.debit = instance.debit + kwargs.get('debit', None)

        instance.stock = instance.debit - instance.credit

        instance.mrp = kwargs.get('mrp', None)

        instance.p_rate = kwargs.get('p_rate', None)

        instance.p_cost = kwargs.get('p_cost', None)

        instance.save()

        return instance

    @staticmethod
    def update_func3(inst, **kwargs):

        instance = inst

        instance.name = kwargs.get('name', None)

        instance.inventory = kwargs.get('inventory', None)

        instance.pack = kwargs.get('pack', None)

        instance.exp_month = kwargs.get('exp_month', None)

        instance.exp_year = kwargs.get('exp_year', None)

        instance.debit = kwargs.get('debit', None)

        instance.stock = instance.debit - instance.credit

        instance.mrp = kwargs.get('mrp', None)

        instance.p_rate = kwargs.get('p_rate', None)

        instance.p_cost = kwargs.get('p_cost', None)

        instance.save()

        return instance


# Batch
class Batch(models.Model):

    name = models.CharField(max_length=55, blank=True, null=True)

    bwd = models.BooleanField(default=True)

    inventory = models.ForeignKey(Inventory, blank=True, null=True)

    pack = models.ForeignKey(Pack, blank=True, null=True)

    pack_conv = models.IntegerField(blank=True, null=True)

    exp_month = models.IntegerField(blank=True, null=True)

    exp_year = models.IntegerField(blank=True, null=True)

    debit = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)

    credit = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)

    stock = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)

    mrp = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)

    p_rate = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)

    p_cost = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)

    s_rate = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)

    s_cost = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)

    tran = models.CharField(max_length=10)

    branch = models.ForeignKey(Branch, related_name='batch_branch', blank=True, null=True)

    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)

    updated = models.DateTimeField(auto_now=True, auto_now_add=False)

    objects = BatchManager()

    class Meta:
        db_table = 'tbl_batch'
        ordering = ["-timestamp", "-updated"]

    def __unicode__(self):
        return str(self.name)

    def __str__(self):
        return str(self.name)


# Sale Batch Display
class SaleBatchDisplay(models.Model):

    batch_id = models.IntegerField()

    batch_name = models.CharField(max_length=45)

    exp_month = models.IntegerField()

    exp_year = models.IntegerField()

    stock = models.IntegerField()

    mrp = models.DecimalField(max_digits=20, decimal_places=2)

    s_disc = models.DecimalField(max_digits=20, decimal_places=2)

    inventory_id = models.IntegerField()

    inventory_name = models.CharField(max_length=100)

    bwd = models.BooleanField()

    tax_id = models.IntegerField()

    tax_name = models.CharField(max_length=45)

    tax_sgst_ratio = models.DecimalField(max_digits=20, decimal_places=2)

    tax_cgst_ratio = models.DecimalField(max_digits=20, decimal_places=2)

    tax_igst_ratio = models.DecimalField(max_digits=20, decimal_places=2)

    rack_id = models.IntegerField()

    rack_name = models.CharField(max_length=10)

    pack_id = models.IntegerField()

    pack_name = models.CharField(max_length=10)

    pack_conv = models.IntegerField()

    class Meta:
        managed = False
