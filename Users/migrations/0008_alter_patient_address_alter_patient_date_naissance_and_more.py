# Generated by Django 4.2.1 on 2023-05-21 12:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0007_alter_patient_sexe'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='address',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='patient',
            name='date_naissance',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='sexe',
            field=models.CharField(blank=True, choices=[('H', 'Homme'), ('F', 'Femme')], max_length=255),
        ),
        migrations.AlterField(
            model_name='user',
            name='tele',
            field=models.CharField(blank=True, max_length=20),
        ),
    ]
