from django.db import models

# Create your models here.
from django.db import models
from wagtail.admin.panels import FieldPanel
from wagtail.fields import StreamField, RichTextField

from wagtail.models import Page

from wagsite_streams import blocks


# Create your models here.
class EventsIndexPage(Page):
    max_count = 1
    intro = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('intro', classname="full")
    ]

    class Meta:
        verbose_name = "Listado de Eventos"
        verbose_name_plural = "Listado de Eventos"


class Events(Page):
    template = "wagtail_events/events.html"

    start_date = models.DateField("Fecha de Inicio")
    end_date = models.DateField("Fecha Final")

    content = StreamField(
        [
          ("Evento", blocks.RichtextBlock())
        ],
        null=True,
        blank=True,
        use_json_field=True
    )

    content_panels = Page.content_panels + [
        FieldPanel('start_date'),
        FieldPanel('end_date'),
        FieldPanel("content"),
    ]

    class Meta:
        verbose_name = "Evento"
        verbose_name_plural = "Eventos"
