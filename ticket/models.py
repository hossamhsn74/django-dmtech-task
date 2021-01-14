from django.db import models
from users.models import CustomUser
from django.urls import reverse
from django.dispatch import receiver
import qrcode
from io import BytesIO
from qrcode.image.pure import PymagingImage
from django.core.files import File
from PIL import Image, ImageDraw



class Ticket(models.Model):
    created_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    title = models.CharField(max_length=256)
    location = models.CharField(max_length=256)
    description = models.TextField(max_length=256)
    price = models.PositiveIntegerField()
    created_on = models.DateTimeField(auto_now=True)
    code = models.ImageField(upload_to="qrcodes/", blank=True, default=None)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('ticketdetails', args=[str(self.id)])

    def save(self, *args, **kwargs):
        qr_info = [str(self.pk), str(self.title), str(self.price), str(
            self.description), str(self.location), str(self.created_by)]
        qr_info = ",".join(qr_info)
        qr = qrcode.QRCode(
            version=12,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=3,
            border=15,
        )
        qr.add_data(qr_info)
        qr.make(fit=True)
        qrcode_img = qr.make_image(fill_color="black", back_color="white", fit=True)
        canvas = Image.new('RGB', (290, 290), 'white')
        draw = ImageDraw.Draw(canvas)
        canvas.paste(qrcode_img)
        file_name = "code-{}.png".format(self.pk)
        buffer = BytesIO()
        canvas.save(buffer, 'PNG')
        self.code.save(file_name, File(buffer), save=False)
        canvas.close()
        super().save(*args, **kwargs)


# generating qr code on post_save ticket model
# @receiver(post_save, sender=Ticket, dispatch_uid="generate_qr_code")
# def generateTicketCodeObject(sender, instance, **kwargs):
#     qr_info = [str(instance.pk), str(instance.title), str(instance.price), str(
#         instance.description), str(instance.location), str(instance.created_by)]
#     qr_info = ",".join(qr_info)
#     qrcode_img = qrcode.make(qr_info)
#     canvas = Image.new('PNG', (300, 300), 'white')
#     draw = ImageDraw.Draw(canvas)
#     canvas.paste(qrcode_img)
#     file_name = "code-{}.png".format(instance.pk)
#     buffer = BytesIO()
#     canvas.save(buffer, 'PNG')

    # qr = pyqrcode.create(",".join(qr_info), error='L')
    # qr.png("static/images/code{}.png".format(instance.pk), scale=8,
    #        module_color=[0, 0, 0, 128], background=[0xff, 0xff, 0xcc])
    #
    # TicketQrCode.objects.create(ticket=instance, code=buffer)


# class TicketQrCode(models.Model):
#     ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE)
#     code = models.ImageField(upload_to="qrcodes/", blank=True, default=None)

#     def __str__(self):
#         return self.ticket.title

    # def save(self,*args,**kwargs):
    #     # self.code = ("q{}.png".format(self.ticket.id), File(self.code),save=False)
    #     # if self.pk is None:
    #         # image_data = ContentFile(b64decode(self.code))
    #         # setattr(instance, model_field.name, ContentFile(image_data, 'myImage.png'))
    #         # self.code = ContentFile(image_data, "static/images/q{}.png".format(self.ticket.id) )
    #     super(Ticket, self).save(*args,**kwargs)
