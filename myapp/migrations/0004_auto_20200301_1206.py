# Generated by Django 2.2.7 on 2020-03-01 12:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_auto_20200229_2321'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='enseigner',
            name='id_classe',
        ),
        migrations.AddField(
            model_name='enseigner',
            name='id_cours',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to='myapp.Cours'),
            preserve_default=False,
        ),
    ]