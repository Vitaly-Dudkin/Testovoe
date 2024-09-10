from django.urls import path
from views.views import TokenObtainPairView, TokenRefreshView

from user.apps import UserConfig

app_name = UserConfig.name

urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
