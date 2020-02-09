# Generated by Django 2.2.7 on 2020-02-08 10:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_auto_20200207_1308'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cahiertexte',
            options={'ordering': ['date'], 'verbose_name_plural': 'Cahier de texte'},
        ),
        migrations.AlterModelOptions(
            name='classe',
            options={'ordering': ['nom_classe'], 'verbose_name_plural': 'Classe'},
        ),
        migrations.AlterModelOptions(
            name='cours',
            options={'verbose_name_plural': 'Cours'},
        ),
        migrations.AlterModelOptions(
            name='eleve',
            options={'ordering': ['nom_eleve'], 'verbose_name_plural': 'Eleve'},
        ),
        migrations.AlterModelOptions(
            name='enseigner',
            options={'verbose_name_plural': 'Enseigner'},
        ),
        migrations.AlterModelOptions(
            name='notification',
            options={'verbose_name_plural': 'Notifications'},
        ),
        migrations.AlterModelOptions(
            name='planning',
            options={'verbose_name_plural': 'Planning'},
        ),
        migrations.AlterModelOptions(
            name='presabs',
            options={'verbose_name_plural': 'Absences'},
        ),
        migrations.AlterModelOptions(
            name='prof',
            options={'verbose_name_plural': 'Professeur'},
        ),
        migrations.AlterModelOptions(
            name='responsable_eleve',
            options={'ordering': ['login_res'], 'verbose_name_plural': 'Responsable de classe'},
        ),
        migrations.AlterModelOptions(
            name='responsable_prof',
            options={'verbose_name_plural': 'Responsable pédagogique'},
        ),
        migrations.AlterModelOptions(
            name='secretaire',
            options={'verbose_name_plural': 'Secretaire'},
        ),
        migrations.AddField(
            model_name='cahiertexte',
            name='id_cours',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to='myapp.Cours'),
            preserve_default=False,
        ),
    ]