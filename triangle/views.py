from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from math import sqrt

from .forms import TriangleForm


def validate(request):
    if request.method == 'POST':
        form = TriangleForm(request.POST)
        if form.is_valid():
            leg_a = form.cleaned_data['leg_a']
            leg_b = form.cleaned_data['leg_b']
            form.hypotenuse = sqrt(leg_a ** 2 + leg_b ** 2)
            return HttpResponseRedirect("/triangle/")
    else:
        form = TriangleForm()
    return render(request, 'triangle.html', {'form': form})
