# Generated by Django 2.2.2 on 2019-07-17 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('result', '0005_listcommit_owned'),
    ]

    operations = [
        migrations.AddField(
            model_name='listcommit',
            name='assigned',
            field=models.BooleanField(default=False),
        ),
    ]
