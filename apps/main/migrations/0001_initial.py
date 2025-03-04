# Generated by Django 5.1.6 on 2025-03-04 05:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dictionary',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated at')),
                ('base_lang', models.CharField(max_length=2)),
                ('target_lang', models.CharField(max_length=2)),
                ('word', models.CharField(max_length=100)),
                ('translation', models.CharField(max_length=100)),
                ('user', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Dictionary',
                'verbose_name_plural': 'Dictionaries',
                'unique_together': {('base_lang', 'target_lang', 'word', 'user')},
            },
        ),
    ]
