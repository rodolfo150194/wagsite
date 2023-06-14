# Generated by Django 4.1.9 on 2023-06-11 23:08

from django.db import migrations, models
import django.db.models.deletion
import wagsite_streams.blocks
import wagtail.blocks
import wagtail.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('wagtailcore', '0083_workflowcontenttype'),
    ]

    operations = [
        migrations.CreateModel(
            name='Services',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.page')),
                ('content', wagtail.fields.StreamField([('Servicio', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(help_text='Añade tu título', required=True)), ('icon', wagtail.blocks.CharBlock(help_text='Añade tu icono font-awesome', required=True)), ('text', wagtail.blocks.RichTextBlock(help_text='Añade el Texto adicional', required=True)), ('button_page', wagtail.blocks.PageChooserBlock(help_text='Pagina'))]))], blank=True, null=True, use_json_field=None)),
                ('description', wagtail.fields.StreamField([('Descripcion', wagsite_streams.blocks.RichtextBlock())], blank=True, null=True, use_json_field=None)),
            ],
            options={
                'verbose_name': 'Servicio',
                'verbose_name_plural': 'Servicios',
            },
            bases=('wagtailcore.page',),
        ),
        migrations.CreateModel(
            name='ServicesIndexPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.page')),
                ('intro', wagtail.fields.RichTextField(blank=True)),
            ],
            options={
                'verbose_name': 'Listado de Servicios',
                'verbose_name_plural': 'Listado de Servicios',
            },
            bases=('wagtailcore.page',),
        ),
    ]
