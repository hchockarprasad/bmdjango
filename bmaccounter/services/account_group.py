from django.db import transaction

from bmcore.models import AccountGroup


# Account group service
class AccountGroupService(object):

    model = AccountGroup

    def create(self, **kwargs):

        name = kwargs.get('name', None)

        group = kwargs.get('group', None)

        created_by = kwargs.get('created_by', None)

        if name is None or group is None or created_by is None:

            raise ValueError('Required parameters are not fulfilled')

        with transaction.atomic():

            return self.model.objects.create(**kwargs)

    def update(self, inst, **kwargs):

        name = kwargs.get('name', None)

        group = kwargs.get('group', None)

        created_by = kwargs.get('created_by', None)

        if name is None or group is None or created_by is None:

            raise ValueError('Required parameters are not fulfilled')

        with transaction.atomic():

            return self.model.objects.update(inst, **kwargs)
