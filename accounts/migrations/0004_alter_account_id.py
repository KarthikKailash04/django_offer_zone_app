# Generated by Django 4.1.4 on 2023-07-10 06:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_alter_account_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
