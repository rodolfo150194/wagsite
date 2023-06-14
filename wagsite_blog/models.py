from django.db import models

# Create your models here.
from django.db import models
from django.db.models import F
from django import forms
from wagtail import hooks
from wagtail.admin.panels import FieldPanel, InlinePanel, MultiFieldPanel


from modelcluster.fields import ParentalKey, ParentalManyToManyField
from modelcluster.contrib.taggit import ClusterTaggableManager
from taggit.models import TaggedItemBase

from wagtail.fields import RichTextField
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.models import Page, Orderable
from wagtail.search import index

from wagtail.snippets.models import register_snippet


# Create your models here.
class BlogIndexPage(Page):
    max_count = 1
    intro = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('intro', classname="full")
    ]

    class Meta:
        verbose_name = "Listado de Artículos"
        verbose_name_plural = "Listados de Artículos"


class BlogPageTag(TaggedItemBase):
    content_object = ParentalKey(
        'BlogPage',
        related_name='tagged_items',
        on_delete=models.CASCADE
    )

    class Meta:
        verbose_name_plural = 'Etiquetas de Artículos'
        verbose_name = 'Etiqueta de Artículos'


class BlogPage(Page):
    view_count = models.PositiveBigIntegerField(default=0, db_index=True)
    date = models.DateField("Post date")
    intro = models.CharField(max_length=250, blank=True)
    body = RichTextField(blank=True)
    tags = ClusterTaggableManager(through=BlogPageTag, blank=True)
    categories = ParentalManyToManyField('wagsite_blog.BlogCategory', blank=True)

    def main_image(self):
        gallery_item = self.gallery_images.first()
        if gallery_item:
            return gallery_item.image
        else:
            return None

    def get_tags(self):
        return BlogPageTag.objects.all()

    @hooks.register("before_serve_page")
    def increment_view_count(page, request, serve_args, serve_kwargs):
        if page.specific_class == BlogPage:
            BlogPage.objects.filter(pk=page.pk).update(view_count=F('view_count') + 1)

    search_fields = Page.search_fields + [
        index.SearchField('intro'),
        index.SearchField('body'),
    ]

    content_panels = Page.content_panels + [
        MultiFieldPanel([
            FieldPanel('date'),
            FieldPanel('tags'),
            FieldPanel('categories', widget=forms.CheckboxSelectMultiple),
            ], heading="Blog Information"),
        FieldPanel('intro'),
        FieldPanel('body', classname="full"),
        InlinePanel('gallery_images', label="Gallery images")

    ]

    class Meta:
        verbose_name = "Artículo"
        verbose_name_plural = "Artículos"


class BlogPageGalleryImage(Orderable):
    page = ParentalKey(BlogPage, on_delete=models.CASCADE, related_name='gallery_images')
    image = models.ForeignKey(
        'wagtailimages.Image', on_delete=models.CASCADE, related_name='+'
    )
    caption = models.CharField(blank=True, max_length=250)

    panels = [
        FieldPanel('image'),
        FieldPanel('caption'),
    ]

    class Meta:
        verbose_name = "Galería de Artículos"
        verbose_name_plural = "Galerías de las Artículos"


class BlogTagIndexPage(Page):

    def get_context(self, request):

        # Filter by tag
        tag = request.GET.get('tag')
        blogpages = BlogPage.objects.filter(tags__name=tag)

        # Update template context
        context = super().get_context(request)
        context['blogpages'] = blogpages
        return context

    class Meta:
        verbose_name_plural = 'Listado de Etiquetas de Artículos'
        verbose_name = 'Listado de Etiquetas de Artículos'


@register_snippet
class BlogCategory(models.Model):
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
        verbose_name_plural = 'Categorías de Artículos'
        verbose_name = 'Categoría de Artículos'
