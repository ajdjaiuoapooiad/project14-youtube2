# Generated by Django 5.0.6 on 2024-07-29 08:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('youtube', '0006_comment_alter_post_thumbnail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='good',
            field=models.IntegerField(default=0, verbose_name='いいね'),
        ),
    ]