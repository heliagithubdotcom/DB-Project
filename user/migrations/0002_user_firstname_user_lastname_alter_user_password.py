# Generated by Django 4.0.6 on 2022-07-13 09:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='firstname',
            field=models.CharField(default='default first name', max_length=40),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='lastname',
            field=models.CharField(default='default last name', max_length=40),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(max_length=300),
        ),
    ]