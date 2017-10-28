from django.db import models

from django.contrib.auth.models import User

from bmcore.models.voucher_template import VoucherTemplate


# Voucher Model Manager
class VoucherModelManager(models.Manager):

    def create(self, name, prefix, suffix, voucher_type, voucher_template, created_by):

        instance = self.model()

        instance.name = name

        instance.prefix = prefix

        instance.suffix = suffix

        instance.voucher_type = voucher_type

        instance.voucher_template = voucher_template

        instance.created_by = created_by

        instance.save()

        return instance

    @staticmethod
    def update_vch_no(inst):

        instance = inst

        instance.vch_no = instance.vch_no + 1

        instance.save()

        return instance


# Voucher Model
class VoucherModel(models.Model):

    name = models.CharField(max_length=45)

    prefix = models.CharField(max_length=8, blank=True, null=True)

    suffix = models.CharField(max_length=8, blank=True, null=True)

    vch_no = models.IntegerField(blank=True, null=True)

    voucher_template = models.ForeignKey(VoucherTemplate, related_name='voucher_model_voucher_template')

    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)

    updated = models.DateTimeField(auto_now=True, auto_now_add=False)

    created_by = models.ForeignKey(User, default=1)

    objects = VoucherModelManager()

    class Meta:
        db_table = 'tbl_vch'
        ordering = ["-timestamp", "-updated"]

    def __unicode__(self):
        return str(self.name)

    def __str__(self):
        return str(self.name)
