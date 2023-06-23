from django.contrib.auth.models import User
from django.db import models
from modelcluster.fields import ParentalKey
from wagtail import blocks
from wagtail.admin.panels import FieldPanel
from wagtail.fields import RichTextField, StreamField
from wagtail.models import Page, Orderable


# Create your models here.
class Faq(Orderable):
    page = ParentalKey('FaqPage', related_name='team_members')
    pregunta = models.CharField(max_length=255)
    respuesta = models.CharField(max_length=255)

    panels = [
        FieldPanel('pregunta'),
        FieldPanel('respuesta'),
    ]
class FaqPage(Page):
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True,blank=True)
    body = StreamField([
        ('faq', blocks.StructBlock([
            ('pregunta', blocks.CharBlock(max_length=255)),
            ('respuesta', blocks.CharBlock(max_length=255)),
            ], icon='user')),

    ],null=True,blank=True, use_json_field=True)

    content_panels = Page.content_panels + [
        FieldPanel('body'),
    ]