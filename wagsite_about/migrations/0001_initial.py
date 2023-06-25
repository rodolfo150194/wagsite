# Generated by Django 4.1.9 on 2023-06-19 19:43

from django.db import migrations, models
import django.db.models.deletion
import wagtail.blocks
import wagtail.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('wagtailcore', '0083_workflowcontenttype'),
    ]

    operations = [
        migrations.CreateModel(
            name='AboutIndexPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.page')),
            ],
            options={
                'verbose_name': 'About',
            },
            bases=('wagtailcore.page',),
        ),
        migrations.CreateModel(
            name='AboutPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.page')),
                ('body', wagtail.fields.StreamField([('propiedad', wagtail.blocks.StructBlock([('name', wagtail.blocks.CharBlock(max_length=255)), ('descripcion', wagtail.blocks.RichTextBlock(max_length=255))], icon='user'))], use_json_field=True)),
            ],
            options={
                'verbose_name': 'Abouts',
            },
            bases=('wagtailcore.page',),
        ),
    ]
