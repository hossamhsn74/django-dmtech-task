from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from ticket.views import TicketList, ticketDetails, addTicket, scanTicket, errorView

urlpatterns = [   
    path('', TicketList.as_view(), name='ticketlist'),
    path('<int:pk>/', ticketDetails.as_view(), name='ticketdetails'),
    path('add/', addTicket.as_view(), name='addTicket'),
    path('scan/', scanTicket.as_view(), name='scanTicket'),
    path('error/', errorView.as_view(), name='errorView'),
]
