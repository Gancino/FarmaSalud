# Generated by Django 3.2.5 on 2021-07-20 15:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('FarmaSaludApp', '0002_rename_fk_id_cat_producto_fk_idcat'),
    ]

    operations = [
        migrations.RenameField(
            model_name='producto',
            old_name='fk_idcat',
            new_name='fk_id_cat',
        ),
    ]