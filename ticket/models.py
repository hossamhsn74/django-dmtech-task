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


