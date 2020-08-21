from django.urls import path

from mentirinha import views

urlpatterns = [
    path('', views.index, name='index')
]
