# Generated by Django 4.0.6 on 2022-07-27 19:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_remove_blog_body_quill_remove_podcast_body_quill'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='company',
            name='user',
        ),
        migrations.AlterField(
            model_name='company',
            name='featured_podcast',
            field=models.ManyToManyField(blank=True, null=True, to='core.podcast'),
        ),
    ]