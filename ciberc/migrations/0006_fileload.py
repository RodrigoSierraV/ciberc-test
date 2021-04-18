# Generated by Django 2.2 on 2021-04-17 14:17

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ciberc', '0005_delete_fileload'),
    ]

    operations = [
        migrations.CreateModel(
            name='FileLoad',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('date', models.DateTimeField(auto_now=True)),
                ('file', models.FileField(upload_to='uploads/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=('xls', 'xlsx'))])),
            ],
        ),
    ]
