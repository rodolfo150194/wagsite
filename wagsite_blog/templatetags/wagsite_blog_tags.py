from django import template
from django.template.defaultfilters import stringfilter
from wagsite_blog.models import *

register = template.Library()
@register.inclusion_tag("wagsite_blog/blog_carousel.html", takes_context=True)
def blog_carousel(context):
    request = context['request']
    noticias = BlogPage.objects.filter(categories__name='Noticias').order_by('date').reverse()[:10]
    # ~ return context['noticias'] = noticias
    return {
        "noticias": noticias,
        # ~ 'user': request.user,
        # ~ 'path': request.path,
        # ~ 'about_us_obj': about_us_obj,
        # ~ 'permitted': permitted
    }

@register.inclusion_tag("wagsite_blog/blog_visited.html", takes_context=True)
def blog_visited_widget(context):
    request = context['request']
    noticias = BlogPage.objects.filter(categories__name='Noticias').order_by('view_count').reverse()[:5]
    # ~ return context['noticias'] = noticias
    return {
        "noticias": noticias,
        # ~ 'user': request.user,
        # ~ 'path': request.path,
        # ~ 'about_us_obj': about_us_obj,
        # ~ 'permitted': permitted
    }
