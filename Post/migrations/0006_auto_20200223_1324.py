# Generated by Django 3.0.3 on 2020-02-23 13:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Post', '0005_auto_20200223_0853'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='post_id',
            field=models.CharField(max_length=10),
        ),
    ]
