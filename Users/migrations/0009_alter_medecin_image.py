# Generated by Django 4.2.1 on 2023-05-23 06:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0008_alter_patient_address_alter_patient_date_naissance_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medecin',
            name='image',
            field=models.ImageField(blank=True, upload_to='media/medecin_images/'),
        ),
    ]