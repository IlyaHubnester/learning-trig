# Generated by Django 3.2.10 on 2021-12-10 03:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='answer',
            name='question',
        ),
        migrations.AddField(
            model_name='question',
            name='answers',
            field=models.ManyToManyField(to='app.Answer'),
        ),
    ]
