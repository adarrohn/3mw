# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('_3mw_app', '0002_auto_20150315_1707'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='entry',
            options={'verbose_name': 'Entry', 'ordering': ['date'], 'verbose_name_plural': 'Entries'},
        ),
        migrations.AlterModelOptions(
            name='site',
            options={'verbose_name': 'Site', 'ordering': ['name'], 'verbose_name_plural': 'Sites'},
        ),
    ]
