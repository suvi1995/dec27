# Generated by Django 4.1.3 on 2022-12-11 06:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0014_message_room'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Document',
        ),
        migrations.DeleteModel(
            name='Message',
        ),
        migrations.DeleteModel(
            name='Room',
        ),
        migrations.DeleteModel(
            name='SignUpForm',
        ),
    ]
