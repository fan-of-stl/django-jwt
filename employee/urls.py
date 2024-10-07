from . import views
from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('register/', views.employee_registration, name='registration'),
    path('success/', views.success_page, name='success_page'),
    path('login/', views.login_view, name='login'),
    path('profile/<int:user_id>/', views.profile, name='profile'),
    path('error/', views.error_page, name='error_page'),
    path('company-registration/', views.company_registration, name='company_registration'),
    path('', views.home_page, name='home'),
    
    # JWT token management paths
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
