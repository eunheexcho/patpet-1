# Generated by Django 2.1.5 on 2019-02-20 05:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('explore', '0008_auto_20190218_1627'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='communicationpost',
            options={'ordering': ['-created_at']},
        ),
        migrations.RemoveField(
            model_name='communicationpost',
            name='author',
        ),
        migrations.AddField(
            model_name='communicationpost',
            name='user',
            field=models.OneToOneField(default='', on_delete=django.db.models.deletion.CASCADE, related_name='communication', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
