# Generated by Django 5.1 on 2024-08-17 12:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('launch', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='confession',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('server_id', models.BigIntegerField()),
                ('count', models.BigIntegerField()),
                ('message', models.CharField(max_length=2000)),
            ],
        ),
    ]
