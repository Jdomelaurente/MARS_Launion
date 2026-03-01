from django.urls import path
from .views import RegisterView, CustomTokenObtainPairView, FileRequestCreateView, FileRequestLookupView
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='auth_register'),
    path('login/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('requests/', FileRequestCreateView.as_view(), name='file_request_create'),
    path('requests/lookup/<str:code>/', FileRequestLookupView.as_view(), name='file_request_lookup'),
]
