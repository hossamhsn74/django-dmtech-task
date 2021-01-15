from django.shortcuts import render
from django.shortcuts import redirect
from users.models import CustomUser


def home_view(request):
    if not request.user.is_authenticated:
        return redirect('login')
    else:
        if request.user.user_type == "service provider":
            return redirect('ticketlist')
        else:
            return redirect('scanTicket')
        return redirect('login')
