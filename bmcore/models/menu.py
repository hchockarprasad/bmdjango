from django.db import models

from django.contrib.auth.models import User


# Menu
class Menu(models.Model):

    name = models.CharField(max_length=50)

    component = models.CharField(max_length=50)

    method = models.CharField(max_length=20)

    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)

    updated = models.DateTimeField(auto_now=True, auto_now_add=False)

    created_by = models.ForeignKey(User, default=1)

    class Meta:
        db_table = 'tbl_menu'
        ordering = ["-timestamp", "-updated"]

    def __unicode__(self):
        return str(self.name)

    def __str__(self):
        return str(self.name)
