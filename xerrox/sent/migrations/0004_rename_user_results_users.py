# Generated by Django 4.1.2 on 2022-10-28 19:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sent', '0003_rename_df_results_tweets_results_urls_results_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='results',
            old_name='user',
            new_name='users',
        ),
    ]