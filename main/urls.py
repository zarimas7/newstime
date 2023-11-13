from . import views
from django.urls import path


urlpatterns = [path('', views.index),
path('<int:pk>/', views.NewsDetailView.as_view(), name='mydetail')
]