from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import *
# Create your views here.


def save_contact(request):
    if request.POST:
        form = ContactUsForm(request.POST)
        if form.is_valid():
            form.save()
            # messages.success(request, _('El elemento ha sido actualizado satisfactoriamente'))
            return HttpResponseRedirect('/')
    else:
        return HttpResponseRedirect('/')
