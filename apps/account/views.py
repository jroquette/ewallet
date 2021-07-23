"""Views of Account"""
from rest_framework.viewsets import ModelViewSet
from rest_framework import status, views
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.permissions import AllowAny

from apps.account.models import Account
from apps.account.serializers import RegistrationSerializer, AccountSerializer


class AccountViewSet(ModelViewSet):
    """View of Account"""
    queryset = Account.objects.all()
    serializer_class = AccountSerializer


class RegistrationView(views.APIView):
    """View of Registration"""
    permission_classes = []
    authentication_classes = []

    def post(self, request):
        """
        Post request to registration a new account

        :param request: Fields of RegistrationSerializer
        :return: json with data
        """
        serializer = RegistrationSerializer(data=request.data)
        valid = serializer.is_valid(raise_exception=True)
        data = {}
        if valid:
            account = serializer.save()
            data['response'] = 'successfully registered a new user'
            data['username'] = account.username
            data['email'] = account.email
            data['token'] = Token.objects.get(user=account).key
        else:
            data = serializer.errors
            return Response(data, status=status.HTTP_412_PRECONDITION_FAILED)
        return Response(data, status=status.HTTP_201_CREATED)


