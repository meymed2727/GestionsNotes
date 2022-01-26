# Generated by Django 4.0.1 on 2022-01-19 23:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='classe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom_classe', models.CharField(max_length=100)),
                ('niveau_classe', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='etudiant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom_etudiant', models.CharField(max_length=100)),
                ('prenom_etudiant', models.CharField(max_length=100)),
                ('matricule_etudiant', models.CharField(max_length=100)),
                ('cin_etudiant', models.CharField(max_length=50)),
                ('date_nai_etudiant', models.CharField(max_length=100)),
                ('adresse_etudiant', models.CharField(max_length=100)),
                ('tel_etudiant', models.CharField(max_length=100)),
                ('classe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.classe')),
            ],
        ),
        migrations.CreateModel(
            name='matiere',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom_matiere', models.CharField(max_length=100)),
                ('coiffi_matiere', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='specialite',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom_specialite', models.CharField(max_length=100)),
                ('classe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.classe')),
            ],
        ),
        migrations.CreateModel(
            name='note',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Note_devoir', models.FloatField(default=0)),
                ('Note_examen', models.FloatField(default=0)),
                ('etudiant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.etudiant')),
                ('matiere', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.matiere')),
            ],
        ),
        migrations.CreateModel(
            name='module',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom_module', models.CharField(max_length=100)),
                ('coiffi_module', models.CharField(max_length=100)),
                ('classe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.classe')),
            ],
        ),
        migrations.AddField(
            model_name='matiere',
            name='module',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.module'),
        ),
    ]
