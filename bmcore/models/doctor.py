from django.db import models

from django.contrib.auth.models import User

from bmcore import utils


# Doctor manager
class DoctorManager(models.Manager):

    def create(self, name, created_by, **kwargs):

        instance = self.model()

        instance.name = name.upper()

        instance.val_name = utils.gen_val_str(instance.name)

        instance.alias_name = kwargs.get('alias_name', None)

        instance.created_by = created_by

        instance.save()

        return instance

    @staticmethod
    def update(inst, name, created_by, **kwargs):

        instance = inst

        instance.name = name.upper()

        instance.val_name = utils.gen_val_str(instance.name)

        instance.alias_name = kwargs.get('alias_name', None)

        instance.created_by = created_by

        instance.save()

        return instance


# Doctor
class Doctor(models.Model):

    name = models.CharField(max_length=55, blank=True, null=True)

    val_name = models.CharField(max_length=55, blank=True, null=True)

    alias_name = models.CharField(max_length=55, blank=True, null=True)

    register_no = models.CharField(max_length=55, blank=True, null=True)

    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)

    updated = models.DateTimeField(auto_now=True, auto_now_add=False)

    created_by = models.ForeignKey(User, default=1)

    objects = DoctorManager()

    class Meta:
        db_table = 'tbl_doctor'
        ordering = ["-timestamp", "-updated"]

    def __unicode__(self):
        return str(self.name)

    def __str__(self):
        return str(self.name)
