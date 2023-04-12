from rest_framework.routers import DefaultRouter
from django.urls import include, path

# from .views import ...

router = DefaultRouter()

urlpatterns = [
    path('v1/', include(router.urls)),
    path('v1/auth/signup/', ..., name='register'),
    path('v1/auth/token/', ..., name='token'),
]
