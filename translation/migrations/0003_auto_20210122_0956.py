# Generated by Django 3.1.4 on 2021-01-22 09:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('translation', '0002_auto_20210112_1924'),
    ]

    operations = [
        migrations.RenameField(
            model_name='countries',
            old_name='flagcode',
            new_name='contrycode',
        ),
    ]
