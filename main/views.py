from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView, TemplateView, CreateView

from .forms import UserCustomForm
from .models import News


# @login_required
def index(request):
    news = News.objects.all()
    return render(request, 'main.html', {"news": news})

from .forms import UserCustomForm

class UserCustomForm(CreateView):
    model = User
    template_name = 'registration/reg.html'
    form_class = UserCustomForm
    success_url = reverse_lazy('login')

class NewsDetailView(DetailView):
    model = News
    template_name = 'detail.html'
    context_object_name = 'news'
# Create your views here.



