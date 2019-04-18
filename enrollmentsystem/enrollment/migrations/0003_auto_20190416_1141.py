# Generated by Django 2.0.1 on 2019-04-16 16:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('forms', '0002_remove_formentry_child'),
        ('enrollment', '0002_auto_20190416_1114'),
    ]

    operations = [
        migrations.AddField(
            model_name='child',
            name='formentries',
            field=models.ManyToManyField(through='enrollment.TakenForm', to='forms.FormEntry'),
        ),
        migrations.AddField(
            model_name='takenform',
            name='formentries',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='taken_forms', to='forms.FormEntry'),
        ),
    ]