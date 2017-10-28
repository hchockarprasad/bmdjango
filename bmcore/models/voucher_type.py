from django.db import models

from django.contrib.auth.models import User


# Voucher Type Manager
class VoucherTypeManager(models.Manager):

    def create(self, name, created_by):

        instance = self.model()

        instance.name = name

        instance.created_by = created_by

        instance.save()

        return instance


# Voucher Type
class VoucherType(models.Model):

    name = models.CharField(max_length=45)

    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)

    updated = models.DateTimeField(auto_now=True, auto_now_add=False)

    created_by = models.ForeignKey(User, default=1)

    objects = VoucherTypeManager()

    class Meta:
        db_table = 'tbl_vch_type'
        ordering = ["-timestamp", "-updated"]

    def __unicode__(self):
        return str(self.name)

    def __str__(self):
        return str(self.name)
