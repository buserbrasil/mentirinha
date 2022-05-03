from django.urls import path, re_path

from mentirinha import views

urlpatterns = [
    path('', views.redirect_to),
    path('__ping', views.ping),
    path('<short_code>', views.redirect_to),
]
