from django.db import transaction

from bmcore.models import AccountGroup

from bmcore.utils import gen_val_str


# Account group service
class AccountGroupService(object):

    model = AccountGroup

    def check_account_group_exists(self, account_group_id=None, account_group_name=None):

        _if_exists_text = 'Account group already exists'

        _val_name = gen_val_str(account_group_name)

        # Validate with account-group name where id does not exists
        if account_group_id is None and account_group_name is not None:

            account_group_exists = self.model.objects.filter(val_name=_val_name).exists()

            if account_group_exists:

                return {'status': True, 'message': _if_exists_text}

            return {'status': False}

        # Validate with account-group id and name
        elif account_group_id is not None and account_group_name is not None:

            account_group_exists = self.model.objects.exclude(pk=account_group_id).filter(val_name=_val_name).exists()

            if account_group_exists:

                return {'status': True, 'message': _if_exists_text}

            return {'status': False}

        return ValueError('Cannot check for account group existence when account group id and name is none')

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
