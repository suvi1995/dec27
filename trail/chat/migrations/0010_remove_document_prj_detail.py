# Generated by Django 4.1.3 on 2022-12-09 16:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0009_document'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='document',
            name='prj_detail',
        ),
    ]
