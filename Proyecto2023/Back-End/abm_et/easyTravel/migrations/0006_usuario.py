# Generated by Django 4.2.1 on 2023-06-16 05:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('easyTravel', '0005_delete_usuario'),
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id_usuario', models.AutoField(primary_key=True, serialize=False)),
                ('nperfil', models.IntegerField()),
                ('nombre', models.CharField(max_length=100)),
                ('apellidos', models.CharField(max_length=100)),
                ('fecha_nac', models.DateField()),
                ('celular', models.CharField(max_length=100)),
                ('mail', models.CharField(max_length=100)),
                ('puntaje', models.IntegerField(default=0)),
            ],
            options={
                'verbose_name': 'Usuarios de EasyTravel',
                'verbose_name_plural': 'Usuarios',
                'db_table': 'Usuario',
            },
        ),
    ]