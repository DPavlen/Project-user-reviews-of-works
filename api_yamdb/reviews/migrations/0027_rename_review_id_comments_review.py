# Generated by Django 3.2 on 2023-06-18 15:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0026_auto_20230618_1440'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comments',
            old_name='review_id',
            new_name='review',
        ),
    ]