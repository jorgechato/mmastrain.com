# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='notas',
            name='imagen',
            field=models.ImageField(default=None, upload_to=b'img/notas'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='libros',
            name='boton',
            field=models.CharField(max_length=140, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='key_expires',
            field=models.DateTimeField(default=datetime.date(2014, 10, 28)),
            preserve_default=True,
        ),
    ]
