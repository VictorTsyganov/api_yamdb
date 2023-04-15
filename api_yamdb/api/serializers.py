from rest_framework import serializers
from reviews.models import User


class SignupSerializer(serializers.Serializer):
    """Сериализатор регистрации пользователя."""
    username = serializers.RegexField(
        regex=r'^[\w.@+-]',
        required=True,
        max_length=50
    )
    email = serializers.EmailField(required=True, max_length=50)

    class Meta:
        model = User
        fields = ('username', 'email',)

    def validate_username(self, value):
        """Проверка: username не равен me."""
        if value.lower() == "me":
            raise serializers.ValidationError(
                'Username "me" не разрешено.'
            )
        return value


class TokenSerializer(serializers.Serializer):
    """Сериализатор получения токена авторизации."""
    username = serializers.CharField(
        required=True
    )
    confirmation_code = serializers.CharField(required=True)


class UserSerializer(serializers.ModelSerializer):
    """Сериализатор модели пользователя"""
    username = serializers.RegexField(
        regex=r'^[\w.@+-]',
        required=True,
        max_length=50
    )

    def validate_username(self, value):
        if User.objects.filter(username=value).exists():
            raise serializers.ValidationError(
                'Пользователь с таким именем уже существует!')
        return value

    def validate_email(self, value):
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError(
                'Пользователь с таким email уже существует!')
        return value

    class Meta:
        model = User
        fields = (
            'username',
            'email',
            'first_name',
            'last_name',
            'bio',
            'role'
        )