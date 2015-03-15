# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('_3mw_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Entry',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('date', models.DateField()),
                ('val_a', models.DecimalField(decimal_places=2, verbose_name='Value A', max_digits=10)),
                ('val_b', models.DecimalField(decimal_places=2, verbose_name='Value B', max_digits=10)),
                ('site', models.ForeignKey(to='_3mw_app.Site')),
            ],
            options={
                'verbose_name': '',
                'verbose_name_plural': '',
                'ordering': ['-date'],
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='site',
            name='date',
        ),
        migrations.RemoveField(
            model_name='site',
            name='val_a',
        ),
        migrations.RemoveField(
            model_name='site',
            name='val_b',
        ),
    ]
