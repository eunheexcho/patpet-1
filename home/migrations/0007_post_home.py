# Generated by Django 2.1.5 on 2019-02-07 13:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('my_profile', '0001_initial'),
        ('home', '0006_auto_20190207_2216'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post_home',
            fields=[
                ('post_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='my_profile.Post')),
            ],
            bases=('my_profile.post',),
        ),
    ]