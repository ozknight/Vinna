# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('company_name', models.CharField(max_length=100)),
                ('company_address', models.CharField(max_length=255)),
                ('company_country', models.CharField(max_length=100)),
                ('company_province', models.CharField(max_length=100)),
                ('company_postal_code', models.SmallIntegerField(default=6000)),
                ('company_email', models.EmailField(max_length=254)),
                ('company_website', models.URLField(null=True, blank=True)),
                ('company_contact_person', models.CharField(max_length=255)),
                ('valid', models.BooleanField(default=False)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Company',
                'verbose_name_plural': 'Companies',
            },
        ),
    ]
