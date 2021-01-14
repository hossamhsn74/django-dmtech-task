from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, FormView
from ticket.models import Ticket
from .forms import CodeScannerForm
from django.urls import reverse
from PIL import Image
import cv2
import numpy


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


class scanTicket(FormView):
    template_name = 'ticket/scanTicket.html'
    form_class = CodeScannerForm

    def get_success_url(self):
        return reverse('ticketlist')

    def form_valid(self, form):
        uploaded_img = form.cleaned_data['uploaded_img']
        pil_img = Image.open(uploaded_img).convert('RGB')
        open_cv_img = cv2.cvtColor(numpy.array(pil_img), cv2.COLOR_RGB2BGR)
        detector = cv2.QRCodeDetector()
        data, bbox, straight_qrcode = detector.detectAndDecode(open_cv_img)

        # check if image has QR code in first place
        if bbox is not None:
            print(f"QRCode data:\n{data}")
            # display the image with lines
            # length of bounding box
            n_lines = len(bbox)
            for i in range(n_lines):
                # draw all lines
                point1 = tuple(bbox[i][0])
                point2 = tuple(bbox[(i+1) % n_lines][0])
                cv2.line(open_cv_img, point1, point2,
                         color=(255, 0, 0), thickness=2)
        else:
            # redirect to sorry page
            pass
        
        print("checking data", type(data))
        # divide data and query from db for match
        # for key in data.items():
            # print("checking data" , data.items())
        # for 
        # if Ticket.objects.filter(title=data.items().['title'] & created_by=data['created_by'] & created_on=data['created_on']):
        #     # found then redirect to show object
        #     print("found")
        #     return reverse('ticketdetails', args=[str(self.id)])
        # else:
        #     # not found redirect to sorry page
        #     pass
        return super().form_valid(form)
