# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0003_auto_20170120_0821'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='pic',
            field=models.FileField(upload_to='', blank=True, null=True),
            preserve_default=True,
        ),
    ]
