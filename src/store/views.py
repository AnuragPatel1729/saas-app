from django.shortcuts import render
from visits.models import PageVisit


def home_view(request, *args, **kwargs):
    qs = PageVisit.objects.all()
    page_qs = PageVisit.objects.filter(path=request.path)
    try:
        percent = (page_qs.count() / qs.count()) * 100
    except:
        percent = 0
    PageVisit.objects.create(path=request.path)
    context = {'page_title': 'Home', 'page_visit_count': page_qs.count(), 'total_visit_count':qs.count(),'percent':percent}
    return render(request, "home.html", context)
    

def about_view(request, *args, **kwargs):
    qs = PageVisit.objects.all()
    page_qs = PageVisit.objects.filter(path=request.path)
    try:
        percent = (page_qs.count() / qs.count()) * 100
    except:
        percent = 0
    PageVisit.objects.create(path=request.path)
    context = {'page_title': 'About', 'page_visit_count': page_qs.count(), 'total_visit_count':qs.count(),'percent':percent}
    return render(request, "about.html", context)
    