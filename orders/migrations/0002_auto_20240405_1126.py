# Generated by Django 3.1 on 2024-04-05 05:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orderproduct',
            old_name='variations',
            new_name='variation',
        ),
    ]