from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from ticket.models import Ticket
import pyqrcode


class TicketList(ListView):
    model = Ticket
    paginate_by = 10
    context_object_name = 'tickets'
    template_name = 'ticket/ticketList.html'


class ticketDetails(DetailView):
    model = Ticket
    context_object_name = 'ticket'
    template_name = 'ticket/ticketDetails.html'


class addTicket(CreateView):
    model = Ticket
    fields = '__all__'
    template_name = 'ticket/addTicket.html'
