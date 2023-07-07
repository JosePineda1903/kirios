# Generated by Django 4.1.5 on 2023-01-05 22:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SobreNosotros',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion_titulo', models.CharField(blank=True, max_length=200, null=True)),
                ('titulo_secundario', models.CharField(blank=True, max_length=100, null=True)),
                ('descripcion', models.TextField(blank=True, null=True)),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='')),
            ],
            options={
                'verbose_name': 'SobreNosotros',
                'verbose_name_plural': 'SobreNosotros',
            },
        ),
    ]
