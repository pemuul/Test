# Generated by Django 2.1.3 on 2019-06-11 07:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0010_auto_20190611_0017'),
    ]

    operations = [
        migrations.CreateModel(
            name='Koment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
                ('koment', models.TextField()),
                ('data', models.CharField(max_length=20)),
            ],
        ),
    ]
