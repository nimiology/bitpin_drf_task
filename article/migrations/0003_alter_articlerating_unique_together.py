# Generated by Django 4.1.2 on 2022-10-23 09:22

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('article', '0002_alter_articlerating_unique_together'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='articlerating',
            unique_together={('owner', 'article')},
        ),
    ]