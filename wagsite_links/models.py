from django.db import models

# Create your models here.
from django.db import models
from wagtail.admin.panels import FieldPanel, MultiFieldPanel, InlinePanel

from wagtail.core.models import Orderable
from wagtail.snippets.models import register_snippet
from wagtail.core.models import Orderable
from wagtail.core.fields import RichTextField
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.snippets.models import register_snippet
from wagtail.search import index
from modelcluster.models import ClusterableModel
from modelcluster.fields import ParentalKey

class Link(Orderable):
    SELF    = '_self'
    BLANK   = '_blank'
    PARENT  = '_parent'
    TOP     = '_top'
    NEW     = 'new'
    LINK_TARGET = ((SELF, 'Misma pestaña'),
                   (BLANK, 'Nueva pestaña'),
                   (PARENT, 'Ventana padre'),
                   (TOP, 'Ventana superior'),
                   (NEW, 'Nueva ventana'))
    link_text   = models.CharField('Texto', max_length=255, help_text='Texto del vínculo')
    link_url    = models.URLField('Url', max_length=255, help_text='Dirección URL [Si es un vínculo local, seleccione el resto de la URL que no incluye el nommbre de dominio]')
    link_title  = models.CharField('Título', max_length=255, help_text='Se colocará en el atributo "Title" del hipervínculo')
    link_target = models.CharField('Destino', max_length=10, choices=LINK_TARGET, default=SELF, help_text='Destino donde se abrirá el vínculo')
    link_icon   = models.ForeignKey('wagtailimages.image', on_delete=models.CASCADE, null=True, blank=True, verbose_name='Ícono')
    link_order  = models.IntegerField('Orden', default=1)
    link_board  = ParentalKey('wagsite_links.LinkBoard', on_delete=models.SET_NULL, blank=True, null=True, related_name='links')

    panels = [FieldPanel('link_text'), FieldPanel('link_url'), FieldPanel('link_title'), FieldPanel('link_target'),
              ImageChooserPanel('link_icon'), FieldPanel('link_order')]

    def __str__(self):
        return self.link_text



@register_snippet
class LinkBoard(ClusterableModel):
    board_title = models.CharField('Título', max_length=100)

    panels = [FieldPanel('board_title'), MultiFieldPanel([InlinePanel('links'), ], 'Links')]

    def __str__(self):
        return  self.board_title

    class Meta:
        verbose_name = 'Links'
        verbose_name_plural = 'Links'
