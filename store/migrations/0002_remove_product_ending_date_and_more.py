# Generated by Django 4.1.4 on 2023-07-11 13:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='ending_date',
        ),
        migrations.RemoveField(
            model_name='product',
            name='starting_date',
        ),
    ]