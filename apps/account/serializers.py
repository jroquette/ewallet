"""Serializer Account"""

from rest_framework import serializers
from apps.account.models import Account


class RegistrationSerializer(serializers.ModelSerializer):
    """Serializer Class of Account"""
    password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)

    class Meta:
        """Meta Class"""
        model = Account
        fields = ['email', 'username', 'password', 'password2']
        extra_kwargs = {'password': {'write_only': True}}

    def save(self, **kwargs):
        account = Account(username=self.validated_data['username'], email=self.validated_data['email'])
        password = self.validated_data['password']
        password2 = self.validated_data['password2']

        if password != password2:
            raise serializers.ValidationError("Passwords don't match.")
        account.set_password(password)
        account.save()
        return account


class AccountSerializer(serializers.ModelSerializer):
    """Serializer Class of Account"""

    class Meta:
        """Meta Class"""
        model = Account
        fields = ['email', 'username', 'last_login']
