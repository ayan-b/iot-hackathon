# Generated by Django 2.1.3 on 2019-11-20 18:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('datavis', '0004_remove_comment_dustbin'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='author',
            new_name='user',
        ),
    ]
