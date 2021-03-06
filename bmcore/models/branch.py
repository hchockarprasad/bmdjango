from django.db import models

from django.contrib.auth.models import User

from bmcore import utils


# Branch Manager
class BranchManager(models.Manager):

    def create(self, name, branch_type, created_by):

        instance = self.model()

        instance.name = name.upper()

        instance.val_name = utils.gen_val_str(instance.name)

        instance.branch_type = branch_type

        instance.created_by = created_by

        instance.save()

        return instance

    @staticmethod
    def update(inst, name, branch_type, created_by):

        instance = inst

        instance.name = name

        instance.val_name = utils.gen_val_str(instance.name)

        instance.branch_type = branch_type

        instance.created_by = created_by

        instance.save()

        return instance


# Branch
class Branch(models.Model):

    name = models.CharField(max_length=100)

    val_name = models.CharField(max_length=100, blank=True, null=True)

    is_default = models.BooleanField(default=False)

    branch_type = models.IntegerField()

    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)

    updated = models.DateTimeField(auto_now=True, auto_now_add=False)

    created_by = models.ForeignKey(User, default=1)

    objects = BranchManager()

    class Meta:
        db_table = 'tbl_branch'
        ordering = ["-timestamp", "-updated"]

    def __unicode__(self):
        return str(self.name)

    def __str__(self):
        return str(self.name)
