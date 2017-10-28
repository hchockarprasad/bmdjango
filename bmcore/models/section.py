from django.db import models

from django.contrib.auth.models import User

from bmcore import utils


# Section Manager
class SectionManager(models.Manager):

    def create(self, name, created_by):

        instance = self.model()

        instance.name = name.upper()

        instance.val_name = utils.gen_val_str(instance.name)

        instance.created_by = created_by

        instance.save()

        return instance

    @staticmethod
    def update(inst, name, created_by):

        instance = inst

        instance.name = name.upper()

        instance.val_name = utils.gen_val_str(instance.name)

        instance.created_by = created_by

        instance.save()

        return instance


# Section
class Section(models.Model):

    name = models.CharField(max_length=20)

    val_name = models.CharField(max_length=20, blank=True, null=True)

    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)

    updated = models.DateTimeField(auto_now=True, auto_now_add=False)

    created_by = models.ForeignKey(User, default=1)

    objects = SectionManager()

    class Meta:
        db_table = 'tbl_section'
        ordering = ["-timestamp", "-updated"]

    def __unicode__(self):
        return str(self.name)

    def __str__(self):
        return str(self.name)
