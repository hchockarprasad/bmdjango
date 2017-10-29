from rest_framework import (
    views,
    response,
    status
)

from bmaccounter.api.serializers import (
    account as account_serializer
)

from bmcore.models import Account

from bmcore import utils

from bmauthenticator.services.user import UserService

from bmaccounter.services.account import AccountService

# Add Account views here


class AccountListAPIView(views.APIView):
    """
    List accounts.
    """

    @staticmethod
    def get(request):

        method = request.GET.get('method')

        name = request.GET.get('name')

        group = request.GET.get('group')

        accounts = Account.objects.all()

        if name:

            accounts = accounts.filter(val_name__istartswith=name)

        if group:

            accounts = accounts.filter(group=group)

        if method is None:

            user_service = UserService(request.user)

            if user_service.has_menu_permission('Account List'):

                serializer = account_serializer.AccountOutwardSerializer(
                    accounts,
                    many=True,
                    fields=('id', 'name'),
                )

                return response.Response(serializer.data)

            return response.Response(status=status.HTTP_401_UNAUTHORIZED)

        elif method == 'common':

            serializer = account_serializer.AccountOutwardSerializer(
                accounts,
                fields=('id', 'name', 'bwd'),
                many=True
            )

            return response.Response(serializer.data)

        elif method == 'current_user':

            accounts = accounts.filter(
                name='Cash on ' + str(request.user.username)
            )

            if name:

                accounts = accounts.filter(name__istartswith=name)

            serializer = account_serializer.AccountOutwardSerializer(
                accounts,
                many=True,
                fields=('id', 'name'),
            )

            return response.Response(serializer.data)

        elif method == 'check_account_name_exists':

            account_id = request.GET.get('id')

            if name:

                val_name = utils.gen_val_str(name)

                accounts = accounts.filter(val_name=val_name)

                if account_id:

                    accounts = accounts.exclude(id=account_id)

                result = accounts.exists()

                return response.Response({'status': result})

            return response.Response({'status': False})

        elif method == 'check_account_alias_name_exists':

            account_id = request.GET.get('id')

            if name:

                queryset = accounts.filter(alias_name=name.lower())

                if account_id:

                    queryset = queryset.exclude(id=account_id)

                result = queryset.exists()

                return response.Response({'status': result})

            return response.Response({'status': False})

        return response.Response(status=status.HTTP_400_BAD_REQUEST)


class AccountCreateAPIView(views.APIView):
    """
    Create account.
    """

    @staticmethod
    def post(request):

        user_service = UserService(request.user)

        if user_service.has_menu_permission('Account Create'):

            request.data['created_by'] = request.user.id

            serializer = account_serializer.AccountInwardSerializer(
                data=request.data
            )
            if serializer.is_valid():

                serializer.save()

                return response.Response(serializer.data, status=status.HTTP_201_CREATED)

            print(serializer.errors)

            return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        return response.Response(status=status.HTTP_401_UNAUTHORIZED)


class AccountUpdateAPIView(views.APIView):
    """
    Update account.
    """

    @staticmethod
    def put(request, pk):
        user_service = UserService(request.user)

        if user_service.has_menu_permission('Account Update'):

            request.data['created_by'] = request.user.id

            account = Account.objects.get(pk=pk)

            serializer = account_serializer.AccountInwardSerializer(
                account,
                data=request.data
            )

            if serializer.is_valid():

                serializer.save()

                return response.Response(serializer.data)

            return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        return response.Response(status=status.HTTP_401_UNAUTHORIZED)


class AccountDetailAPIView(views.APIView):
    """
    Detail account
    """

    @staticmethod
    def get(request, pk):

        user_service = UserService(request.user)

        if user_service.has_menu_permission('Account Detail'):

            account = Account.objects.get(pk=pk)

            serializer = account_serializer.AccountOutwardSerializer(
                account
            )

            return response.Response(serializer.data)

        return response.Response(status=status.HTTP_401_UNAUTHORIZED)


class AccountDeleteAPIView(views.APIView):
    """
    Delete account
    """

    @staticmethod
    def delete(request, pk):
        user_service = UserService(request.user)

        if user_service.has_menu_permission('Account Delete'):

            account = Account.objects.get(pk=pk)

            account.delete()

            return response.Response(status=status.HTTP_204_NO_CONTENT)

        return response.Response(status=status.HTTP_401_UNAUTHORIZED)


class FlaggedAccountListAPIView(views.APIView):
    """
    List Flagged Accounts
    """

    @staticmethod
    def get(request):

        name = request.GET.get('name')

        voucher_type = request.GET.get('voucher_type')

        if voucher_type:

            account_service = AccountService()

            flagged_accounts = account_service.get_flagged_account(voucher_type, name=name)

            serializer = account_serializer.FlaggedAccountSerializer(
                flagged_accounts,
                many=True
            )

            return response.Response(serializer.data, status=status.HTTP_200_OK)

        return response.Response(status=status.HTTP_400_BAD_REQUEST)
