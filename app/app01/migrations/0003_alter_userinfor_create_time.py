# Generated by Django 4.0 on 2022-05-19 19:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0002_remove_userinfor_account_remove_userinfor_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfor',
            name='create_time',
            field=models.DateField(verbose_name='入职时间'),
        ),
    ]
