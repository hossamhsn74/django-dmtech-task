# Generated by Django 3.1.2 on 2021-01-14 05:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ticket', '0010_auto_20210114_0141'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='code',
            field=models.ImageField(blank=True, upload_to='qrcodes/'),
        ),
    ]