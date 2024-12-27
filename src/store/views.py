from django.shortcuts import render
from visits.models import PageVisit


def home_page_view(request, *args, **kwargs):
    qs = PageVisit.objects.all()
    page_qs = PageVisit.objects.filter(path=request.path)
    path = request.path
    PageVisit.objects.create(path=path)
    context = {'page_title': 'Home', 'page_visit_count': page_qs.count(), 'total_visit_count':qs.count()}
    return render(request, "home.html", context)