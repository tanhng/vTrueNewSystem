# Generated by Django 2.2.6 on 2020-01-24 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0008_auto_20200124_2141'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imagefile',
            name='anh',
            field=models.ImageField(blank=True, null=True, upload_to='media/'),
        ),
    ]
