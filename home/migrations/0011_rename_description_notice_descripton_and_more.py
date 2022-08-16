# Generated by Django 4.0.2 on 2022-02-24 16:48

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0010_notice_date_notice_description'),
    ]

    operations = [
        migrations.RenameField(
            model_name='notice',
            old_name='description',
            new_name='descripton',
        ),
        migrations.RemoveField(
            model_name='notice',
            name='date',
        ),
        migrations.AddField(
            model_name='notice',
            name='event_date',
            field=models.DateTimeField(default=datetime.date.today),
        ),
        migrations.AddField(
            model_name='notice',
            name='name',
            field=models.CharField(default='none', max_length=120),
        ),
    ]