from django.urls import path, include
from .views import home_view, signup_view
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('signup/', signup_view, name="signup"),
    path('login/', auth_views.LoginView.as_view(template_name='registrations/login.html'), name="login"),
    path('logout/', auth_views.LogoutView.as_view(), name="logout"),
   
]
