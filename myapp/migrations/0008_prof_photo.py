# Generated by Django 2.2.7 on 2020-03-03 15:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0007_remove_enseigner_duree'),
    ]

    operations = [
        migrations.AddField(
            model_name='prof',
            name='photo',
            field=models.ImageField(default=2, upload_to='Images/'),
            preserve_default=False,
        ),
    ]
