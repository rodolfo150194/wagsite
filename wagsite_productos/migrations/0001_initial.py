# Generated by Django 4.1.9 on 2023-06-22 18:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import modelcluster.fields
import wagtail.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('taggit', '0005_auto_20220424_2025'),
        ('wagtailcore', '0083_workflowcontenttype'),
        ('wagtailimages', '0025_alter_image_file_alter_rendition_file'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductoCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('icon', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image')),
            ],
            options={
                'verbose_name': 'Categoría de Productos',
                'verbose_name_plural': 'Categorías de Productos',
            },
        ),
        migrations.CreateModel(
            name='ProductoIndexPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.page')),
                ('intro', wagtail.fields.RichTextField(blank=True)),
            ],
            options={
                'verbose_name': 'Listado de Productos',
                'verbose_name_plural': 'Listados de Productos',
            },
            bases=('wagtailcore.page',),
        ),
        migrations.CreateModel(
            name='ProductoPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.page')),
                ('view_count', models.PositiveBigIntegerField(db_index=True, default=0)),
                ('date', models.DateField(verbose_name='Post date')),
                ('name', models.CharField(max_length=255, null=True)),
                ('description', wagtail.fields.RichTextField(blank=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=12, null=True)),
                ('stock', models.IntegerField(null=True)),
                ('author', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('categories', modelcluster.fields.ParentalManyToManyField(blank=True, to='wagsite_productos.productocategory')),
            ],
            options={
                'verbose_name': 'Producto',
                'verbose_name_plural': 'Productos',
            },
            bases=('wagtailcore.page',),
        ),
        migrations.CreateModel(
            name='ProductoTagIndexPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.page')),
            ],
            options={
                'verbose_name': 'Listado de Etiquetas de Productos',
                'verbose_name_plural': 'Listado de Etiquetas de Productos',
            },
            bases=('wagtailcore.page',),
        ),
        migrations.CreateModel(
            name='ProductoPageTag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content_object', modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='tagged_items', to='wagsite_productos.productopage')),
                ('tag', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='%(app_label)s_%(class)s_items', to='taggit.tag')),
            ],
            options={
                'verbose_name': 'Etiqueta de Productos',
                'verbose_name_plural': 'Etiquetas de Productos',
            },
        ),
        migrations.CreateModel(
            name='BlogPageGalleryImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sort_order', models.IntegerField(blank=True, editable=False, null=True)),
                ('caption', models.CharField(blank=True, max_length=250)),
                ('image', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='wagtailimages.image')),
                ('page', modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='gallery_images', to='wagsite_productos.productopage')),
            ],
            options={
                'verbose_name': 'Galería de Productos',
                'verbose_name_plural': 'Galerías de las Productos',
            },
        ),
    ]
