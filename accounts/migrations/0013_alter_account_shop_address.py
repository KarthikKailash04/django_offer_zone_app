# Generated by Django 4.1.4 on 2023-07-21 18:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0012_alter_account_is_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='Shop_Address',
            field=models.CharField(max_length=100),
        ),
    ]
