# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-24 20:46
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import s3direct.fields


class Migration(migrations.Migration):

    dependencies = [
        ('Project', '0003_auto_20170924_1522'),
    ]

    operations = [
        migrations.CreateModel(
            name='SurveyAnswers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Project.Questions')),
                ('survey', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Project.CustomSurvey')),
            ],
        ),
        migrations.AlterField(
            model_name='senateprojects',
            name='image',
            field=s3direct.fields.S3DirectField(blank=True, null=True),
        ),
    ]
