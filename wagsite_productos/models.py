
from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.db import models
from django.db.models import F
from django import forms
from wagtail import hooks
from wagtail.admin.panels import FieldPanel, InlinePanel, MultiFieldPanel


from modelcluster.fields import ParentalKey
from taggit.models import TaggedItemBase

from wagtail.fields import RichTextField
from wagtail.models import Page, Orderable
from wagtail.search import index

from wagtail.snippets.models import register_snippet


# Create your models here.
class ProductoIndexPage(Page):
    max_count = 1
    intro = RichTextField(blank=True)
    content_panels = Page.content_panels + [
        FieldPanel('intro', classname="full")
    ]
    subpage_types = ['ProductoPage']


    class Meta:
        verbose_name = "Listado de Productos"
        verbose_name_plural = "Listados de Productos"


@register_snippet
class ProductoCategory(models.Model):
    name = models.CharField(max_length=255)
    icon = models.ForeignKey(
        'wagtailimages.Image', null=True, blank=True,
        on_delete=models.SET_NULL, related_name='+'
    )

    panels = [
        FieldPanel('name'),
        FieldPanel('icon'),
    ]

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Categorías de Productos'
        verbose_name = 'Categoría de Productos'

class ProductoPageTag(TaggedItemBase):
    content_object = ParentalKey(
        'ProductoPage',
        related_name='tagged_items',
        on_delete=models.CASCADE
    )

    class Meta:
        verbose_name_plural = 'Etiquetas de Productos'
        verbose_name = 'Etiqueta de Productos'

class ProductoPage(Page):
    view_count = models.PositiveBigIntegerField(default=0, db_index=True)
    date = models.DateField("Post date")
    name = models.CharField(max_length=255, null=True)
    description = RichTextField(blank=True)
    price = models.DecimalField(max_digits=12, decimal_places=2, null=True)
    stock = models.IntegerField(null=True)
    # tags = ClusterTaggableManager(through=ProductoPageTag, blank=True)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    category = models.ForeignKey(ProductoCategory, on_delete=models.SET_NULL, null=True, blank=True)

    # def save(self, *args, **kwargs):
    #     if not self.author_id:
    #         self.author_id = self.get_latest_revision().user_id
    #     super(BlogPage, self).save(*args, **kwargs)

    def main_image(self):
        gallery_item = self.gallery_images.first()
        if gallery_item:
            return gallery_item.image
        else:
            return None

    # def get_tags(self):
    #     return ProductoPageTag.objects.all()

    @hooks.register("before_serve_page")
    def increment_view_count(page, request, serve_args, serve_kwargs):
        if page.specific_class == ProductoPage:
            ProductoPage.objects.filter(pk=page.pk).update(view_count=F('view_count') + 1)

    search_fields = Page.search_fields + [
        index.SearchField('name'),
        index.SearchField('description'),
    ]

    content_panels = Page.content_panels + [
        MultiFieldPanel([
            FieldPanel('date'),
            # FieldPanel('tags'),
            FieldPanel('category'),
        ], heading="Producto Informacion"),
        FieldPanel('name'),
        FieldPanel('description'),
        FieldPanel('price'),
        FieldPanel('stock'),
        InlinePanel('gallery_images', label="Gallery images")

    ]

    class Meta:
        verbose_name = "Producto"
        verbose_name_plural = "Productos"

class BlogPageGalleryImage(Orderable):
    page = ParentalKey(ProductoPage, on_delete=models.CASCADE, related_name='gallery_images')
    image = models.ForeignKey(
        'wagtailimages.Image', on_delete=models.CASCADE, related_name='+'
    )
    caption = models.CharField(blank=True, max_length=250)

    panels = [
        FieldPanel('image'),
        FieldPanel('caption'),
    ]

    class Meta:
        verbose_name = "Galería de Productos"
        verbose_name_plural = "Galerías de las Productos"


class ProductoTagIndexPage(Page):

    def get_context(self, request):

        # Filter by tag
        tag = request.GET.get('tag')
        productopages = ProductoPage.objects.filter(tags__name=tag)

        # Update template context
        context = super().get_context(request)
        context['productopages'] = productopages
        return context

    class Meta:
        verbose_name_plural = 'Listado de Etiquetas de Productos'
        verbose_name = 'Listado de Etiquetas de Productos'







