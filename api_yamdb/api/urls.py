from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, signup, get_token


v1_router = DefaultRouter()
v1_router.register('users', UserViewSet)

auth_urlpatterns = [
    path('signup/', signup, name='signup'),
    path('token/', get_token, name='token'),
]

urlpatterns = [
    path('v1/auth/', include(auth_urlpatterns)),
    path('v1/', include(v1_router.urls)),
]