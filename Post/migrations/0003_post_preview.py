# Generated by Django 3.0.3 on 2020-02-22 07:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Post', '0002_post_readed'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='preview',
            field=models.CharField(default=1, max_length=150),
            preserve_default=False,
        ),
    ]
