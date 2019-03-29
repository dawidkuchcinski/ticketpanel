# Generated by Django 2.2 on 2018-12-30 12:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Apps',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app_name', models.CharField(max_length=254, unique=True)),
                ('app_desc', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Statuses',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status_name', models.CharField(max_length=254, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Types',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_name', models.CharField(max_length=254, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Tickets',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('temat', models.CharField(max_length=254)),
                ('tresc', models.TextField()),
                ('data_utworzenia', models.DateTimeField(auto_now_add=True)),
                ('data_ostatniej_modyfikacji', models.DateTimeField()),
                ('aplikacja', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ticketlist.Apps')),
                ('status', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ticketlist.Statuses')),
                ('typ', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ticketlist.Types')),
            ],
        ),
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('commentauthor', models.CharField(max_length=254)),
                ('commentcontent', models.TextField()),
                ('commentdate', models.DateTimeField(auto_now_add=True)),
                ('ticket', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ticketlist.Tickets')),
            ],
        ),
    ]
