# Generated by Django 2.0.1 on 2019-04-28 17:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('enrollment', '0002_auto_20190426_1052'),
    ]

    operations = [
        migrations.AddField(
            model_name='parent',
            name='address',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='parent',
            name='phonenumber',
            field=models.CharField(max_length=255, null=True),
        ),
    ]