# Generated by Django 4.2.1 on 2023-05-27 18:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paiement', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='paiement',
            name='start_date',
            field=models.DateField(null=True),
        ),
    ]