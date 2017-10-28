from django.db import models

from django.contrib.auth.models import User

from bmcore import utils

from bmcore.models.salt import Salt


# Composition Manager
class CompositionManager(models.Manager):

    def create(self, name, salts, created_by):

        instance = self.model()

        instance.name = name.upper()

        instance.val_name = utils.gen_val_str(instance.name)

        instance.created_by = created_by

        instance.save()

        for item in salts:

            instance.salt.add(item)

        return instance

    @staticmethod
    def update(inst, name, salts, created_by):

        instance = inst

        instance.name = name.upper()

        instance.val_name = utils.gen_val_str(instance.name)

        instance.created_by = created_by

        instance.save()

        for item in salts:

            instance.salt.add(item)

        return instance


# Composition
class Composition(models.Model):

    name = models.CharField(max_length=500)

    val_name = models.CharField(max_length=500, blank=True, null=True)

    salt = models.ManyToManyField(Salt, blank=True)

    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)

    updated = models.DateTimeField(auto_now=True, auto_now_add=False)

    created_by = models.ForeignKey(User, default=1)

    objects = CompositionManager()

    class Meta:
        db_table = 'tbl_composition'
        ordering = ["-timestamp", "-updated"]

    def __unicode__(self):
        return str(self.name)

    def __str__(self):
        return str(self.name)
