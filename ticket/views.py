from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from ticket.models import Ticket


class TicketList(ListView):
    model = Ticket
    queryset = Ticket.objects.all()
    paginate_by = 10
    context_object_name = 'tickets'
    template_name = 'ticket/ticketList.html'


class ticketDetails(DetailView):
    model = Ticket
    template_name = 'ticket/ticketDetails.html'


class addTicket(CreateView):
    model = Ticket
    fields = '__all__'
    template_name = 'ticket/addTicket.html'
