from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views.generic import DetailView, ListView, TemplateView



from .models import News


# @login_required
def index(request):
    news = News.objects.all()
    return render(request, 'main.html', {"news": news})




# Create your views here.



