from django.db import models
from wagtail.admin.panels import FieldPanel
from wagtail.snippets.models import register_snippet


# Create your models here.
@register_snippet
class IconFontawesome(models.Model):
    name = models.CharField(max_length=255)
    icon_class = models.CharField(max_length=255)

    panels = [
        FieldPanel('name'),
        FieldPanel('icon_class'),
    ]

    def __str__(self):
        return self.name