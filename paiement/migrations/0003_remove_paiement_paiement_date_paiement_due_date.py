# Generated by Django 4.2.1 on 2023-05-27 18:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paiement', '0002_paiement_start_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='paiement',
            name='paiement_date',
        ),
        migrations.AddField(
            model_name='paiement',
            name='due_date',
            field=models.DateField(auto_now_add=True, null=True),
        ),
    ]
