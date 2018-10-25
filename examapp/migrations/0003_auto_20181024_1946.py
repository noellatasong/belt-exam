# Generated by Django 2.1.2 on 2018-10-24 19:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('examapp', '0002_remove_users_doh'),
    ]

    operations = [
        migrations.RenameField(
            model_name='added',
            old_name='add',
            new_name='item',
        ),
        migrations.RenameField(
            model_name='items',
            old_name='item',
            new_name='product',
        ),
        migrations.AlterField(
            model_name='items',
            name='added_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='examapp.Users'),
        ),
    ]
