# Generated by Django 3.0.2 on 2020-05-02 18:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0005_todo_verify_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='verify_email',
            field=models.BooleanField(default=False, null=True, verbose_name='Email Verify'),
        ),
    ]