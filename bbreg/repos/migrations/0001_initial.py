# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Repositorio',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Nombre', models.CharField(max_length=50, verbose_name=b'nombre proyecto')),
                ('Url', models.CharField(max_length=100, verbose_name=b'url repositorio del proyecto')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
