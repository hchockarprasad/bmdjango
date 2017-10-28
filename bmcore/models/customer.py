from django.db import models

from django.contrib.auth.models import User

from bmcore import utils


# Customer manager
class CustomerManager(models.Manager):

    def create(self, name, alias_name, created_by, **kwargs):

        instance = self.model()

        instance.name = name.upper()

        instance.val_name = utils.gen_val_str(instance.name)

        instance.alias_name = alias_name.lower()

        instance.print_name = kwargs.get('print_name', None)

        instance.door = kwargs.get('door', None)

        instance.street = kwargs.get('street', None)

        instance.station = kwargs.get('station', None)

        instance.district = kwargs.get('district', None)

        instance.state = kwargs.get('state', None)

        instance.telephone = kwargs.get('telephone', None)

        instance.mobile = kwargs.get('mobile', None)

        instance.email = kwargs.get('email', None)

        instance.is_default = kwargs.get('is_default', False)

        instance.created_by = created_by

        instance.save()

        return instance

    @staticmethod
    def update(inst, name, alias_name, created_by, **kwargs):

        instance = inst

        instance.name = name.upper()

        instance.val_name = utils.gen_val_str(instance.name)

        instance.alias_name = alias_name.lower()

        instance.print_name = kwargs.get('print_name', None)

        instance.door = kwargs.get('door', None)

        instance.street = kwargs.get('street', None)

        instance.station = kwargs.get('station', None)

        instance.district = kwargs.get('district', None)

        instance.state = kwargs.get('state', None)

        instance.telephone = kwargs.get('telephone', None)

        instance.mobile = kwargs.get('mobile', None)

        instance.email = kwargs.get('email', None)

        instance.is_default = kwargs.get('is_default', False)

        instance.created_by = created_by

        instance.save()

        return instance


# Customer
class Customer(models.Model):

    name = models.CharField(max_length=55, blank=True, null=True)

    val_name = models.CharField(max_length=55, blank=True, null=True)

    alias_name = models.CharField(max_length=55, blank=True, null=True)

    print_name = models.CharField(max_length=55, blank=True, null=True)

    door = models.CharField(max_length=10, blank=True, null=True)

    street = models.CharField(max_length=100, blank=True, null=True)

    station = models.CharField(max_length=20, blank=True, null=True)

    district = models.CharField(max_length=15, blank=True, null=True)

    state = models.CharField(max_length=15, blank=True, null=True)

    telephone = models.CharField(max_length=15, blank=True, null=True)
    mobile = models.CharField(max_length=10, blank=True, null=True)

    email = models.EmailField(blank=True, null=True)

    inv_req = models.CharField(max_length=10, blank=True, null=True)

    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)

    updated = models.DateTimeField(auto_now=True, auto_now_add=False)

    created_by = models.ForeignKey(User, default=1)

    objects = CustomerManager()

    class Meta:
        db_table = 'tbl_customer'
        ordering = ["-timestamp", "-updated"]

    def __unicode__(self):
        return str(self.name)

    def __str__(self):
        return str(self.name)
