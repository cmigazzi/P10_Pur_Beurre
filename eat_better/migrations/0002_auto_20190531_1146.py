# Generated by Django 2.2.1 on 2019-05-31 09:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('eat_better', '0001_initial'),
    ]

    database_operations = [
        migrations.AlterModelTable('Substitution', 'my_products_substitution')
                          ]

    state_operations = [migrations.DeleteModel('Substitution')]

    operations = [
        migrations.SeparateDatabaseAndState(
            database_operations=database_operations,
            state_operations=state_operations)
    ]