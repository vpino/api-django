# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('repos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PackageCinnamon',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Nombre', models.CharField(max_length=50, verbose_name=b'nombre paquete')),
            ],
        ),
    ]
