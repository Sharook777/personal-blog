# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0002_auto_20170119_0909'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blog',
            options={'ordering': ['-date']},
        ),
        migrations.AlterField(
            model_name='blog',
            name='image',
            field=models.FileField(blank=True, upload_to='', null=True),
            preserve_default=True,
        ),
    ]
