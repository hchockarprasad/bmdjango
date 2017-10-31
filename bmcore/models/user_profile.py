from django.db import models

from django.contrib.auth.models import User

from django.db.models.signals import post_save

from django.dispatch import receiver

from bmcore.models.role import Role

from bmcore.models.account import Account

# Create your models here.


# User Profile Manager
class UserProfileManager(models.Manager):

    def create(self, user, **kwargs):

        instance = self.model()

        instance.user = user

        instance.phone = kwargs.get('phone', None)

        instance.sex = kwargs.get('sex', None)

        instance.save()

        return instance

    def update(self, user, **kwargs):

        instance = self.model.objects.get(user=user)

        instance.sex = kwargs.get('sex', None)

        instance.phone = kwargs.get('phone', None)

        instance.save()

    def verify(self, user):

        instance = self.model()

        instance.user = user

        instance.verified = True

        instance.save()


# User Profile model
class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    phone = models.CharField(max_length=15, blank=True, null=True)

    sex = models.NullBooleanField()

    verified = models.BooleanField(default=False)

    role = models.ForeignKey(Role, blank=True, null=True)

    is_cashier = models.BooleanField(default=False)

    cash_account = models.ForeignKey(Account, blank=True, null=True)

    objects = UserProfileManager()

    def __str__(self):
        return self.user.name

    class Meta:

        db_table = 'tbl_user_profile'

        managed = True


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):

    if created is True and kwargs.get('raw') is False:

        UserProfile.objects.update_or_create(user=instance)
