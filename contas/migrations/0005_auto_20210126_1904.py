# Generated by Django 3.1.5 on 2021-01-26 22:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contas', '0004_auto_20210126_1809'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='transacao',
            name='data',
        ),
        migrations.AddField(
            model_name='transacao',
            name='data6',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
