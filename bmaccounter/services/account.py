from django.db import transaction

from bmcore.models import Account, FlaggedAccount

from bmcore.utils import gen_val_str


# Account service
class AccountService(object):

    model = Account

    def check_account_exists(self, account_id=None, account_name=None):

        _if_exists_text = 'Account already exists'

        _val_name = gen_val_str(account_name)

        # Validate with account name where id does not exists
        if account_id is None and account_name is not None:

            account_exists = self.model.objects.filter(val_name=_val_name).exists()

            if account_exists:

                return {'status': True, 'message': _if_exists_text}

            return {'status': False}

        # Validate with account id and name
        elif account_id is not None and account_name is not None:

            account_exists = self.model.objects.exclude(pk=account_id).filter(val_name=_val_name).exists()

            if account_exists:

                return {'status': True, 'message': _if_exists_text}

            return {'status': False}

        return ValueError('Cannot check for account existence when account id and name is none')

    @staticmethod
    def get_flagged_account(voucher_type, **kwargs):

        name = kwargs.get('name', None)

        sql = "SELECT * FROM vw_{0}_vch WHERE name like '{1}%%'".format(voucher_type, name.upper())

        return FlaggedAccount.objects.raw(sql)

    def create(self, **kwargs):

        name = kwargs.get('name', None)

        group = kwargs.get('group', None)

        bwd = kwargs.get('bwd', None)

        created_by = kwargs.get('created_by', None)

        if name is None or group is None or bwd is None or created_by is None:

            raise ValueError('Required parameters are not fulfilled')

        with transaction.atomic():

            return self.model.objects.create(name, group, bwd, created_by, **kwargs)

    def update(self, inst, **kwargs):

        name = kwargs.get('name', None)

        group = kwargs.get('group', None)

        bwd = kwargs.get('bwd', None)

        created_by = kwargs.get('created_by', None)

        if name is None or group is None or bwd is None or created_by is None:

            raise ValueError('Required parameters are not fulfilled')

        with transaction.atomic():

            return self.model.objects.update(inst, name, group, bwd, created_by, **kwargs)
