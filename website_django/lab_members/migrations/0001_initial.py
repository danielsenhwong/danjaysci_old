# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='LabMember',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('trainee_type', models.CharField(blank=True, max_length=128, choices=[(b'Post-doctoral Fellow', b'Post-doctoral Fellow'), (b'Graduate Student, PhD', b'Graduate Student, PhD'), (b'Medical Student, MD', b'Medical Student, MD'), (b'Graduate Student, MS/MBS', b'Graduate Student, MS/MBS'), (b'Technician', b'Technician'), (b'PREP Scholar', b'PREP Scholar'), (b'Undergraduate Student', b'Undergraduate Student'), (b'High School Student', b'High School Student'), (b'Visiting Scientist', b'Visiting Scientist')])),
                ('start_year', models.PositiveIntegerField(blank=True, null=True, choices=[(1985, 1985), (1986, 1986), (1987, 1987), (1988, 1988), (1989, 1989), (1990, 1990), (1991, 1991), (1992, 1992), (1993, 1993), (1994, 1994), (1995, 1995), (1996, 1996), (1997, 1997), (1998, 1998), (1999, 1999), (2000, 2000), (2001, 2001), (2002, 2002), (2003, 2003), (2004, 2004), (2005, 2005), (2006, 2006), (2007, 2007), (2008, 2008), (2009, 2009), (2010, 2010), (2011, 2011), (2012, 2012), (2013, 2013), (2014, 2014)])),
                ('end_year', models.PositiveIntegerField(blank=True, null=True, choices=[(1985, 1985), (1986, 1986), (1987, 1987), (1988, 1988), (1989, 1989), (1990, 1990), (1991, 1991), (1992, 1992), (1993, 1993), (1994, 1994), (1995, 1995), (1996, 1996), (1997, 1997), (1998, 1998), (1999, 1999), (2000, 2000), (2001, 2001), (2002, 2002), (2003, 2003), (2004, 2004), (2005, 2005), (2006, 2006), (2007, 2007), (2008, 2008), (2009, 2009), (2010, 2010), (2011, 2011), (2012, 2012), (2013, 2013), (2014, 2014)])),
                ('current_position', models.TextField(null=True, blank=True)),
                ('date_added', models.DateField(auto_now_add=True)),
                ('last_updated', models.DateField(help_text=b'The date this person\'s "Current Position" information was last updated.', null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
