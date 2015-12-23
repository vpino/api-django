# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('repos', '0002_packagecinnamon'),
    ]

    operations = [
        migrations.CreateModel(
            name='PackageCinnamonEdu',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Nombre', models.CharField(max_length=50, verbose_name=b'nombre paquete')),
            ],
        ),
        migrations.CreateModel(
            name='PackageGeneric',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Nombre', models.CharField(max_length=50, verbose_name=b'nombre paquete')),
            ],
        ),
        migrations.CreateModel(
            name='PackageGenericEdu',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Nombre', models.CharField(max_length=50, verbose_name=b'nombre paquete')),
            ],
        ),
        migrations.CreateModel(
            name='PackageMate',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Nombre', models.CharField(max_length=50, verbose_name=b'nombre paquete')),
            ],
        ),
        migrations.CreateModel(
            name='PackageMateEdu',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Nombre', models.CharField(max_length=50, verbose_name=b'nombre paquete')),
            ],
        ),
    ]
