# Generated by Django 2.2.7 on 2020-03-01 12:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_auto_20200301_1206'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='enseigner',
            name='id_cours',
        ),
        migrations.AddField(
            model_name='enseigner',
            name='id_cours',
            field=models.ManyToManyField(to='myapp.Cours'),
        ),
    ]
