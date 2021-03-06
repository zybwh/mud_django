# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-23 09:36
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0002_auto_20160921_1536'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserStats',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('currentHp', models.PositiveIntegerField(default=0)),
                ('maxHp', models.PositiveIntegerField(default=0)),
                ('currentMana', models.PositiveIntegerField(default=0)),
                ('maxMana', models.PositiveIntegerField(default=0)),
                ('power', models.PositiveIntegerField(default=0)),
                ('agility', models.PositiveIntegerField(default=0)),
                ('intelligent', models.PositiveIntegerField(default=0)),
                ('currentExp', models.PositiveIntegerField(default=0)),
                ('nextExp', models.PositiveIntegerField(default=0)),
            ],
        ),
        migrations.AlterField(
            model_name='users',
            name='userid',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='users',
            name='stats',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to='backend.UserStats'),
            preserve_default=False,
        ),
    ]
