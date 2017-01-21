# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0004_auto_20170120_1042'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comments',
            options={'ordering': ['-date']},
        ),
        migrations.AddField(
            model_name='comments',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2017, 1, 20, 6, 48, 21, 953779, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
    ]
