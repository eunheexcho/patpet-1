# Generated by Django 2.1.5 on 2019-02-11 05:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_profile', '0002_auto_20190211_1420'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='author',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='post',
        ),
        migrations.RemoveField(
            model_name='post',
            name='author',
        ),
        migrations.AlterField(
            model_name='post',
            name='photo',
            field=models.ImageField(upload_to=''),
        ),
        migrations.DeleteModel(
            name='Comment',
        ),
    ]
