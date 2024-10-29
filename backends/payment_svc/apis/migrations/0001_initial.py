# Generated by Django 5.1.2 on 2024-10-22 20:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('amount', models.FloatField()),
                ('user_id', models.BigIntegerField()),
                ('user_name', models.CharField(max_length=100)),
            ],
        ),
    ]