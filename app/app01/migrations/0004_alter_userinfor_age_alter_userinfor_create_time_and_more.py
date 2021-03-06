# Generated by Django 4.0 on 2022-05-24 23:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0003_alter_userinfor_create_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfor',
            name='age',
            field=models.IntegerField(verbose_name='age'),
        ),
        migrations.AlterField(
            model_name='userinfor',
            name='create_time',
            field=models.DateField(verbose_name='start date'),
        ),
        migrations.AlterField(
            model_name='userinfor',
            name='depart',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app01.department', verbose_name='department'),
        ),
        migrations.AlterField(
            model_name='userinfor',
            name='gender',
            field=models.SmallIntegerField(choices=[(1, 'male'), (2, 'female')], verbose_name='gender'),
        ),
        migrations.AlterField(
            model_name='userinfor',
            name='name',
            field=models.CharField(max_length=16, verbose_name='name'),
        ),
    ]
