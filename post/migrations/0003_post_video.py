# Generated by Django 4.2.3 on 2023-07-15 11:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0002_post_type_1'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='video',
            field=models.TextField(blank=True, null=True),
        ),
    ]
