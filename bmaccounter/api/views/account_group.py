from rest_framework import (
    views,
    response,
    status
)

from bmaccounter.api.serializers import (
    account_group as account_group_serializer
)

from bmcore.models import AccountGroup

from bmcore import utils

from bmauthenticator.services.user import UserService

# Add AccountGroup views here


class AccountGroupListAPIView(views.APIView):
    """
    List all account-groups.
    """

    @staticmethod
    def get(request):

        method = request.GET.get('method')

        name = request.GET.get('name')

        ldc = request.GET.get('ldc')

        class_flag = request.GET.get('class_flag')

        account_groups = AccountGroup.objects.all().exclude(val_name='primary')

        if method is None:

            user_service = UserService(request.user)

            if user_service.has_menu_permission('Account Group List'):

                if name:

                    account_groups = account_groups.filter(val_name__istartswith=name)

                if ldc == 'true':

                    account_groups = account_groups.filter(ldc=True)

                if class_flag == 'true':

                    account_groups = account_groups.filter(class_flag__gt=0)

                serializer = account_group_serializer.AccountGroupOutwardSerializer(
                    account_groups,
                    many=True,
                    fields=('id', 'name')
                )

                return response.Response(serializer.data)

            return response.Response(status=status.HTTP_401_UNAUTHORIZED)

        if method == 'common':

            if name:

                account_groups = account_groups.filter(val_name__istartswith=name)

            if ldc == 'true':

                account_groups = account_groups.filter(ldc=True)

            if class_flag == 'true':

                account_groups = account_groups.filter(class_flag__gt=0)

            serializer = account_group_serializer.AccountGroupOutwardSerializer(
                account_groups, fields=('id', 'name', 'class_flag'),
                many=True
            )

            return response.Response(serializer.data)

        elif method == 'check_account_group_exists':

            account_group_id = request.GET.get('id')

            if name:

                val_name = utils.gen_val_str(name)

                account_groups = account_groups.filter(val_name=val_name)

                if account_group_id:

                    account_groups = account_groups.exclude(id=account_group_id)

                result = account_groups.exists()

                return response.Response({'status': result})

            return response.Response({'status': False})

        return response.Response(status.HTTP_400_BAD_REQUEST)


class AccountGroupCreateAPIView(views.APIView):
    """
    Create account-group.
    """

    @staticmethod
    def post(request):

        user_service = UserService(request.user)

        if user_service.has_menu_permission('Account Group Create'):

            request.data['created_by'] = request.user.id

            serializer = account_group_serializer.AccountGroupInwardSerializer(
                data=request.data
            )

            if serializer.is_valid():

                serializer.save()

                return response.Response(serializer.data, status=status.HTTP_201_CREATED)

            return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        return response.Response(status=status.HTTP_401_UNAUTHORIZED)


class AccountGroupUpdateAPIView(views.APIView):
    """
    Update account-group.
    """

    @staticmethod
    def put(request, pk):

        user_service = UserService(request.user)

        if user_service.has_menu_permission('Account Group Update'):

            request.data['created_by'] = request.user.id

            account_groups = AccountGroup.objects.get(pk=pk)

            serializer = account_group_serializer.AccountGroupInwardSerializer(
                account_groups,
                data=request.data
            )

            if serializer.is_valid():

                serializer.save()

                return response.Response(serializer.data)

            return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        return response.Response(status=status.HTTP_401_UNAUTHORIZED)


class AccountGroupDetailAPIView(views.APIView):
    """
    Detail account-group
    """

    @staticmethod
    def get(request, pk):

        user_service = UserService(request.user)

        if user_service.has_menu_permission('Account Group Detail'):

            account_group = AccountGroup.objects.get(pk=pk)

            serializer = account_group_serializer.AccountGroupOutwardSerializer(
                account_group
            )

            return response.Response(serializer.data)

        return response.Response(status=status.HTTP_401_UNAUTHORIZED)


class AccountGroupDeleteAPIView(views.APIView):
    """
    Delete account-group
    """

    @staticmethod
    def delete(request, pk):

        user_service = UserService(request.user)

        if user_service.has_menu_permission('Account Group List'):

            account_groups = AccountGroup.objects.get(pk=pk)

            account_groups.delete()

            return response.Response(status=status.HTTP_204_NO_CONTENT)

        return response.Response(status=status.HTTP_401_UNAUTHORIZED)
