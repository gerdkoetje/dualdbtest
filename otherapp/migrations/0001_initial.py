# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TestModel8',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('naam', models.CharField(max_length=255, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='TestModel9',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('lastpath', models.TextField(blank=True)),
                ('memberstatus', models.CharField(max_length=255, blank=True)),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, blank=True, to='otherapp.TestModel8')),
            ],
        ),
    ]
