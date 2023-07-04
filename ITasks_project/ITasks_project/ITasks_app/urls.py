from . import views
from django.urls import path

urlpatterns = [

    # task 1
    # path('', views.home, name='home'),
    # path('about/', views.about, name='about'),
    # path('contact/', views.contact, name='contact'),
    # path('detail/', views.detail, name='detail'),
    # path('thanks/', views.thanks, name='thanks')

    # task 2
    path('', views.first, name='first'),
    path('ops/', views.ops, name='opr')
]
