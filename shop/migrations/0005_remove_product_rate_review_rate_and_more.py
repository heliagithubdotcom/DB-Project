# Generated by Django 4.0.6 on 2022-07-10 08:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_remove_review_caption_review_description_review_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='rate',
        ),
        migrations.AddField(
            model_name='review',
            name='rate',
            field=models.PositiveSmallIntegerField(default=3),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='review',
            name='description',
            field=models.CharField(blank=True, max_length=300),
        ),
    ]