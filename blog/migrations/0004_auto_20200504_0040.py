# Generated by Django 3.0.5 on 2020-05-04 07:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_blogcomment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blogcomment',
            old_name='User',
            new_name='user',
        ),
    ]
