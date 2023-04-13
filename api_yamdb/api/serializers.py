from rest_framework.validators import UniqueValidator
from django.shortcuts import get_object_or_404

from ..reviews.models import User
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True, max_length=254,
        validators=[UniqueValidator(queryset=User.objects.all(),
                                    message='this email is already taken')])
    username = serializers.RegexField(
        required=True, max_length=150, regex=r'^[\w.@+-]+$',
        validators=[UniqueValidator(queryset=User.objects.all(),
                                    message='this username is already taken')])

    class Meta:
        model = User
        fields = ['username', 'email', 'bio',
                  'first_name', 'last_name', 'role']


class UserProfileSerializer(UserSerializer):
    role = serializers.CharField(read_only=True)


class UsernameSerializer(serializers.Serializer):
    username = serializers.RegexField(
        required=True, max_length=150, regex=r'^[\w.@+-]+$')

    def validate_username(self, value):
        if value.lower() == 'me':
            raise serializers.ValidationError(f'{value} - not allowed username')
        return value


class SignUpSerializer(UsernameSerializer):
    email = serializers.EmailField(required=True, max_length=254)


class TokenSerializer(UsernameSerializer):
    confirmation_code = serializers.CharField(required=True)

    def validate(self, data):
        user = get_object_or_404(User, username=data['username'])
        data['user'] = user
        if user.confirmation_code == data['confirmation_code']:
            return data
        raise serializers.ValidationError('Wrong Code')
