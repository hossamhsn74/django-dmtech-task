from django.urls import path, include
from .views import signUpView
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('signup/', signUpView.as_view(), name="signup"),
    path('login/', auth_views.LoginView.as_view(template_name='registrations/login.html'), name="login"),
    path('logout/', auth_views.LogoutView.as_view(
        template_name='registrations/logout.html'), name="logout"),
]
