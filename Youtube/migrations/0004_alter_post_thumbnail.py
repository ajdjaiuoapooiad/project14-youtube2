# Generated by Django 5.0.6 on 2024-07-28 07:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('youtube', '0003_alter_post_movie'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='thumbnail',
            field=models.ImageField(blank=True, null=True, upload_to='media/thumbnail/', verbose_name='画像'),
        ),
    ]
