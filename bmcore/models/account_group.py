from django.db import models

from django.contrib.auth.models import User

from bmcore import utils


# Account group manager
class AccountGroupManager(models.Manager):

    def create(self, name, created_by, **kwargs):

        instance = self.model()

        instance.name = name.upper()

        instance.val_name = utils.gen_val_str(instance.name)

        instance.alias_name = kwargs.get('alias_name', None)

        instance.print_name = kwargs.get('print_name', None)

        instance.group = kwargs.get('group', None)

        instance.class_flag = instance.group.class_flag

        instance.created_by = created_by

        instance.save()

        return instance

    @staticmethod
    def update(inst, name, created_by, **kwargs):

        instance = inst

        instance.name = name.upper()

        instance.val_name = utils.gen_val_str(instance.name)

        instance.alias_name = kwargs.get('alias_name', None)

        instance.print_name = kwargs.get('print_name', None)

        instance.group = kwargs.get('group', None)

        instance.class_flag = instance.group.class_flag

        instance.created_by = created_by

        instance.save()

        return instance


# Account Group model
class AccountGroup(models.Model):

    name = models.CharField(max_length=55)

    val_name = models.CharField(max_length=55, blank=True, null=True)

    alias_name = models.CharField(max_length=55, blank=True, null=True)

    print_name = models.CharField(max_length=55, blank=True, null=True)

    group = models.ForeignKey('self', blank=True, null=True)

    is_default = models.BooleanField(default=False)

    ldc = models.BooleanField(default=False)

    class_flag = models.IntegerField(blank=True, null=True)

    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)

    updated = models.DateTimeField(auto_now=True, auto_now_add=False)

    created_by = models.ForeignKey(User, default=1)

    objects = AccountGroupManager()

    class Meta:
        db_table = 'tbl_acc_group'

        ordering = ["-timestamp", "-updated"]

    def __unicode__(self):

        return str(self.name)

    def __str__(self):

        return str(self.name)
