from rest_framework import filters
from rest_framework.settings import api_settings

from reviews.models import Category
from .mixins import ListCreateDestroyViewSet
from .serializers import CategorySerializer
from .premissions import IsAdminOrReadOnly


class CategoryViewSet(ListCreateDestroyViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = (IsAdminOrReadOnly,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name',)
    lookup_field = 'slug'
    pagination_class = api_settings.DEFAULT_PAGINATION_CLASS
    print('pagination_class', pagination_class)
