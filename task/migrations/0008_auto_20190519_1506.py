# Generated by Django 2.2.1 on 2019-05-19 23:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0007_delete_hleba'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hleb',
            name='description',
            field=models.CharField(max_length=2500),
        ),
    ]
