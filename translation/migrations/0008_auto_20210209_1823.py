# Generated by Django 3.1.4 on 2021-02-09 18:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('translation', '0007_auto_20210127_1238'),
    ]

    operations = [
        migrations.AlterField(
            model_name='country',
            name='Continent',
            field=models.CharField(choices=[('AF', 'Afrique'), ('NA', 'Amerique du Nord'), ('SA', 'Amerique du Sud'), ('OC', 'Océanie'), ('AS', 'Asie'), ('EU', 'Europe')], max_length=50),
        ),
    ]
