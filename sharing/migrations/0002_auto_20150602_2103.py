# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sharing', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='name',
            field=models.CharField(default=b'unnamed', max_length=120),
        ),
        migrations.AlterField(
            model_name='item',
            name='id',
            field=models.IntegerField(serialize=False, primary_key=True),
        ),
    ]
