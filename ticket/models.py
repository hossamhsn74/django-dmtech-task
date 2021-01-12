from django.db import models
from users.models import CustomUser
from django.urls import reverse
import pyqrcode


class Ticket(models.Model):
    created_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    title = models.CharField(max_length=256)
    location = models.CharField(max_length=256)
    description = models.TextField(max_length=256)
    price = models.PositiveIntegerField()
    created_on = models.DateTimeField(auto_now=True)
    # code = models.ImageField(upload_to="qrcodes/")

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('ticketdetails', args=[str(self.id)])


    def get_code(self):
        return self.code
    
    def set_code(self, generatedCode):
        self.code = generatedCode
        self.codeGenerated = True

    code = property(get_code, set_code) 


    # def save(self, *args, **kwargs):
    #     # override save method, after saving ticket, generate qr code has all ticket info
    #     if getattr(self, 'codeGenerated', True):
    #         qr_info = [str(self.id), str(self.title), str(self.price), str(self.description), str(self.location), str(self.created_by)]
    #         qr = pyqrcode.create(",".join(qr_info))
    #         self.code = qr.png(("t%s.png", (self.id)), scale=8)
    #     super(Ticket, self).save(*args, **kwargs)


class TicketQrCode(models.Model):
    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE)
    code = models.ImageField(upload_to="qrcodes/")

    def __str__(self):
        return self.ticket
