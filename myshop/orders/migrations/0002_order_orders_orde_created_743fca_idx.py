# Generated by Django 4.0 on 2023-11-01 10:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AddIndex(
            model_name='order',
            index=models.Index(fields=['-created'], name='orders_orde_created_743fca_idx'),
        ),
    ]