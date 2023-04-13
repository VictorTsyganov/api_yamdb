from rest_framework.routers import DefaultRouter
from django.urls import include, path

from ..api.views import SignUpView, TokenCreateView

router = DefaultRouter()

urlpatterns = [
    path('v1/', include(router.urls)),
    path('v1/auth/signup/', SignUpView.as_view(), name='signup'),
    path('v1/auth/token/', TokenCreateView.as_view(), name='get_token'),
]
