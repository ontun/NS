# Generated by Django 4.2.4 on 2023-08-22 19:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0006_author_alter_post_author'),
        ('accounts', '0003_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Author',
        ),
    ]
