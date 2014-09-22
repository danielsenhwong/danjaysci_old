# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lab_members', '0003_auto_20140921_1643'),
    ]

    operations = [
        migrations.AddField(
            model_name='labmember',
            name='alt_email_address',
            field=models.EmailField(help_text=b'An alternate e-mail address for this lab member, in case the primary becomes deactivated.', max_length=75, unique=True, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='labmember',
            name='email_address',
            field=models.EmailField(help_text=b'Primary e-mail address for this lab member. If a current Tufts affiliate, the Tufts e-mail address is preferred.', max_length=75, unique=True, null=True, blank=True),
            preserve_default=True,
        ),
    ]
