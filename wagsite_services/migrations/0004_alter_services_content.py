# Generated by Django 4.1.9 on 2023-06-12 19:44

from django.db import migrations
import wagtail.blocks
import wagtail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('wagsite_services', '0003_alter_services_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='services',
            name='content',
            field=wagtail.fields.StreamField([('Servicio', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(help_text='Añade tu título', required=True)), ('icon', wagtail.blocks.CharBlock(help_text='Añade tu icono font-awesome', required=True)), ('text', wagtail.blocks.RichTextBlock(help_text='Añade el Texto adicional', required=True)), ('button_page', wagtail.blocks.PageChooserBlock(help_text='Pagina'))]))], blank=True, null=True, use_json_field=None),
        ),
    ]
