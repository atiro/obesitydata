# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Admissions',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('year', models.IntegerField()),
                ('gender', models.CharField(default=b'M', max_length=1, choices=[(b'M', b'Male'), (b'F', b'Female'), (b'U', b'Unknown')])),
                ('admissions', models.IntegerField()),
            ],
        ),
    ]
