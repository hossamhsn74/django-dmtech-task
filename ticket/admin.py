from django.contrib import admin
from ticket.models import Ticket


# class TicketAdmin(admin.ModelAdmin):
#     readonly_fields = ('code',)


admin.site.register(Ticket)
# admin.site.register(TicketQrCode)
