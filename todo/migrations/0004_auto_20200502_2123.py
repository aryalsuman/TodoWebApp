# Generated by Django 3.0.2 on 2020-05-02 15:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0003_auto_20200502_2122'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='details',
            field=models.TextField(blank=True, max_length=100, null=True),
        ),
    ]
