from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from ticket.models import Ticket
import pyqrcode


class TicketList(ListView):
    model = Ticket
    queryset = Ticket.objects.all()
    paginate_by = 10
    context_object_name = 'tickets'
    template_name = 'ticket/ticketList.html'


class ticketDetails(DetailView):
    model = Ticket
    template_name = 'ticket/ticketDetails.html'

    # def get_context_data(self, **kwargs):
    #     context = super(ticketDetails, self).get_context_data(**kwargs)
    #     qr = pyqrcode.create(str(context))
    #     qr.png("test.png", scale=8)
    #     # context['qrCode'] = qr.png("test.png", scale=8)

    #     context['qrCode'] = qr.terminal(quiet_zone=1)
    #     return context


# class ticketQrDetails(DetailView):
#     model = TicketQrCode
#     template_name = 'ticket/QR.html'


class addTicket(CreateView):
    model = Ticket
    fields = '__all__'
    template_name = 'ticket/addTicket.html'
