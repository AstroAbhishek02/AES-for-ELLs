# Generated by Django 2.1 on 2018-08-12 15:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('grader', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='essaySet',
            field=models.IntegerField(default=0, unique=True),
            preserve_default=False,
        ),
    ]
