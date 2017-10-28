from rest_framework import (
    views,
    response,
    permissions,
    status
)

from bmauthenticator.api.serializers.user import (
    UserRegisterSerializer,
    UserUpdateSerializer,
    UserLoginSerializer,
)


# Add your user api views here


# User Register APIView
class UserRegisterAPIView(views.APIView):

    permission_classes = [permissions.AllowAny]

    @staticmethod
    def post(request):

        data = request.data

        serializer = UserRegisterSerializer(data=data)

        if serializer.is_valid():

            serializer.save()

            return response.Response(serializer.data, status=status.HTTP_200_OK)

        return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# User Login APIView
class UserLoginAPIView(views.APIView):

    permission_classes = [permissions.AllowAny]

    @staticmethod
    def post(request):

        data = request.data

        serializer = UserLoginSerializer(data=data)

        if serializer.is_valid():

            return response.Response(serializer.data, status=status.HTTP_200_OK)

        return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# User Update APIView
class UserUpdateAPIView(views.APIView):

    @staticmethod
    def post(request):

        serializer = UserUpdateSerializer(request.user, data=request.data)

        if serializer.is_valid():

            serializer.save()

            return response.Response(serializer.data, status=status.HTTP_200_OK)

        return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
