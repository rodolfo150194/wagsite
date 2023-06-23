from wagtail import blocks
from wagtail.admin.panels import FieldPanel
from wagtail.fields import StreamField, RichTextField
from wagtail.models import Page


class AboutPage(Page):
    max_count = 1
    intro = RichTextField(blank=True)
    body = StreamField([
         # ('image', ImageChooserBlock()),
        ('propiedad', blocks.StructBlock([
            ('order', blocks.IntegerBlock()),
            ('name', blocks.CharBlock(max_length=255)),
            ('descripcion', blocks.RichTextBlock(max_length=255)),
        ], icon='user')),

    ], use_json_field=True)

    content_panels = Page.content_panels + [
        FieldPanel('intro'),
        FieldPanel('body'),
    ]
    # def __str__(self):
    #     return self.body.name

    class Meta:
        verbose_name = "Abouts"
