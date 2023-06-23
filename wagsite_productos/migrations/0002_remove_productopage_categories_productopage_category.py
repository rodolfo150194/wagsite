# Generated by Django 4.1.9 on 2023-06-22 19:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagsite_productos', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productopage',
            name='categories',
        ),
        migrations.AddField(
            model_name='productopage',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='wagsite_productos.productocategory'),
        ),
    ]
