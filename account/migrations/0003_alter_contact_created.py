# Generated by Django 4.0.2 on 2022-03-06 10:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_contact'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='created',
            field=models.DateTimeField(auto_now=True, db_index=True),
        ),
    ]
