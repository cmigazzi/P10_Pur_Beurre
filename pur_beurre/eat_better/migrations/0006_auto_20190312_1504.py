# Generated by Django 2.1.7 on 2019-03-12 14:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('eat_better', '0005_auto_20190308_1520'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='nutriments',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='eat_better.Nutriments'),
        ),
    ]
