# Generated by Django 5.1.5 on 2025-01-18 05:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(blank=True, max_length=100, null=True)),
                ('brand', models.CharField(blank=True, max_length=100, null=True)),
                ('price', models.FloatField()),
            ],
        ),
    ]
