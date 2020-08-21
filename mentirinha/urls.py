from django.urls import path, re_path

from mentirinha import views

urlpatterns = [
    path('list', views.list_all, name='list'),
    path('<short_code>', views.redirect_to)
]
