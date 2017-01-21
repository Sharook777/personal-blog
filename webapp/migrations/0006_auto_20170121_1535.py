# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0005_auto_20170120_1218'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='name',
            field=models.CharField(max_length=200, default='unknown'),
            preserve_default=True,
        ),
    ]
