from django.contrib.auth.models import User

from rest_framework import (
    status,
    test,
)

from rest_framework_jwt.settings import api_settings

from bmcore.tests import utils

# Write account tests here


class AccountTests(test.APITestCase):

    def setUp(self):

        utils.load_initial_data()

        self.user = User.objects.get(pk=2)

    def test_create_account(self):
        """
        Ensure we can create a new account object
        """

        payload = api_settings.JWT_PAYLOAD_HANDLER(self.user)

        token = api_settings.JWT_ENCODE_HANDLER(payload)

        auth = 'JWT {0}'.format(token)

        url = '/acc/api/account/create/'

        data = {'name': 'VIJAY PHARMACEUTICALS', 'bwd': True, 'group': 24}

        response = self.client.post(url, data, format='json', HTTP_AUTHORIZATION=auth)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
