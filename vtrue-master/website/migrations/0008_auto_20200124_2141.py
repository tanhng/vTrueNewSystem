# Generated by Django 2.2.6 on 2020-01-24 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0007_imagefile_news'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='thamso',
            name='maxcount',
        ),
        migrations.AddField(
            model_name='thamso',
            name='name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='thamso',
            name='value',
            field=models.IntegerField(default=0),
        ),
    ]
