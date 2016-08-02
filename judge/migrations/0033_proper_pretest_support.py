# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-08-01 21:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('judge', '0032_hide_problem_tags_in_contest'),
    ]

    operations = [
        migrations.AddField(
            model_name='contest',
            name='run_pretests_only',
            field=models.BooleanField(default=False, help_text='Whether judges should grade pretests only, versus all testcases. Commonly set during a contest, then unset prior to rejudging user submissions when the contest ends.', verbose_name='run pretests only'),
        ),
        migrations.AddField(
            model_name='contestsubmission',
            name='is_pretest',
            field=models.BooleanField(default=False, help_text='Whether this submission was ran only on pretests.', verbose_name='is pretested'),
        ),
    ]