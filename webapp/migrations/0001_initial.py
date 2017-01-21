# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('title', models.CharField(max_length=200)),
                ('body', models.CharField(max_length=2000)),
                ('date', models.DateTimeField()),
                ('image', models.FileField(upload_to='', default=None)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=200)),
                ('comment', models.CharField(max_length=2000)),
                ('pic', models.FileField(upload_to='', default=None)),
                ('post', models.ForeignKey(to='webapp.Blog')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=200)),
                ('mail_id', models.CharField(max_length=300)),
                ('message', models.CharField(max_length=2000)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
