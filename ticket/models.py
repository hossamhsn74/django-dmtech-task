from django.db import models
from users.models import CustomUser
from django.urls import reverse
from django.db.models.signals import post_save
from django.dispatch import receiver
import pyqrcode


class Ticket(models.Model):
    created_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    title = models.CharField(max_length=256)
    location = models.CharField(max_length=256)
    description = models.TextField(max_length=256)
    price = models.PositiveIntegerField()
    created_on = models.DateTimeField(auto_now=True)
    # code = models.ImageField(upload_to="qrcodes/", default=None, null=True)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('ticketdetails', args=[str(self.id)])

    # def save(self,*args,**kwargs):
    #     if self.pk is None:
    #         qr_info = [str(self.pk), str(self.title), str(self.price), str(self.description), str(self.location), str(self.created_by)]
    #         qr = pyqrcode.create(",".join(qr_info))
    #         code = qr.png("code{}.png".format(self.pk), scale=8)
    #         TicketQrCode.objects.create(ticket=self, code=code)
    #     super(Ticket, self).save(*args,**kwargs)


# generating qr code on post_save ticket model
@receiver(post_save, sender=Ticket, dispatch_uid="generate_qr_code")
def generateTicketCodeObject(sender, instance, **kwargs):
    qr_info = [str(instance.pk), str(instance.title), str(instance.price), str(
        instance.description), str(instance.location), str(instance.created_by)]
    qr = pyqrcode.create(",".join(qr_info),error='L', version=27, mode='binary')
    code = qr.png("static/images/code{}.png".format(instance.pk), scale=8)
    qr.show()
    # print(qr.terminal(quiet_zone=1))
    TicketQrCode.objects.create(ticket=instance, code=code)


class TicketQrCode(models.Model):
    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE)
    code = models.ImageField(upload_to="qrcodes/")

    def __str__(self):
        return self.ticket.title
