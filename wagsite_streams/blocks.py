# from wagtail.core import blocks
from django.db import models
from wagtail import blocks
from wagtail.images import blocks as b

from wagsite_streams.models import IconFontawesome


class TitleIconAndSimpleRichtextBlock(blocks.StructBlock):
    title = blocks.CharBlock(required=True, help_text='Añade tu título')
    icon = blocks.CharBlock(required=True, help_text='Añade tu icono font-awesome')
    text = blocks.RichTextBlock(required=True, help_text='Añade el Texto adicional')
    button_page = blocks.PageChooserBlock(help_text="Pagina")

    class Meta:
        template = "wagsite_streams/title_and_text_block.html"
        icon = "edit"
        label = "Título, Icono y Texto"



class RichtextBlock(blocks.RichTextBlock):

    class Meta:
        template = "streams/richtext_block.html"
        icon = "doc-full"
        label = "Texto Enriquecido Completo"


class SimpleRichtextBlock(blocks.RichTextBlock):

    def __init__(self, required=True, help_text=None, editor='default', features=None, validators=(), **kwargs):
        self.features = [
            "bold",
            "italic",
            "link",
        ]
        super().__init__(**kwargs)

    class Meta:
        template = "wagsite_streams/simple_richtext_block.html"
        icon = "edit"
        label = "Texto Enriquecido Simple"


class SliderImageAndTextBlock(blocks.StructBlock):
    title = blocks.CharBlock(required=True, help_text='Añade tu título')
    text1 = blocks.CharBlock(required=True, help_text='Añade tu texto 1')
    text2 = blocks.CharBlock(required=True, help_text='Añade tu texto 2')
    text3 = blocks.CharBlock(required=True, help_text='Añade tu texto 3')
    image = b.ImageChooserBlock(required=True, help_text='Añade tu imagen (1908 x 850)')

    class Meta:
        template = "wagsite_streams/slider_image_and_text_block.html"
        icon = "image"
        label = "Imagen de Slider y Texto"
