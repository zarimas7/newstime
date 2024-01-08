from . import views
from django.urls import path
from django.urls import path



urlpatterns = [path('', views.index,name='main'),
            path('<int:pk>/', views.NewsDetailView.as_view(), name='mydetail'),
            path('registr/', views.UserRegister.as_view()),
            path('contact/', views.contact,name='contact')

]