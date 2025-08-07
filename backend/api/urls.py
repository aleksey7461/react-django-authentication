from django.urls import path

from .views import get_notes, logout, register, is_authenticated, CustomTokenObtainPairView, CustomRefreshTokenView

urlpatterns = [
    path('token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', CustomRefreshTokenView.as_view(), name='token_refresh'),
    path('notes/', get_notes),
    path('logout/', logout),
    path('authenticated', is_authenticated),
    path('register/', register),
]
