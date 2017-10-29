from rest_framework import (
    serializers,
    validators,
)

from bmcore import generics

from bmcore.models import AccountGroup

from bmaccounter.services.account_group import AccountGroupService

# Add your AccountGroup here


class AccountGroupOutwardSerializer(generics.DynamicFieldsModelSerializer):

    group = generics.AccountGroupSerializer(
        fields=('id', 'name')
    )

    class Meta:
        model = AccountGroup
        fields = [
            'id',
            'name',
            'alias_name',
            'print_name',
            'group',
            'class_flag'
        ]


class AccountGroupInwardSerializer(serializers.ModelSerializer):

    id = serializers.IntegerField(required=False, allow_null=True)

    class Meta:
        model = AccountGroup
        fields = [
            'id',
            'name',
            'alias_name',
            'print_name',
            'group',
            'created_by',
        ]

    @staticmethod
    def validate_name(value):

        account_group_service = AccountGroupService()

        account_group_exists = account_group_service.check_account_group_exists(None, value)

        if account_group_exists['status'] is True:
            raise validators.ValidationError(account_group_exists['message'])

        return value

    def validate(self, data):

        if data.get('id', None) is not None:

            account_group_service = AccountGroupService()

            account_group_exists = account_group_service.check_account_group_exists(data['id'], data['name'])

            if account_group_exists['status'] is True:
                raise validators.ValidationError(account_group_exists['message'])

        return data

    def create(self, validated_data):

        account_group_service = AccountGroupService()

        return account_group_service.create(**validated_data)

    def update(self, instance, validated_data):

        account_group_service = AccountGroupService()

        return account_group_service.update(instance, **validated_data)
