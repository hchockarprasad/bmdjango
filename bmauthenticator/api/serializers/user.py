from django.contrib.auth.models import User

from django.db import transaction

from rest_framework import serializers, validators

from rest_framework_jwt.settings import api_settings

from bmcore.models import UserProfile

from bmauthenticator.services.user import UserService

jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER

jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

# Add your User serializers here


# User Registration Serializer
class UserRegisterSerializer(serializers.ModelSerializer):

    token = serializers.CharField(allow_blank=True, read_only=True)

    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password',
            'token'
        ]
        extra_kwargs = {"password": {"write_only": True}}

    def validate(self, data):

        user_service = UserService()

        if user_service.check_user_exists(data['username']):

            return validators.ValidationError('This user is already registered.')

        return data

    def create(self, validated_data):

        with transaction.atomic():

            user_service = UserService()

            user = user_service.register(
                validated_data['username'],
                validated_data.get('email', None),
                validated_data['password']
            )

            UserProfile.objects.create(user)

            payload = jwt_payload_handler(user)

            token = jwt_encode_handler(payload)

            validated_data['token'] = token

            return validated_data


# User Login Serializer
class UserLoginSerializer(serializers.ModelSerializer):

    id = serializers.IntegerField(required=False, allow_null=True)

    token = serializers.CharField(allow_blank=True, read_only=True)

    username = serializers.CharField()

    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'password',
            'token',
        ]

    def validate(self, data):

        username = data['username']

        password = data['password']

        user_service = UserService()

        login = user_service.login(username, password)

        if login['status'] is True:

            data['username'] = login['data'].username

            data['id'] = login['data'].id

            payload = jwt_payload_handler(login['data'])

            token = jwt_encode_handler(payload)

            data['token'] = token

            return data

        raise validators.ValidationError(login['message'])


# User Update Serializer
class UserUpdateSerializer(serializers.ModelSerializer):

    phone = serializers.CharField(write_only=True, required=False)

    sex = serializers.CharField(write_only=True, required=False)

    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',
            'email',
            'phone',
            'sex'
        ]

    def validate(self, data):

        return data

    def update(self, instance, validated_data):

        user_service = UserService()

        return user_service.update(instance, **validated_data)
