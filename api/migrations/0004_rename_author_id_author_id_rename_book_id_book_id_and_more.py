# Generated by Django 4.2.3 on 2023-08-25 04:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_alter_author_author_id_alter_book_book_id_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='author',
            old_name='author_id',
            new_name='id',
        ),
        migrations.RenameField(
            model_name='book',
            old_name='book_id',
            new_name='id',
        ),
        migrations.RenameField(
            model_name='publisher',
            old_name='publisher_id',
            new_name='id',
        ),
    ]