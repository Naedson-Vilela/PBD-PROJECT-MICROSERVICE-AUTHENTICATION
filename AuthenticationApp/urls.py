from django.urls import path
from .views import RegisterView, ServiceApiView, GroupApiView, PermissionApiView, TokenValidationView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView
)

urlpatterns = [
    path('api/register/', RegisterView.as_view(), name="sign_up"),
    path('api/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/login/validate/', TokenValidationView.as_view(), name='token_validate'),
    path('api/login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/service/', ServiceApiView.as_view(), name="service_list_create"),
    path('api/group/', GroupApiView.as_view(), name='group_list_create'),
    path('api/permission', PermissionApiView.as_view(), name='permission_list_create'),
]
