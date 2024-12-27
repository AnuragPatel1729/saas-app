from django.shortcuts import render
from visits.models import PageVisit


def home_page_view(request, *args, **kwargs):
    queryset = PageVisit.objects.all()
    path = request.path
    PageVisit.objects.create(path=path)
    context = {'page_title': 'Home', 'queryset': queryset}
    return render(request, "home.html", context)