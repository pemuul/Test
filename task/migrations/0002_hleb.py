# Generated by Django 2.2.1 on 2019-05-14 06:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hleb',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=60)),
                ('button', models.CharField(max_length=10)),
                ('img', models.FileField(upload_to='')),
            ],
        ),
    ]
