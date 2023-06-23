from django.db import models

# Create your models here.
from django.db import models
from wagtail import blocks
from wagtail.admin.panels import FieldPanel

from wagtail.fields import StreamField, RichTextField
from wagtail.images.blocks import ImageChooserBlock
from wagtail.models import Page

from wagsite_teams.models import SocialNetwork


# Create your models here.
class ServicesIndexPage(Page):
    max_count = 1

    subpage_types = ['Services']

    class Meta:
        verbose_name = "Listado de Servicios"
        verbose_name_plural = "Listado de Servicios"


class Services(Page):
    body = StreamField([
        ('servicio', blocks.StructBlock([
            ('title', blocks.CharBlock(required=True, help_text='Añade tu título')),
            ('icon', blocks.CharBlock(required=True, help_text='Añade tu icono de awesome')),
            ('text', blocks.CharBlock(required=True, help_text='Añade una descripcion')),
            ('image', ImageChooserBlock(label="Image"))
        ], icon='user')
         ),

    ], use_json_field=True)



    content_panels = Page.content_panels + [
        FieldPanel("body"),
    ]

    class Meta:
        verbose_name = "Servicio"
        verbose_name_plural = "Servicios"
