from django.contrib.auth.models import AbstractUser
from django.db import models

from django.core.validators import MaxValueValidator, MinValueValidator


class User(AbstractUser):
    USER = 'user'
    MODERATOR = 'moderator'
    ADMIN = 'admin'
    ROLES = {
        (USER, 'user'),
        (MODERATOR, 'moderator'),
        (ADMIN, 'admin'),
    }
    username = models.CharField(
        verbose_name='Имя пользователя',
        max_length=150,
        null=True,
        unique=True,
    )
    email = models.EmailField(
        verbose_name='Электронная почта',
        unique=True,
    )
    role = models.CharField(
        verbose_name='Роль',
        max_length=50,
        choices=ROLES,
        default=USER,
    )
    bio = models.TextField(
        verbose_name='О себе',
        null=True,
        blank=True,
    )

    @property
    def is_moderator(self):
        return self.role == self.MODERATOR

    @property
    def is_admin(self):
        return self.role == self.ADMIN

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    class Meta:
        ordering = ['id']
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

        constraints = [
            models.CheckConstraint(
                check=~models.Q(username__iexact="me"),
                name="username_is_not_me"
            )
        ]


class Review(models.Model):
    """ Определение модели отзывов """
    #title = models.ForeignKey(
        #Title,
        #on_delete=models.CASCADE,
        #verbose_name='произведение'
    #)
    text = models.CharField(
        max_length=200,
        verbose_name='текст'
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='автор'
    )
    # встроенные валидаторы проверяют, что значения оценки от 1 до 10
    # в противном случае вызывается  ValidationError
    score = models.IntegerField(
        verbose_name='рейтинг',
        validators=(
        MinValueValidator(1),
        MaxValueValidator(10)
        )
    )
    pub_date = models.DateTimeField(
        verbose_name='дата публикации',
        auto_now_add=True,
    )

class Meta:
    default_related_name = 'reviews'
    verbose_name = 'отзыв'
    ordering = ('pub_date', )
    constraints = [
        models.UniqueConstraint(
        fields=('title', 'author', ),
        name='unique review'
        )
    ]


class Comment(models.Model):
    """ Определение модели комментариев """
    review = models.ForeignKey(
        Review,
        on_delete=models.CASCADE,
        verbose_name='отзыв'
    )
    text = models.CharField(
        max_length=200,
        verbose_name='текст'
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='автор'
    )
    pub_date = models.DateTimeField(
        verbose_name='дата публикации',
        auto_now_add=True,
    )

class Meta:
    default_related_name = 'сomments'
    verbose_name='комментарий'
    ordering = ('pub_date', )
