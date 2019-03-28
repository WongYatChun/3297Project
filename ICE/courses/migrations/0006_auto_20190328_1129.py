# Generated by Django 2.1.7 on 2019-03-28 11:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0005_auto_20190328_1059'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='course',
            options={'ordering': ['create_time']},
        ),
        migrations.RenameField(
            model_name='course',
            old_name='created',
            new_name='create_time',
        ),
        migrations.RenameField(
            model_name='course',
            old_name='overview',
            new_name='description',
        ),
        migrations.RenameField(
            model_name='file',
            old_name='created',
            new_name='create_time',
        ),
        migrations.RenameField(
            model_name='file',
            old_name='updated',
            new_name='update_time',
        ),
        migrations.RenameField(
            model_name='image',
            old_name='created',
            new_name='create_time',
        ),
        migrations.RenameField(
            model_name='image',
            old_name='updated',
            new_name='update_time',
        ),
        migrations.RenameField(
            model_name='text',
            old_name='created',
            new_name='create_time',
        ),
        migrations.RenameField(
            model_name='text',
            old_name='updated',
            new_name='update_time',
        ),
        migrations.RenameField(
            model_name='video',
            old_name='created',
            new_name='create_time',
        ),
        migrations.RenameField(
            model_name='video',
            old_name='updated',
            new_name='update_time',
        ),
        migrations.AlterField(
            model_name='content',
            name='content_type',
            field=models.ForeignKey(limit_choices_to={'model__in': ('text', 'image', 'video', 'file')}, on_delete=django.db.models.deletion.CASCADE, to='contenttypes.ContentType'),
        ),
        migrations.AlterField(
            model_name='course',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='courses_create_date', to=settings.AUTH_USER_MODEL),
        ),
    ]