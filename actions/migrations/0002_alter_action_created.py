# Generated by Django 4.0.2 on 2022-03-06 11:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('actions', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='action',
            name='created',
            field=models.DateTimeField(auto_now=True, db_index=True),
        ),
    ]