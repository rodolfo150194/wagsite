# Generated by Django 4.1.9 on 2023-06-13 02:45

from django.db import migrations, models
import django.db.models.deletion
import wagsite_streams.blocks
import wagtail.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('wagtailcore', '0083_workflowcontenttype'),
    ]

    operations = [
        migrations.CreateModel(
            name='Events',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.page')),
                ('start_date', models.DateField(verbose_name='Fecha de Inicio')),
                ('end_date', models.DateField(verbose_name='Fecha Final')),
                ('content', wagtail.fields.StreamField([('Evento', wagsite_streams.blocks.RichtextBlock())], blank=True, null=True, use_json_field=None)),
            ],
            options={
                'verbose_name': 'Evento',
                'verbose_name_plural': 'Eventos',
            },
            bases=('wagtailcore.page',),
        ),
        migrations.CreateModel(
            name='EventsIndexPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.page')),
                ('intro', wagtail.fields.RichTextField(blank=True)),
            ],
            options={
                'verbose_name': 'Listado de Eventos',
                'verbose_name_plural': 'Listado de Eventos',
            },
            bases=('wagtailcore.page',),
        ),
    ]
