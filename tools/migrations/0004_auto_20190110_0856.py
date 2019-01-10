# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2019-01-10 08:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tools', '0003_auto_20190110_0647'),
    ]

    operations = [
        migrations.AddField(
            model_name='nikto_vuln_db',
            name='dup_hash',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='nikto_vuln_db',
            name='false_positive',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='nikto_vuln_db',
            name='false_positive_hash',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='nikto_vuln_db',
            name='jira_ticket',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='nikto_vuln_db',
            name='vuln_duplicate',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='nikto_vuln_db',
            name='vuln_id',
            field=models.UUIDField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='nikto_vuln_db',
            name='vuln_status',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='nikto_vuln_db',
            name='scan_id',
            field=models.UUIDField(blank=True, null=True),
        ),
    ]
