# Generated by Django 3.2.16 on 2022-10-29 21:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sent', '0010_rename_containter_results_container'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='results',
            name='key',
        ),
        migrations.RemoveField(
            model_name='results',
            name='value',
        ),
    ]