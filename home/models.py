from django.db import models

from wagtail.models import Page

from wagsite_blog.models import BlogPage
from wagsite_teams.models import TeamPage
from wagsite_contact_us.forms import ContactUsForm
from wagsite_events.models import Events
from wagsite_services.models import Services


class HomePage(Page):
    def get_context(self, request):
        context = super().get_context(request)
        servicios = Services.objects.live()[:4]
        noticias = BlogPage.objects.filter(categories__name='Noticias').order_by('date').reverse()[:10]
        carrusel = BlogPage.objects.filter(categories__name='Noticias').order_by('date').reverse()[:5]
        team = TeamPage.objects.first()
        eventos = Events.objects.live().order_by('start_date')[:6]
        contact_form = ContactUsForm()
        context['noticias'] = noticias
        context['carrusel'] = carrusel
        context['eventos'] = eventos
        context['servicios'] = servicios
        context['teams'] = team
        context['contact_form'] = contact_form

        return context
