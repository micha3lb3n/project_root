# Generated by Django 2.0.7 on 2019-12-29 19:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0004_auto_20191228_2258'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='email',
            field=models.EmailField(max_length=254, null=True),
        ),
    ]
