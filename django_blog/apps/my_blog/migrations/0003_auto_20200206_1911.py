# Generated by Django 3.0.3 on 2020-02-06 12:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('my_blog', '0002_auto_20200204_1956'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='post_annotation',
            new_name='annotation',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='post_text',
            new_name='text',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='post_title',
            new_name='title',
        ),
    ]
