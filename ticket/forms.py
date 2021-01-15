from ticket.models import Ticket
from django import forms


class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = "__all__"
        



class CodeScannerForm(forms.Form):
    uploaded_img = forms.ImageField(allow_empty_file=False)
