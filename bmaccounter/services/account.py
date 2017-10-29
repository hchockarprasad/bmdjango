from django.db import transaction

from bmcore.models import Account, FlaggedAccount

from bmcore.utils import gen_val_str


# Account service
class AccountService(object):

    model = Account

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

            return self.model.objects.create(**kwargs)

    def update(self, inst, **kwargs):

        name = kwargs.get('name', None)

        group = kwargs.get('group', None)

        bwd = kwargs.get('bwd', None)

        created_by = kwargs.get('created_by', None)

        if name is None or group is None or bwd is None or created_by is None:

            raise ValueError('Required parameters are not fulfilled')

        with transaction.atomic():

            return self.model.objects.update(inst, name, group, bwd, created_by, **kwargs)
