# Generated by Django 4.2.1 on 2023-07-02 20:49

import Users.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0009_alter_medecin_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medecin',
            name='image',
            field=models.ImageField(blank=True, upload_to=Users.models.upload_to),
        ),
    ]
