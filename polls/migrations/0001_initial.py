# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('AuthorID', models.IntegerField(default=0)),
                ('Name', models.CharField(max_length=30)),
                ('Age', models.IntegerField(default=0)),
                ('Country', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ISBN', models.CharField(max_length=13)),
                ('Title', models.CharField(max_length=40)),
                ('Publisher', models.CharField(max_length=50)),
                ('PublishDate', models.DateField(verbose_name=b'date published')),
                ('Price', models.FloatField()),
                ('AuthorID', models.ForeignKey(to='polls.Author')),
            ],
        ),
    ]
