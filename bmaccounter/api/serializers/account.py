from rest_framework import (
    serializers,
    validators,
)

from bmcore import generics, utils

from bmcore.models import (
    Account,
    FlaggedAccount
)

from bmaccounter.services.account import AccountService


# Account Inward Serializer that serializes both create and update inputs
class AccountInwardSerializer(serializers.ModelSerializer):

    id = serializers.IntegerField(required=False, allow_null=True)

    class Meta:
        model = Account
        fields = [
            'id',
            'name',
            'alias_name',
            'print_name',
            'group',
            'bwd',
            'door',
            'street',
            'district',
            'station',
            'state',
            'telephone',
            'mobile',
            'fax',
            'email',
            'it_pan',
            'gst_no',
            'cst_no',
            'tin_no',
            'created_by'
        ]

    @staticmethod
    def validate_name(value):

        account_exists = utils.check_obj_exists(Account, None, **{'name': value})

        if account_exists['status'] is True:

            raise validators.ValidationError(account_exists['message'])

        return value

    def validate(self, data):

        if data.get('id', None) is not None:

            account_exists = utils.check_obj_exists(Account, data['id'], **{'name': data['name']})

            if account_exists['status'] is True:

                raise validators.ValidationError(account_exists['message'])

        return data

    def create(self, validated_data):

        account_service = AccountService()

        return account_service.create(**validated_data)

    def update(self, instance, validated_data):

        account_service = AccountService()

        return account_service.update(instance, **validated_data)


# Account outward serializer that serializes both list and detail outputs
class AccountOutwardSerializer(generics.DynamicFieldsModelSerializer):

    group = generics.AccountGroupSerializer(
        fields=('id', 'name')
    )

    class Meta:
        model = Account
        fields = [
            'id',
            'name',
            'alias_name',
            'print_name',
            'group',
            'bwd',
            'door',
            'street',
            'district',
            'station',
            'state',
            'telephone',
            'mobile',
            'fax',
            'email',
            'it_pan',
            'gst_no',
            'cst_no',
            'tin_no',
            'is_default'
        ]


class FlaggedAccountSerializer(generics.DynamicFieldsModelSerializer):

    class Meta:

        model = FlaggedAccount
        fields = [
            'id',
            'name',
            'bwd',
            'class_flag'
        ]
