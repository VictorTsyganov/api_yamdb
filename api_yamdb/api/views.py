from secrets import token_hex

from django.core.mail import send_mail
from django.db import IntegrityError
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.generics import RetrieveUpdateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework_simplejwt.tokens import AccessToken

from .permissions import AdminOnly
from ..api.serializers import (SignUpSerializer,
                               TokenSerializer,
                               UserProfileSerializer,
                               UserSerializer, )
from ..reviews.models import User


class SignUpView(APIView):
    """
    Отправить email с кодом подтверждения пользователю.
    Добавление пользователя в базу.
    """
    def post(self, request):
        serializer = SignUpSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        try:
            user, created = User.objects.get_or_create(
                username=serializer.validated_data['username'],
                email=serializer.validated_data['email']
            )
            user.confirmation_code = token_hex(16)
            user.save()
            self.send_code(user.email, user.confirmation_code)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except IntegrityError:
            return Response(
                data={'error:': 'Username or Email already taken'},
                status=status.HTTP_400_BAD_REQUEST)

    def send_code(self, email, code):
        subject = 'YaMDB Confirmation Code'
        message = f'Confirmation Code: {code}'
        from_email = 'YaMDB@email.com'
        send_mail(subject, message, from_email, [email, ], fail_silently=False)


class TokenCreateView(APIView):
    """
    Отправить JWT токен пользователю.
    """
    def post(self, request):
        serializer = TokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        token = AccessToken.for_user(serializer.validated_data['user'])
        return Response({'token': str(token)})


class UserViewSet(ModelViewSet):
    """
    Работа с моделью пользователей. Доступ: Админ.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AdminOnly, ]
    http_method_names = ['get', 'list', 'post', 'patch', 'delete', ]
    search_fields = ['username', ]
    lookup_field = 'username'

    @action(detail=False, permission_classes=[IsAuthenticated, ],
            methods=['get', 'patch'], serializer_class=UserProfileSerializer)
    def me(self, request):
        user = self.request.user
        if request.method == 'GET':
            serializer = self.get_serializer(user)
            return Response(serializer.data, status=status.HTTP_200_OK)
        serializer = self.get_serializer(user, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)


class UserProfileView(RetrieveUpdateAPIView):
    """
    Изменить данные пользователя. Доступ: Зарегистрированный пользователь.
    """
    queryset = User.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = [IsAuthenticated, ]

    def get_object(self):
        return self.request.user
