# Generated by Django 3.1.7 on 2021-04-16 13:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0003_comment'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'ordering': ['-created_date']},
        ),
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ['-comment_date']},
        ),
    ]