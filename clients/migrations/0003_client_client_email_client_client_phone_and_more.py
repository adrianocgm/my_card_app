# Generated by Django 4.1.5 on 2023-01-23 22:21

import datetime
from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0002_alter_client_issue_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='client_email',
            field=models.EmailField(max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='client',
            name='client_phone',
            field=models.CharField(max_length=11, null=True),
        ),
        migrations.AddField(
            model_name='client',
            name='client_since',
            field=models.DateField(default=datetime.date, max_length=10),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='client',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
    ]
