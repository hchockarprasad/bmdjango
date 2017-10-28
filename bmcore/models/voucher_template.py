from django.db import models

from django.contrib.auth.models import User

from bmcore.models import VoucherType


# Voucher Template Manager
class VoucherTemplateManager(models.Manager):

    def create(self, name, voucher_type, created_by):

        instance = self.model()

        instance.name = name

        instance.voucher_type = voucher_type

        instance.created_by = created_by

        instance.save()

        return instance


# Voucher Template
class VoucherTemplate(models.Model):

    name = models.CharField(max_length=45)

    voucher_type = models.ForeignKey(VoucherType)

    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)

    updated = models.DateTimeField(auto_now=True, auto_now_add=False)

    created_by = models.ForeignKey(User, default=1)

    objects = VoucherTemplateManager()

    class Meta:
        db_table = 'tbl_vch_tpl'
        ordering = ["-timestamp", "-updated"]

    def __unicode__(self):
        return str(self.name)

    def __str__(self):
        return str(self.name)
