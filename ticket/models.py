from django.db import models
from users.models import CustomUser
from django.urls import reverse
from django.dispatch import receiver
import qrcode
from io import BytesIO
from qrcode.image.pure import PymagingImage
from django.core.files import File
from PIL import Image, ImageDraw
from django.db.models.signals import post_save


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
        data = {}
        data["title"] = str(self.title)
        data["description"] = str(self.description)
        data["price"] = str(self.price)
        data["location"] = str(self.location)
        data["created_by"] = str(self.created_by)
        qr_info = str(data)
                           
        qr = qrcode.QRCode(
            version=12,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=3,
            border=15,
        )
        qr.add_data(str(qr_info))
        qr.make(fit=True)
        qrcode_img = qr.make_image(
            fill_color="black", back_color="white", fit=True)
        canvas = Image.new('RGB', (290, 290), 'white')
        draw = ImageDraw.Draw(canvas)
        canvas.paste(qrcode_img)
        file_name = "code-{}.png".format(self.pk)
        buffer = BytesIO()
        canvas.save(buffer, 'PNG')
        self.code.save(file_name, File(buffer), save=False)
        canvas.close()
        super().save(*args, **kwargs)
