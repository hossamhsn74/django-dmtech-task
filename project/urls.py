from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from .views import home_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view, name="home"),
    # path('registration/', include('users.urls'), name="users"),
    path('tickets/', include('ticket.urls'), name="tickets"),


    # all-auth urls
    # path('rest-auth/signup/', include('rest_auth.registration.urls')),
    # path('rest-auth/', include('rest_auth.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
