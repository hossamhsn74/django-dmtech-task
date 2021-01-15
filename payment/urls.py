from django.urls import path

from . import views

urlpatterns = [
    path('<int:pk>/', views.HomePageView.as_view(), name='pay'),
    path('charge/', views.charge, name='charge'),
    path('config/', views.stripe_config, name='config'),
    path('create-checkout-session/', views.create_checkout_session),  # new

]
