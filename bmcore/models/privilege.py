from django.db import models

from django.contrib.auth.models import User

from bmcore.models import (
    Menu,
    Role,
)


# Privilege
class Privilege(models.Model):

    menu = models.ForeignKey(Menu)

    access = models.BooleanField(default=False)

    from_days = models.IntegerField(blank=True, null=True)

    to_days = models.IntegerField(blank=True, null=True)

    role = models.ForeignKey(Role, related_name='role_privileges', blank=True, null=True)

    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)

    updated = models.DateTimeField(auto_now=True, auto_now_add=False)

    created_by = models.ForeignKey(User, default=1)

    class Meta:
        db_table = 'tbl_privilege'
        ordering = ["-timestamp", "-updated"]

    def __unicode__(self):
        return str(self.menu)

    def __str__(self):
        return str(self.menu)
