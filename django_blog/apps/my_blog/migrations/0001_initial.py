# Generated by Django 3.0.3 on 2020-02-04 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('post_title', models.CharField(max_length=100)),
                ('post_annotation', models.CharField(max_length=1000)),
                ('post_text', models.TextField()),
            ],
        ),
    ]
