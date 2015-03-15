# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Site',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('name', models.CharField(max_length=50)),
                ('date', models.DateField()),
                ('val_a', models.DecimalField(max_digits=10, decimal_places=2)),
                ('val_b', models.DecimalField(max_digits=10, decimal_places=2)),
            ],
            options={
                'ordering': ['-name'],
                'verbose_name': 'Site',
                'verbose_name_plural': 'Sites',
            },
            bases=(models.Model,),
        ),
    ]
