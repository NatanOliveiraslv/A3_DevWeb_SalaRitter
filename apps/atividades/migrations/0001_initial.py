# Generated by Django 4.1 on 2023-11-25 20:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('usuarios', '0004_aluno_email_professor_email'),
        ('materia', '0002_remove_materia_turma'),
        ('turma', '0003_alter_turma_materias'),
    ]

    operations = [
        migrations.CreateModel(
            name='Atividade',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100)),
                ('descricao', models.TextField()),
                ('materia', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='materia.materia')),
                ('turma', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='turma.turma')),
            ],
        ),
        migrations.CreateModel(
            name='AtividadeConcluida',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('resposta', models.TextField()),
                ('aluno', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='usuarios.aluno')),
                ('atividade', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='atividades.atividade')),
            ],
        ),
    ]
