# Generated by Django 4.0.6 on 2022-07-26 23:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_quill.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0005_rename_body_blog_body_quill'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='user',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='podcast',
            name='body_quill',
            field=django_quill.fields.QuillField(blank=True, verbose_name='quill text'),
        ),
        migrations.AlterField(
            model_name='podcast',
            name='published_link',
            field=models.URLField(blank=True, verbose_name='published link'),
        ),
    ]
