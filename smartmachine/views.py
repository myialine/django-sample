from django.shortcuts import render
from django.http import Http404

from .models import Machine


def home(request):
    try:
        machines = Machine.objects.all()
    except Machine.DoesNotExist:
        raise Http404('Machines not found')
    return render(request, 'home.html', {'machines': machines, })
