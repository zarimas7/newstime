from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView, TemplateView, CreateView
from django.shortcuts import render
import requests
from .forms import UserCustomForm
from .models import News, Image


# @login_required
def index(request):


# URL Binance API для получения текущих котировок
    binance_api_url = "https://api.binance.com/api/v3/ticker/price"

    # Символы пар валют, для которых вы хотите получить котировки
    symbols = ["BTCTUSD", "TUSDBTC", "ETHTUSD",]  # Например, сом к вону, доллару, евро

    # Словарь для хранения котировок
    quotes = {}

    # Запрос к Binance API для каждой пары валют
    for symbol in symbols:
        response = requests.get(binance_api_url, params={"symbol": symbol})

        print(f"Symbol: {symbol}, Status Code: {response.status_code}")

        if response.status_code == 200:
            data = response.json()
            price = data.get("price", "N/A")
            quotes[symbol] = price
        else:
            quotes[symbol] = f"Ошибка при получении котировок: {response.status_code}"

    print(quotes)
    news = News.objects.all()
    # Передача котировок в шаблон и рендеринг его
    return render(request, 'main.html', {'quotes': quotes,"news": news})

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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['images'] = self.object.image_set.all()
        return context
# Create your views here.




