__author__ = 'hpp'
from django import template
from wagsite_links.models import Link, LinkBoard

register = template.Library()

@register.inclusion_tag('wagsite_links/tags/links.html', takes_context=True)

def link_board(context, title):
    lb = LinkBoard.objects.filter(board_title__iexact=title).first()
    if lb:
        links = lb.links.all().order_by('link_order')
    else:
        links = []
    return {
        'links'     : links,
        'request'   : context['request']
    }

@register.inclusion_tag('wagsite_links/tags/links.html', takes_context=True)

def links_all(context):
    lb = Link.objects.all().order_by('link_order')
    if lb:
        links = lb
    else:
        links = []
    return {
        'links'     : links,
        'request'   : context['request']
    }

@register.inclusion_tag('wagsite_links/tags/links_widget.html', takes_context=True)

def links_all_widget(context):
    lb = Link.objects.all().order_by('link_order')
    if lb:
        links = lb
    else:
        links = []
    return {
        'links'     : links,
        'request'   : context['request']
    }

