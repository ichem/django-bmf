# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion
from django.conf import settings

class Migration(migrations.Migration):
    dependencies = [
        ('djangobmf_quotation', '0002_optional_quotation_project'),
        migrations.swappable_dependency(settings.BMF_CONTRIB_EMPLOYEE),
    ]
    operations = [
        migrations.AddField(
            model_name='quotation',
            name='employee',
            field=models.ForeignKey(to=settings.BMF_CONTRIB_EMPLOYEE, on_delete=django.db.models.deletion.SET_NULL, null=True),
            preserve_default=True,
        ),
    ]
