from django.db import models
from modelcluster.fields import ParentalKey
from wagtail import blocks
from wagtail.admin.panels import FieldPanel, InlinePanel
from wagtail.blocks import StructBlock, CharBlock, URLBlock
from wagtail.fields import StreamField
from wagtail.images.blocks import ImageChooserBlock
from wagtail.models import Orderable, Page


class TeamMember(Orderable):
    page = ParentalKey('TeamPage', related_name='team_members')
    name = models.CharField(max_length=255)
    role = models.CharField(max_length=255)
    image = models.ForeignKey(
        'wagtailimages.Image', on_delete=models.CASCADE, related_name='+'
    )
    panels = [
        FieldPanel('image'),
        FieldPanel('name'),
        FieldPanel('role'),
    ]


class SocialNetwork(StructBlock):
    name = CharBlock(max_length=255)
    url = URLBlock()

    class Meta:
        icon = 'grip'


class TeamPage(Page):
    # Campos personalizados
    body = StreamField([
        ('text', blocks.RichTextBlock()),
        ('image', ImageChooserBlock()),
        ('team_member', blocks.StructBlock([
            ('name', blocks.CharBlock(max_length=255)),
            ('role', blocks.CharBlock(max_length=255)),
            ('image', ImageChooserBlock()),
            ('social_media', blocks.ListBlock(SocialNetwork(label='Social Network'))),
        ], icon='user')),

    ])

    # Paneles de configuración del admin de la página
    content_panels = Page.content_panels + [
        FieldPanel('body'),
    ]

    # Paneles de configuración del admin para los miembros de equipo
    promote_panels = Page.promote_panels + [
        InlinePanel('team_members', label="Equipo"),
    ]