# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-05-14 18:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_pregunta_respuesta'),
    ]

    operations = [
        migrations.RenameField(
            model_name='respuesta',
            old_name='isCorrect',
            new_name='correct',
        ),
        migrations.RenameField(
            model_name='respuesta',
            old_name='pregunta',
            new_name='question',
        ),
        migrations.RenameField(
            model_name='respuesta',
            old_name='votos',
            new_name='votes',
        ),
        migrations.RemoveField(
            model_name='pregunta',
            name='tema',
        ),
        migrations.RemoveField(
            model_name='pregunta',
            name='texto',
        ),
        migrations.RemoveField(
            model_name='respuesta',
            name='textoRespuesta',
        ),
        migrations.AddField(
            model_name='pregunta',
            name='question_tema',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='pregunta',
            name='question_text',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='respuesta',
            name='respuesta',
            field=models.CharField(default='', max_length=200),
        ),
    ]
