# Generated by Django 3.2 on 2022-12-20 20:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0003_merge_20221220_2104'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='review',
            unique_together={('title', 'author')},
        ),
    ]
