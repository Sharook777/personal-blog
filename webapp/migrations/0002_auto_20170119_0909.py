# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2017, 1, 19, 3, 39, 29, 681244, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='blog',
            name='body',
            field=models.TextField(),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='comments',
            name='comment',
            field=models.TextField(),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='contact',
            name='message',
            field=models.TextField(),
            preserve_default=True,
        ),
    ]
