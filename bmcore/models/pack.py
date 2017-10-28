from django.db import models

from django.contrib.auth.models import User

from bmcore import utils


# Pack Manager
class PackManager(models.Manager):

    def create(self, name, conversion, created_by):

        instance = self.model()

        instance.name = name

        instance.val_name = utils.gen_val_str(instance.name)

        instance.print_name = instance.name + "'s"

        instance.conversion = conversion

        instance.created_by = created_by

        instance.save()

        return instance

    @staticmethod
    def update(inst, name, conversion, created_by):

        instance = inst

        instance.name = name

        instance.val_name = utils.gen_val_str(instance.name)

        instance.print_name = instance.name + "'s"

        instance.conversion = conversion

        instance.created_by = created_by

        instance.save()

        return instance


# Pack
class Pack(models.Model):

    name = models.CharField(max_length=10, blank=True, null=True)

    val_name = models.CharField(max_length=10, blank=True, null=True)

    print_name = models.CharField(max_length=11, blank=True, null=True)

    conversion = models.IntegerField(blank=True, null=True)

    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)

    updated = models.DateTimeField(auto_now=True, auto_now_add=False)

    created_by = models.ForeignKey(User, default=1)

    objects = PackManager()

    class Meta:
        db_table = 'tbl_pack'
        ordering = ["-timestamp", "-updated"]

    def __unicode__(self):
        return str(self.name)

    def __str__(self):
        return str(self.name)
