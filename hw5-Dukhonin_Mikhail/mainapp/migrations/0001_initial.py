# Generated by Django 3.2 on 2021-06-03 12:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BookCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, unique=True, verbose_name='Название')),
                ('description', models.CharField(blank=True, max_length=512, verbose_name='Описание')),
            ],
        ),
        migrations.CreateModel(
            name='Books',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256, verbose_name='Заголовок')),
                ('author', models.CharField(blank=True, max_length=255, verbose_name='Автор(ы)')),
                ('annotation', models.TextField(blank=True, verbose_name='Аннотация')),
                ('cover', models.ImageField(blank=True, upload_to='covers', verbose_name='Обложка')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Добавлен')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Обновлён')),
                ('cat_fk', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.bookcategory')),
            ],
        ),
    ]
