from django.db import models

# Create your models here.
from django.db import models
from wagtail.admin.panels import FieldPanel

from wagtail.fields import StreamField, RichTextField
from wagtail.models import Page

from wagsite_streams import blocks


# Create your models here.
class ServicesIndexPage(Page):
    max_count = 1
    intro = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('intro', classname="full")
    ]

    class Meta:
        verbose_name = "Listado de Servicios"
        verbose_name_plural = "Listado de Servicios"


class Services(Page):
    template = "wagsite_services/services.html"

    content = StreamField(
        [
          ("Servicio", blocks.TitleIconAndSimpleRichtextBlock()),
        ],
        null=True,
        blank=True,
        use_json_field=True
    )

    description = StreamField(
        [
          ("Descripcion", blocks.RichtextBlock()),
        ],
        null=True,
        blank=True,
        use_json_field=True
    )


    content_panels = Page.content_panels + [
        FieldPanel("content"),
        FieldPanel("description"),
    ]

    class Meta:
        verbose_name = "Servicio"
        verbose_name_plural = "Servicios"
