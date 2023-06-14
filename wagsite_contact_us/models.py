from django.db import models
from wagtail.admin.panels import FieldPanel

from wagtail.snippets.models import register_snippet

# Create your models here.
@register_snippet
class ContactUs(models.Model):
    name = models.CharField(max_length=250)
    email = models.EmailField(max_length=250)
    phone = models.CharField(max_length=250, null=True, blank=True)
    message = models.TextField()

    panels = [
        FieldPanel('name'),
        FieldPanel('email'),
        FieldPanel('phone'),
        FieldPanel('message'),
    ]

    class Meta:
        verbose_name = "Contacto"
        verbose_name_plural = "Contactos"

    def __str__(self):
        return self.name + " - " + self.email
