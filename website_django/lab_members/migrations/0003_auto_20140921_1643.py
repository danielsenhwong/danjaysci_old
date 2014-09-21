# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lab_members', '0002_traineetype'),
    ]

    operations = [
        migrations.AlterField(
            model_name='labmember',
            name='trainee_type',
            field=models.ForeignKey(to='lab_members.TraineeType'),
        ),
    ]
