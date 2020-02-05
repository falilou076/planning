# Generated by Django 2.2.7 on 2020-02-04 23:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='eleve',
            name='grade_eleve',
        ),
        migrations.CreateModel(
            name='Responsable_Eleve',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('login_res', models.CharField(max_length=40)),
                ('nom_res', models.CharField(max_length=50)),
                ('prenom_res', models.CharField(max_length=50)),
                ('pasword_res', models.CharField(max_length=40)),
                ('nom_classe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.Classe')),
            ],
            options={
                'verbose_name': 'Responsable de classe',
                'ordering': ['login_res'],
            },
        ),
        migrations.CreateModel(
            name='Planning',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('heure', models.CharField(max_length=7, null=True)),
                ('moduleLundi', models.CharField(blank=True, max_length=30)),
                ('moduleMardi', models.CharField(blank=True, max_length=30)),
                ('moduleMercredi', models.CharField(blank=True, max_length=30)),
                ('moduleJeudi', models.CharField(blank=True, max_length=30)),
                ('moduleVendredi', models.CharField(blank=True, max_length=30)),
                ('moduleSamedi', models.CharField(blank=True, max_length=30)),
                ('id_classe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.Classe')),
                ('id_prof', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.Prof')),
            ],
            options={
                'verbose_name': 'Planning',
            },
        ),
    ]
