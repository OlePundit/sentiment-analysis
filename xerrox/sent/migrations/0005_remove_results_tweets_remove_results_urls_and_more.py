# Generated by Django 4.1.2 on 2022-10-28 20:43

from django.db import migrations



class Migration(migrations.Migration):

    dependencies = [
        ('sent', '0004_rename_user_results_users'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='results',
            name='tweets',
        ),
        migrations.RemoveField(
            model_name='results',
            name='urls',
        ),
        migrations.RemoveField(
            model_name='results',
            name='users',
        ),
        migrations.AddField(
            model_name='results',
            name='json',
            field=jsonfield.fields.JSONField(default=0),
            preserve_default=False,
        ),
    ]
