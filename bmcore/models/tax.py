from django.db import models

from django.contrib.auth.models import User

from bmcore import utils


# Tax Manager
class TaxManager(models.Manager):

    def create(self, name, tax_type, sgst_ratio, cgst_ratio, igst_ratio, created_by):

        instance = self.model()

        instance.name = name.upper()

        instance.val_name = utils.gen_val_str(instance.name)

        instance.tax_type = tax_type

        instance.sgst_ratio = sgst_ratio

        instance.cgst_ratio = cgst_ratio

        instance.igst_ratio = igst_ratio

        instance.created_by = created_by

        instance.save()

        return instance

    @staticmethod
    def update(inst, name, tax_type, sgst_ratio, cgst_ratio, igst_ratio, created_by):

        instance = inst

        instance.name = name.upper()

        instance.val_name = utils.gen_val_str(instance.name)

        instance.tax_type = tax_type

        instance.sgst_ratio = sgst_ratio

        instance.cgst_ratio = cgst_ratio

        instance.igst_ratio = igst_ratio

        instance.created_by = created_by

        instance.save()

        return instance


# Tax
class Tax(models.Model):

    name = models.CharField(max_length=40)

    val_name = models.CharField(max_length=40, blank=True, null=True)

    tax_type = models.CharField(max_length=40)

    sgst_ratio = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)

    cgst_ratio = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)

    igst_ratio = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)

    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)

    updated = models.DateTimeField(auto_now=True, auto_now_add=False)

    created_by = models.ForeignKey(User, default=1)

    objects = TaxManager()

    class Meta:
        db_table = 'tbl_tax'
        ordering = ["-timestamp", "-updated"]

    def __unicode__(self):
        return str(self.name)

    def __str__(self):
        return str(self.name)
