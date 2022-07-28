# Generated by Django 4.0.6 on 2022-07-23 07:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_blog_is_published_alter_blog_slug_alter_blog_title'),
    ]

    operations = [
        migrations.RenameField(
            model_name='podcast',
            old_name='body',
            new_name='body_quill',
        ),
        migrations.RemoveField(
            model_name='blog',
            name='summary',
        ),
        migrations.AddField(
            model_name='blog',
            name='body_plain',
            field=models.TextField(blank=True, verbose_name='plain text'),
        ),
        migrations.AddField(
            model_name='blog',
            name='body_rich',
            field=models.TextField(blank=True, verbose_name='rich text'),
        ),
        migrations.AddField(
            model_name='podcast',
            name='body_plain',
            field=models.TextField(blank=True, verbose_name='plain text'),
        ),
        migrations.AddField(
            model_name='podcast',
            name='body_rich',
            field=models.TextField(blank=True, verbose_name='rich text'),
        ),
    ]