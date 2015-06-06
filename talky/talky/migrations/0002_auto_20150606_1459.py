# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('talky', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Passport',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('passport_number', models.IntegerField(unique=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='player',
            name='passport_number',
        ),
    ]
